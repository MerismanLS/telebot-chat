import requests
import json

with open("./config.json") as a:
    config = json.load(a)

url = f'https://api.telegram.org/bot{config[0]['config']}/deleteWebhook'
response = requests.get(url)
print(response.json())