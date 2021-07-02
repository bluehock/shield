# coding=utf-8
import requests
import json
import time
import socket
import base64
import socks

base_url = "http://127.0.0.1:18080"
# proxies = {"http": "127.0.0.1:8888", "https": "127.0.0.1:8888"}
proxies = None


class XhsSocketClient:
    def __init__(self):
        self.client = None

    def connect(self):
        if self.client is not None:
            return
        HOST = 'apppush.xiaohongshu.com'
        PORT = 5333
        socket.socket = socks.socksocket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

    def send(self, based64ed):
        if self.client is None:
            self.connect()
        content = base64.b64decode(based64ed)
        user_input = content
        print content
        print "================= sent =========================="
        self.client.sendall(user_input)

    def close(self):
        if self.client is not None:
            self.client.close()
        print "================= close =========================="

    def __del__(self):
        self.close()


def test():
    url = base_url + "/s/login"
    params = {
        "uid": "60ddb0d10000000001015f01",
        "sid": "session.1594515706332388740313",
        "deviceId": "353CE2F-0131-474E-A093-DF39D12E4515",
        "fingerprint": "202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883",

    }
    text = requests.get(url, params=params, proxies=proxies).json()

    print json.dumps(text, ensure_ascii=False)

    client = XhsSocketClient()
    client.connect()
    client.send(text.get("data").get("body"))

    url = base_url + "/s/send"
    params = {
        "receiver": "9f775f5f3cf7000000000100",
        "sender": "60ddb0d10000000001015f01",
        "content": "hi",
    }

    text = requests.get(url, params=params, proxies=proxies).json()
    client.send(text.get("data").get("body"))

    print json.dumps(text, ensure_ascii=False)


if __name__ == '__main__':
    test()
