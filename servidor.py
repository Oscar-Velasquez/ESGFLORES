from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys
from string import Template
import pyodbc


port = 3008

class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        lenc = int(self.headers["Content-Length"])
        data = self.rfile.read(lenc)
        data = data.decode()
        data = float(parse.unquote(data))

    

        self.send_response(200)
        self.end_headers()
        self.wfile.write( str(data).encode() )

print("Servidor corriendo en el pueto", port)
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()




