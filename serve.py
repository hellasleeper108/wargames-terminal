#!/usr/bin/env python3
"""Simple HTTP server to serve the WOPR Terminal locally."""
import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)

handler = http.server.SimpleHTTPRequestHandler

print(f"\033[32m")
print(f"  ╔══════════════════════════════════════╗")
print(f"  ║   WOPR TERMINAL — SERVER STARTED     ║")
print(f"  ║                                      ║")
print(f"  ║   Serving at:                        ║")
print(f"  ║   http://localhost:{PORT}                ║")
print(f"  ║                                      ║")
print(f"  ║   Press Ctrl+C to disconnect          ║")
print(f"  ╚══════════════════════════════════════╝")
print(f"\033[0m")

with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
