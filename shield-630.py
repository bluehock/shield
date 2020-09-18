# coding=utf-8
import requests
import json

# proxies = {"http": "127.0.0.1:8888", "https": "127.0.0.1:8888"}
proxies = None

ENCRYPT_HOST = "http://127.0.0.1"
ENCRYPT_URL = ENCRYPT_HOST + "/630"
RID_URL = ENCRYPT_HOST + "/rid"

USER_AGENT = "Dalvik/2.1.0 (Linux; U; Android 5.0.2; Samsung Note3 Build/LMY47X) Resolution/1080*1920 Version/6.30.0 Build/6300132 Device/(samsung;Samsung Note3)"


def test_get():
    xy_platform_info = "platform=android&build=6300132&deviceId=353CE2F-0131-474E-A093-DF39D12E4515"
    xy_common_params = "platform=android&deviceId=353CE2F-0131-474E-A093-DF39D12E4515&device_fingerprint=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&device_fingerprint1=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&versionName=6.30.0&channel=Store360&sid=session.1585660985001435804941&t=1592219866&uis=light&identifier_flag=2"
    data = {
        "url": "https://www.xiaohongshu.com/api/sns/v6/homefeed?deviceId=353CE2F-0131-474E-A093-DF39D12E4515&platform=android&sid=session.1593665994331207470119&oid=homefeed_recommend&device_fingerprint=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883",
        "xy-platform-info": xy_platform_info,
        "xy-common-params": xy_common_params}

    ret = requests.post(ENCRYPT_URL, data=data, proxies=proxies).json()
    if ret["code"] == 1000:
        header = {
            "User-Agent": USER_AGENT,
            "xy-platform-info": xy_platform_info,
            "xy-common-params": xy_common_params,
            "shield": ret["data"]["shield"]
        }
        url = ret["data"]["url"]
        ret = requests.get(url, headers=header, proxies=proxies, verify=False).json()
        print json.dumps(ret, ensure_ascii=False)
    else:
        print json.dumps(ret, ensure_ascii=False)


def test_post_rid(rid):
    url = "https://www.xiaohongshu.com/api/sns/v1/system_service/slide_captcha_check"
    xy_platform_info = "platform=android&build=6300132&deviceId=353CE2F-0131-474E-A093-DF39D12E4515"
    xy_common_params = "platform=android&deviceId=353CE2F-0131-474E-A093-DF39D12E4515&device_fingerprint=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&device_fingerprint1=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&versionName=6.30.0&channel=Store360&sid=session.1593665994331207470119&t=1592219866&uis=light&identifier_flag=2"

    data = {
        "url": url,
        "xy-platform-info": xy_platform_info,
        "xy-common-params": xy_common_params,
        "body": "from=native&pass=true&rid=" + rid + "&deviceId=353CE2F-0131-474E-A093-DF39D12E4515&identifier_flag=0&device_fingerprint1=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&uis=light&device_fingerprint=202006261454019d1b1a0db8172b59cbe25925c1c3900001ab4b27b14c4883&versionName=6.30.0&platform=android&sid=session.1593665994331207470119&t=1600185507&x_trace_page_current=login_full_screen_pwd_page&lang=zh-Hans&channel=BaiduPinzhuan"
    }
    ret = requests.post(ENCRYPT_URL, data=data, proxies=proxies).json()

    if ret["code"] == 1000:
        header = {
            "User-Agent": USER_AGENT,
            "xy-platform-info": xy_platform_info,
            "xy-common-params": xy_common_params,
            "shield": ret["data"]["shield"],
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 'Connection': 'close'
        }

        body = ret["data"]["body"]
        ret = requests.post(url, data=body, headers=header, proxies=proxies, verify=False).json()

        print json.dumps(ret, ensure_ascii=False)

    else:
        print json.dumps(ret, ensure_ascii=False)


def rid():
    ret = requests.get(RID_URL, proxies=proxies, verify=False).json()
    print json.dumps(ret, ensure_ascii=False)
    rid = ret["data"]["rid"]
    # test_post_encoded(rid)
    print rid
    test_post_rid(rid)


if __name__ == '__main__':
    test_get()
    rid()
    test_get()

    # test_post_encoded()
