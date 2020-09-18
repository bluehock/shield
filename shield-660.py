# coding=utf-8
import requests
import json

ENCRYPT_HOST = "http://127.0.0.1"
ENCRYPT_URL = ENCRYPT_HOST + "/660"

# proxies = {"http": "127.0.0.1:8888", "https": "127.0.0.1:8888"}
proxies = None

USER_AGENT = "Dalvik/2.1.0 (Linux; U; Android 5.0.2; Samsung Note3 Build/LMY47X) Resolution/1080*1920 Version/6.60.0 Build/6600125 Device/(samsung;Samsung Note3)"

xy_common_params = "platform=android&deviceId=353CE2F-0131-474E-A093-DF39D12E4515&version=6.60&build=6600125&t=1592222248&identifier_flag=1&fid=1595172589-0-0-2de0b0d2666328142e712e63c19fad35&device_fingerprint=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&sid=session.1593665994331207470119"
xy_platform_info = "platform=android&version=6.60&build=6600125&deviceId=353CE2F-0131-474E-A093-DF39D12E4515&bundle=com.xingin.discover"


def get_ter_str():
    url = "https://www.xiaohongshu.com/api/sns/v3/user/me?deviceId=353CE2F-0131-474E-A093-DF39D12E4515&device_fingerprint=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&device_fingerprint1=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&fid=1595172589-0-0-2de0b0d2666328142e712e63c19fad35&lang=zh&platform=android&sid=session.1593665994331207470119&t=1592222248"
    header = {
        "User-Agent": USER_AGENT,
        "xy-common-params": "platform=android&deviceId=353CE2F-0131-474E-A093-DF39D12E4515&version=6.60&build=6600125&t=1592222248&identifier_flag=1&fid=1595172589-0-0-2de0b0d2666328142e712e63c19fad35&device_fingerprint=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&sid=session.1593665994331207470119",
        "xy-platform-info": "platform=android&version=6.60&build=6600125&deviceId=353CE2F-0131-474E-A093-DF39D12E4515&bundle=com.xingin.discover",
        "shield": ""
    }

    response = requests.get(url, headers=header, proxies=proxies, verify=False)

    xy_ter_str = response.headers["xy-ter-str"]
    return xy_ter_str
    # ret = res.json()
    # print json.dumps(ret, ensure_ascii=False)


def test_get(xy_ter_str):
    url = "https://www.xiaohongshu.com/api/sns/v3/user/me?deviceId=353CE2F-0131-474E-A093-DF39D12E4515&device_fingerprint=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&device_fingerprint1=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&fid=1595172589-0-0-2de0b0d2666328142e712e63c19fad35&lang=zh&platform=android&sid=session.1593665994331207470119&t=1592222248"
    data = {
        "url": url,
        "xy-common-params": xy_common_params,
        "xy-platform-info": xy_platform_info,
        "xy-ter-str": xy_ter_str,
        "body": ""  # GET 请求不需要 body 参数
    }

    ret = requests.post(ENCRYPT_URL, data=data, proxies=proxies).json()
    if ret["code"] == 1000:
        header = {
            "User-Agent": USER_AGENT,
            "xy-common-params": xy_common_params,
            "xy-platform-info": xy_platform_info,
            "shield": ret["data"]["shield"]
        }
        ret = requests.get(url, headers=header, proxies=proxies, verify=False).json()
        print json.dumps(ret, ensure_ascii=False)
    else:
        print json.dumps(ret, ensure_ascii=False)


def test_post(xy_ter_str):
    url = "https://www.xiaohongshu.com/api/sns/v4/user/login/password"
    body = "password=14f6099edf2cc94cb206710c716260ec&deviceId=353CE2F-0131-474E-A093-DF39D12E4515&device_fingerprint=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&device_fingerprint1=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&fid=1595172589-0-0-2de0b0d2666328142e712e63c19fad35&lang=zh&note_id=5ee369b4000000000100772a&platform=android&sid=session.1593665994331207470119&t=1592224068"

    data = {
        "url": url,
        "xy-common-params": xy_common_params,
        "xy-platform-info": xy_platform_info,
        "xy-ter-str": xy_ter_str,
        "body": body  # POST 请求需要 body 参数
    }

    ret = requests.post(ENCRYPT_URL, data=data, proxies=None, verify=False).json()

    if ret["code"] == 1000:
        header = {
            "User-Agent": USER_AGENT,
            "xy-common-params": xy_common_params,
            "xy-platform-info": xy_platform_info,
            "shield": ret["data"]["shield"],
            "content-type": "application/x-www-form-urlencoded"
        }
        ret = requests.post(url, data=body, headers=header, proxies=proxies, verify=False).json()

        print json.dumps(ret, ensure_ascii=False)

    else:
        print json.dumps(ret, ensure_ascii=False)


if __name__ == '__main__':
    xy_ter_str = get_ter_str()
    test_get(xy_ter_str)
    # test_post(xy_ter_str)
    # me()
