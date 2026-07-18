import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = r"C:\Users\internship\OneDrive\Desktop\Ghee\twobrothers-reference"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

os.chdir(DIRECTORY)
print(f"Starting local server at http://localhost:{PORT}")
print(f"Serving files from: {DIRECTORY}")
print("Press Ctrl+C to stop")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
