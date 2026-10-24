#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT = 8080
DIST_DIR = r"C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app\dist"

class RabbitHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST_DIR, **kwargs)

    def translate_path(self, path):
        if path.startswith('/Rabbit./'):
            path = '/' + path[len('/Rabbit./'):]
        elif path.startswith('/Rabbit/'):
            path = '/' + path[len('/Rabbit/'):]
        return super().translate_path(path)

    def end_headers(self):
        # Disable caching for testing
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(DIST_DIR)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), RabbitHandler) as httpd:
        print(f"RABBIT Dist Server running at http://localhost:{PORT}/Rabbit./")
        sys.stdout.flush()
        httpd.serve_forever()
