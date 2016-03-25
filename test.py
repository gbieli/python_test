import requests
# from http.server import HTTPServer
# from http.server import BaseHTTPRequestHandler
from xml.etree import ElementTree
import tkinter as tk

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
            print("Tag: " + child.tag, "\n  Text: " + child.text)

xmlapihandler = XMLAPIHandler("http://www.w3schools.com/xml/note.xml")

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()