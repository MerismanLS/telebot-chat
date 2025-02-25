from telebot import types
import json
from sql import sql_requests
import os

with open("./additional/config.json", encoding="utf-8") as a:
    config = json.load(a)
    
admin_ids = list(map(int, os.environ["ADMIN_IDS"].split()))

def start_message(bot, message):
    home_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    books = types.KeyboardButton(text="📖Учебники📖")
    events = types.KeyboardButton(text="🎭Мероприятия🎭")
    home_markup.add(books)
    home_markup.add(events)
    if sql_requests.notif_checker(message.chat.id):
        notif = types.KeyboardButton(text="✅Вы получаете рассылки✅")
        home_markup.add(notif)
    else:
        notif = types.KeyboardButton(text="❌Вы не получаете рассылки❌")
        home_markup.add(notif)
    if message.from_user.id in admin_ids:
        bot.send_message(message.chat.id,
                         text=config[0]["start_admin_message"],
                         reply_markup=home_markup)
    else:

        bot.send_message(message.chat.id,
                         text=config[0]["start_message"],
                         reply_markup=home_markup)

def change_notif(bot, message):
    home_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    books = types.KeyboardButton(text="📖Учебники📖")
    events = types.KeyboardButton(text="🎭Мероприятия🎭")
    home_markup.add(books)
    home_markup.add(events)
    if sql_requests.notif_checker(message.chat.id):
        notif = types.KeyboardButton(text="✅Вы получаете рассылки✅")
        home_markup.add(notif)
    else:
        notif = types.KeyboardButton(text="❌Вы не получаете рассылки❌")
        home_markup.add(notif)
    bot.send_message(message.chat.id, "Статус рассылки успешно изменён", reply_markup=home_markup)

def help_message(bot, message):
    bot.send_message(message.chat.id,
                        text=config[0]["help_message"])

def about_message(bot, message):
    bot.send_message(message.chat.id,
                         text=config[0]["about_message"])

def timetable(bot, message):
    inline_markup = types.InlineKeyboardMarkup()
    t_tb = types.InlineKeyboardButton(text="Расписание", url="https://raspisanie.nikasoft.ru/27701164.html")
    inline_markup.add(t_tb)
    bot.send_message(message.chat.id, "Расписание лицея", reply_markup=inline_markup)

def universities(bot, message):
    inline_markup = types.InlineKeyboardMarkup()
    t_tb = types.InlineKeyboardButton(text="Поступление", url="https://propostuplenie.ru/vuzi/")
    inline_markup.add(t_tb)
    bot.send_message(message.chat.id, "Думаю, этот сайт поможет вам с поступлением", reply_markup=inline_markup)

def website(bot, message):
    inline_markup = types.InlineKeyboardMarkup()
    t_tb = types.InlineKeyboardButton(text="Сайт", url="https://litsey101.gosuslugi.ru")
    inline_markup.add(t_tb)
    bot.send_message(message.chat.id, "Сайт лицея", reply_markup=inline_markup)

def vkgroup(bot, message):
    inline_markup = types.InlineKeyboardMarkup()
    t_tb = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/litsey101")
    inline_markup.add(t_tb)
    bot.send_message(message.chat.id, "Группа лицея во Вконтакте", reply_markup=inline_markup)

def cit(bot, message):
    inline_markup = types.InlineKeyboardMarkup()
    t_tb = types.InlineKeyboardButton(text="Сет. город", url="https://sgo.cit73.ru/")
    inline_markup.add(t_tb)
    bot.send_message(message.chat.id, "Сайт сетевого города", reply_markup=inline_markup)

def events_admin(bot, message):
    admins_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    deleting = types.KeyboardButton(text="❌Удалить мероприятие❌")
    updating = types.KeyboardButton(text="🟡Изменить мероприятие🟡")
    home = types.KeyboardButton("🏠Домой🏠")
    admins_markup.add(deleting)
    admins_markup.add(updating)
    admins_markup.add(home)
    bot.send_message(message.chat.id,
                     text="Администратор, прошу, выберите действие:",
                     reply_markup=admins_markup)

def home_page(bot, message):
    home_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    books = types.KeyboardButton(text="📖Учебники📖")
    events = types.KeyboardButton(text="🎭Мероприятия🎭")
    home_markup.add(books)
    home_markup.add(events)
    if sql_requests.notif_checker(message.chat.id):
        notif = types.KeyboardButton(text="✅Вы получаете рассылки✅")
        home_markup.add(notif)
    else:
        notif = types.KeyboardButton(text="❌Вы не получаете рассылки❌")
        home_markup.add(notif)
    bot.send_message(message.chat.id,
                         text=config[0]["home_message"],
                         reply_markup=home_markup)
