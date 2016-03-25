# comment
import requests
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from xml.etree import ElementTree

class JSONAPIHandler:
    def __init__(self, url):
        req = requests.get(url)
        print("Status: " + str(req.status_code))
        data = req.json()
        for k, v in data.items():
            print(str(k) + ": " + str(v))

#apihandler = APIHandler("http://ip.jsontest.com/")
apihandler = JSONAPIHandler("http://date.jsontest.com/")

# class HTTPServer:
#     def __init__(self):
#         self.run()
#
#     def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
#         server_address = ('', 8000)
#         httpd = server_class(server_address, handler_class)
#         httpd.serve_forever()
#
# server = HTTPServer()

class XMLAPIHandler:
    def __init__(self, url):
        req = requests.get(url)
        root = ElementTree.fromstring(req.content)
        for child in root:
            print(child.tag, child.text)

xmlapihandler = XMLAPIHandler("http://www.w3schools.com/xml/note.xml")