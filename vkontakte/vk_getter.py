import requests
import os
from telebot.types import InputMediaPhoto as imp

token = os.environ["VK_TOKEN"]
param = {'access_token': token, 'owner_id': 187548314_457250348, 'domain': 'litsey101', 'count': 2, 'v': 5.199}
method = 'wall.get'

def get_last_not_pinned():
    rec = requests.get(url=f'https://api.vk.com/method/{method}', params=param)
    list_of_photos = []
    text = ""
    try:
        if rec.json()["response"]["items"][0]["is_pinned"] == 1:
            text = rec.json()["response"]["items"][1]["text"] + f"\n\nhttps://vk.com/wall-187548314_{rec.json()["response"]["items"][1]["id"]}"
            for i in range(len(rec.json()["response"]["items"][1]["attachments"])):
                if rec.json()["response"]["items"][1]["attachments"][i]["type"] == "video":
                    list_of_photos.append(imp(rec.json()["response"]["items"][1]["attachments"][i]["video"]["image"][-1]["url"]))
                else:
                    list_of_photos.append(imp(rec.json()["response"]["items"][1]["attachments"][i]["photo"]["orig_photo"]["url"]))
    except:
        text = rec.json()["response"]["items"][0]["text"]  + f"\n\nhttps://vk.com/wall-187548314_{rec.json()["response"]["items"][0]["id"]}"
        for i in range(len(rec.json()["response"]["items"][0]["attachments"])):
            if rec.json()["response"]["items"][0]["attachments"][i]["type"] == "video":
                list_of_photos.append(imp(rec.json()["response"]["items"][0]["attachments"][i]["video"]["image"][-1]["url"]))
            else:
                list_of_photos.append(imp(rec.json()["response"]["items"][0]["attachments"][i]["photo"]["orig_photo"]["url"]))
    return list_of_photos, text


def check_last_not_pinned():
    rec = requests.get(url=f'https://api.vk.com/method/{method}', params=param)
    try:
        if rec.json()["response"]["items"][0]["is_pinned"] == 1:
            return rec.json()["response"]["items"][1]["id"]
    except:
        return rec.json()["response"]["items"][0]["id"]