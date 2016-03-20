# comment
import requests


class APIHandler:
    def __init__(self, url):
        req = requests.get(url)
        print("Status: " + str(req.status_code))
        data = req.json()
        print(data)
        print(data["date"])
        for k in data:
            strK = str(k)
            print(str(k) + ": " + data[strK])


#apihandler = APIHandler("http://ip.jsontest.com/")
apihandler = APIHandler("http://date.jsontest.com/")
