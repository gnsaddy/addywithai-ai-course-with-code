# check_nginx.py: NGINX HTTP/2 bug exposure check (defensive, read-only)

Companion code for the @addywithai video "Learn the NGINX HTTP/2 RCE Bugs" (19 Nov 2026).
It answers one question for your own servers: **is my NGINX version in the affected range, and is HTTP/2 on?**
It only reads text. It never sends traffic, never touches a server and has no exploit code.

Facts used (from the Wiz Research write-up of 18 Nov 2026, "Unauthenticated Remote Code Execution in NGINX: CVE-2026-123633 and CVE-2026-123007"):
- CVE-2026-123007 (HTTP/2 `send_window` integer underflow): NGINX 1.9.5 to 1.31.8, default configs with HTTP/2 on.
- CVE-2026-123633 (HTTP/2 connection use-after-free): NGINX 1.19.7 to 1.31.8, mainly when NGINX proxies with HTTP/2 on.
- Fixed in NGINX open source **1.30.7 (stable)** and **1.31.9 (mainline)**. NGINX Plus has its own fixed builds (see F5).
- Both need HTTP/2. Temporary workaround if you cannot upgrade yet: `http2 off;` (NGINX 1.25.1+) and remove `http2` from `listen` lines, test, reload, re-enable after upgrading.

## Run the demo
```
python check_nginx.py samples/shop.conf samples/blog.conf samples/patched.conf
```
The three sample files are made-up configs. Line 1 of each holds the `nginx -v` output.

## Check your own server (one you own or run)
```
(nginx -v 2>&1; nginx -T 2>/dev/null) > mysite.conf     # version + full config, read-only
python check_nginx.py mysite.conf
```
`nginx -T` prints the full loaded config and the version comes first, so the script can read both.

## Limits
- NGINX open source only. NGINX Plus and products that bundle NGINX: check your vendor's advisory.
- A simple text scan: it can miss `http2` set in unusual ways. Treat "LOW" as "look again", not "safe forever".
- Not a replacement for patching. Upgrade first.

Defensive education only. Test only systems you own or have permission to check.
