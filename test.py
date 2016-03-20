# comment
import requests


class APIHandler:
    def __init__(self, url):
        req = requests.get(url)
        print("Status: " + str(req.status_code))
        data = req.json()
        for k, v in data.items():
            print(str(k) + ": " + str(v))

#apihandler = APIHandler("http://ip.jsontest.com/")
apihandler = APIHandler("http://date.jsontest.com/")
