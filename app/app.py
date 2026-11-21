import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

APP_VERSION = os.getenv("APP_VERSION", "v1")


class AppHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps({"status": "healthy"}).encode()
            )

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            html = f"""
            <html>
              <head><title>GitOps Demo</title></head>
              <body>
                <h1>GitOps Continuous Deployment Platform</h1>
                <h2>Application Version: {APP_VERSION}</h2>
                <p>Deployed and managed by Argo CD.</p>
              </body>
            </html>
            """
            self.wfile.write(html.encode())

        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 8080), AppHandler)
print(f"GitOps Demo running: {APP_VERSION}")
server.serve_forever()
