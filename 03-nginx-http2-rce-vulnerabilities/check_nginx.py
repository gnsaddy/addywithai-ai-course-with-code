# check_nginx.py: exposed to the Nov 2026 NGINX HTTP/2 bugs? Read-only.
# Reads `nginx -v` + your config text. Changes nothing. Stdlib only.
import re, sys

FIXED = {(1, 30): (1, 30, 7), (1, 31): (1, 31, 9)}     # stable, mainline
BUGS = {"CVE-2026-123007": ((1, 9, 5), "send_window integer underflow"),
        "CVE-2026-123633": ((1, 19, 7), "use-after-free, proxy setups")}

def parse_version(text):
    m = re.search(r"nginx/(\d+)\.(\d+)\.(\d+)", text)
    return tuple(int(x) for x in m.groups()) if m else None

def is_fixed(v):
    if v >= (1, 31, 9): return True
    fix = FIXED.get(v[:2])
    return fix is not None and v >= fix

def scan_config(conf):
    lines = [l.split("#")[0].strip() for l in conf.splitlines()]
    h2 = [l for l in lines if re.match(r"http2\s+on", l)
          or (l.startswith("listen") and re.search(r"\bhttp2\b", l))]
    proxy = any(re.search(r"\bproxy_pass\b", l) for l in lines)
    return {"http2": bool(h2), "proxy": proxy,
            "tls": any(l.startswith("listen") and " ssl" in l for l in lines)}

def report(version_text, conf):
    v, c = parse_version(version_text), scan_config(conf)
    if v is None: return ["UNKNOWN  could not read the version"]
    name = ".".join(map(str, v)); out = []
    for cve, (first, what) in BUGS.items():
        hit = first <= v and not is_fixed(v)
        out.append(f"{'IN RANGE' if hit else 'fixed   '} {cve} ({what})")
    if not c["http2"]:
        out.append(f"LOW      nginx {name}: HTTP/2 is off, both bugs need it")
    elif is_fixed(v):
        out.append(f"PATCHED  nginx {name}: keep HTTP/2 on")
    else:
        extra = " + proxy" if c["proxy"] else ""
        out.append(f"HIGH     nginx {name}: HTTP/2 on{extra}.")
        out.append("         upgrade to 1.30.7 stable or 1.31.9 mainline,")
        out.append("         or set 'http2 off;' and remove http2 from listen")
    return out

if __name__ == "__main__":
    for path in sys.argv[1:] or ["samples/shop.conf"]:
        text = open(path, encoding="utf-8").read()
        ver = text.splitlines()[0]      # samples keep `nginx -v` on line 1
        print(f"== {path}")
        print("\n".join(report(ver, text)))
