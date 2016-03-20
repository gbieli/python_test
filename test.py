# comment
import requests
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler


class APIHandler:
    def __init__(self, url):
        req = requests.get(url)
        print("Status: " + str(req.status_code))
        data = req.json()
        for k, v in data.items():
            print(str(k) + ": " + str(v))

#apihandler = APIHandler("http://ip.jsontest.com/")
apihandler = APIHandler("http://date.jsontest.com/")

class HTTPServer:
    def __init__(self):
        self.run()

    def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()

server = HTTPServer()