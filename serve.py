#!/usr/bin/env python3
"""Tiny durable static server for random.0xbeckett.me (port 8742)."""
import http.server, socketserver, os

PORT = 8742
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        super().end_headers()
    def log_message(self, *a):
        pass

class S(socketserver.ThreadingTCPServer):
    allow_reuse_address = True

with S(("127.0.0.1", PORT), H) as httpd:
    httpd.serve_forever()
