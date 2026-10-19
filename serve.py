"""Serve the standalone page locally, including its /gamba route."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


class PageHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path.rstrip("/") == "/gamba":
            self.path = "/index.html"
        super().do_GET()

    def do_HEAD(self):
        if urlsplit(self.path).path.rstrip("/") == "/gamba":
            self.path = "/index.html"
        super().do_HEAD()


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", "5173"))
    server = ThreadingHTTPServer(
        ("127.0.0.1", port),
        partial(PageHandler, directory=str(Path(__file__).parent / "dist")),
    )
    print(f"Gamba preview: http://127.0.0.1:{port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
