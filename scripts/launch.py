#!/usr/bin/env python3
"""
IPLS Website Local Launcher
Serves the complete IPLS website (HTML, CSS, JS, mockups, images) and opens it in your default browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

PORT = 8080
# Website root directory (parent folder of scripts/)
DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    if not os.path.exists(DIRECTORY):
        print(f"Error: Directory {DIRECTORY} not found.", file=sys.stderr)
        sys.exit(1)
        
    os.chdir(DIRECTORY)
    
    # Allow port reuse immediately
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print("=" * 60)
        print(f"IPLS Website is running at: {url}")
        print(f"Home Page:         http://localhost:{PORT}/index.html")
        print(f"Merchandise Store: http://localhost:{PORT}/merchandise.html")
        print(f"Moot Court:        http://localhost:{PORT}/moot-court.html")
        print(f"IPSEL Certificate: http://localhost:{PORT}/ipsel.html")
        print(f"Constitution:      http://localhost:{PORT}/constitution.html")
        print(f"Documents:         http://localhost:{PORT}/documents.html")
        print(f"Schedule:          http://localhost:{PORT}/schedule.html")
        print("=" * 60)
        print("Press Ctrl+C to stop the server.")
        
        # Open default browser
        threading.Thread(target=lambda: (time.sleep(0.5), webbrowser.open(url)), daemon=True).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()
