import requests
# from http.server import HTTPServer
# from http.server import BaseHTTPRequestHandler
from xml.etree import ElementTree
import tkinter as tk
import sys
import re
from pathlib import Path
from time import localtime
import socket


class JSONAPIHandler:
    def __init__(self, url):
        try:
            req = requests.get(url)
            print("Status: " + str(req.status_code))
            data = req.json()
            for k, v in data.items():
                print(str(k) + ": " + str(v))
        except:
            print("Unexpected error:", sys.exc_info()[0])


# apihandler = APIHandler("http://ip.jsontest.com/")
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


# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()

# name = input('What is your name?\n')
# print('Hi, %s.' % name)

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# p = Path('/')
# for x in p.iterdir():
#     if x.is_dir():
#         print(x)

print(localtime())

try:
    ip = socket.gethostbyname("www.google.ch")
    sock = socket.socket()
    ip_port = (ip, 80)
    print("IP: " + str(ip_port[0]), "Port: " + str(ip_port[1]))
    result = sock.connect_ex(ip_port)
    print("Result: ", str(result))
    sock.close()
except:
    print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
