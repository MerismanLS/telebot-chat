from gigachat import GigaChat
import os

token = os.environ["CHATBOT_TOKEN"]

giga = GigaChat(credentials=token, verify_ssl_certs=False)

def question(message):
    response = giga.chat(f"{message.text}")
    return response.choices[0].message.content