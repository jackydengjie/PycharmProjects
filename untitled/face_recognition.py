# !/usr/bin/python3

#  *_* coding:utf8 *_*
# @Time :   2020/1/5 18:34
# @Author : FengLin
# @Email : damon__dong@163.com
# @File :  face_recognition.py

import requests
import json
import base64

""" 你的 APPID AK SK """
APP_ID ="21513331"
API_KEY = "L0Ee2VYzTK2TS1kCNnTTUXBw"
SECRET_KEY = "u7oLMXt0iMFQcLbAc78TdEnMg5LW8I0L"

def get_access_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'\
        .format(API_KEY, SECRET_KEY)

    response = requests.get(url)

    if response:
        access_token = response.json()["access_token"]
        return access_token

def encode_image(image):
    if isinstance(image, str):
        with open(image, "rb") as f:
            image_data = f.read()
    else:
        image_data = image

    # print(base64.b64encode(image_data).decode("utf-8"))
    return base64.b64encode(image_data).decode("utf-8")

def get_similarity(img1, img2):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

    params = {
        "access_token": get_access_token()
    }

    header = {
        "Content-Type": "application/json"
    }

    request_data = [
        {
            "image": encode_image(img1),
            "image_type": "BASE64",
            "face_type": "LIVE",
            "quality_control": "LOW",
        },
        {
            "image": encode_image(img2),
            "image_type": "BASE64",
            "face_type": "IDCARD",
            "quality_control": "LOW",
        }
    ]

    data = json.dumps(request_data)

    response = requests.post(request_url, params=params, data=data, headers=header)

    # print(response.text)
    if response and response.json()["error_msg"] == "SUCCESS":
        return response.json()["result"]["score"]


if __name__ == '__main__':
    score = get_similarity("base.png", "photo.png")
    print(score)







