import time
import os
import telebot
import schedule
import multiprocessing as mp
from chatbot import chatbot
from bot import callbacks
from sql import sql_requests
from yadisk_getter import yadisk_getter
from vkontakte import vk_getter
from sql import mark_words

saved_id = 3177

admin_id = int(os.environ["ADMIN_ID"])
admin_ids = list(map(int, os.environ["ADMIN_IDS"].split()))
token = os.environ["TG_TOKEN"]


bot = telebot.TeleBot(token)

def scheduled_update():
    global saved_id
    try:
        if vk_getter.check_last_not_pinned() != saved_id:
            users = sql_requests.users_list()
            for id, notif in users.items():
                try:
                    if notif:
                        list_of_photos, text = vk_getter.get_last_not_pinned()
                        bot.send_media_group(id, list_of_photos)
                        bot.send_message(id, text)
                except Exception as e:
                    bot.send_message(admin_id, str(e))
            saved_id = vk_getter.check_last_not_pinned()
    except Exception as e:
        bot.send_message(admin_id, str(e))

def run_scheduler():
    schedule.every(30).minutes.do(scheduled_update)
    while True:
        schedule.run_pending()
        time.sleep(1)

def starter():
    @bot.message_handler(commands=['start'])
    def start_message(message):
        callbacks.start_message(bot, message)
        try:
            sql_requests.check_user(message)
        except Exception as e:
            bot.send_message(admin_id, str(e))

    @bot.message_handler(commands=['help'])
    def start_message(message):
        callbacks.help_message(bot, message)

    @bot.message_handler(commands=['about'])
    def start_message(message):
        callbacks.about_message(bot, message)

    @bot.message_handler(content_types=['photo', 'audio', 'sticker', 'video'])
    def send_chatbot_photo(message):
        message_id = message.chat.id
        bot.send_message(message_id, "К сожалению, я пока не могу работать с такими форматами сообщений)")

    @bot.message_handler(content_types=['text'])
    def ultimate(message):
        user_message = message.text.lower()
        message_id = message.chat.id
        if message.text == "🏠Домой🏠":
            callbacks.home_page(bot, message)
        elif message.text == "📖Учебники📖":
            bot.send_message(message_id, yadisk_getter.get_all_books())
        elif message.text == "🎭Мероприятия🎭":
            if message.from_user.id in admin_ids:
                bot.send_message(message_id, sql_requests.get_all_events())
                callbacks.events_admin(bot, message)
            else:
                text = mark_words.get_5_nearest()
                bot.send_message(message_id, text)
        elif message.text == "✅Вы получаете рассылки✅" or message.text == "❌Вы не получаете рассылки❌":
            sql_requests.change_notif(message_id)
            callbacks.change_notif(bot, message)
        elif message.text == "❌Удалить мероприятие❌":
            msg = bot.send_message(message_id, "Введи дату в формате ГГГГ-ММ-ДД")
            bot.register_next_step_handler(msg, deleting_sql)
        elif message.text == "🟡Изменить мероприятие🟡":
            msg = bot.send_message(message_id, "Пример сообщения для изменения мероприятия:\nГГГГ-ММ-ДД\n(Новое описание мероприятия)")
            bot.register_next_step_handler(msg, updating_sql)

        elif "10" in user_message and "информатик" in user_message:
            bot.send_message(message_id, yadisk_getter.info_10())
        elif "11" in user_message and "информатик" in user_message:
            bot.send_message(message_id, yadisk_getter.info_11())
        elif "10" in user_message and "английск" in user_message:
            bot.send_message(message_id, yadisk_getter.english_10())
        elif "11" in user_message and "английск" in user_message:
            bot.send_message(message_id, yadisk_getter.english_11())
        elif "10" in user_message and "физик" in user_message:
            bot.send_message(message_id, yadisk_getter.physics_10())
        elif "11" in user_message and "физик" in user_message:
            bot.send_message(message_id, yadisk_getter.physics_11())
        elif "10" in user_message and "хими" in user_message:
            bot.send_message(message_id, yadisk_getter.chemistry_10())
        elif "11" in user_message and "хими" in user_message:
            bot.send_message(message_id, yadisk_getter.chemistry_11())
        elif "10" in user_message and ("обществознан" in user_message or "обществ" in user_message):
            bot.send_message(message_id, yadisk_getter.social_10())
        elif "11" in user_message and ("обществознан" in user_message or "обществ" in user_message):
            bot.send_message(message_id, yadisk_getter.social_11())

        elif "алгебр" in user_message:
            bot.send_message(message_id, yadisk_getter.algebra())
        elif "географ" in user_message:
            bot.send_message(message_id, yadisk_getter.geog())
        elif "биолог" in user_message:
            bot.send_message(message_id, yadisk_getter.biology())
        elif "геометр" in user_message:
            bot.send_message(message_id, yadisk_getter.geom())
        elif "русск" in user_message:
            bot.send_message(message_id, yadisk_getter.russian())

        elif "расписан" in user_message:
            callbacks.timetable(bot, message)

        elif "поступление" in user_message or "поступать" in user_message or "поступить" in user_message:
            callbacks.universities(bot, message)

        elif "последн" in user_message and "новост" in user_message:
            try:
                list_of_photos, text = vk_getter.get_last_not_pinned()
                bot.send_media_group(message_id, list_of_photos)
                bot.send_message(message_id, text)
            except Exception as e:
                bot.send_message(admin_id, "error")
                bot.send_message(admin_id, str(e))

        elif "сайт" in user_message and "лице" in user_message:
            callbacks.website(bot, message)

        elif "вк" in user_message and "групп" in user_message:
            callbacks.vkgroup(bot, message)

        elif ("дз" in user_message or "домашк" in user_message or
              ("домашн" in user_message and "работ" in user_message)
              or ("сетев" in user_message and "город" in user_message)
              or "сетевой" in user_message):
            callbacks.cit(bot, message)

        elif "покажи всех" in user_message:
            try:
                if message.from_user.id in admin_ids:
                    bot.send_message(message_id, sql_requests.get_all_users())
                else:
                    bot.send_message(message_id, "Чта?")
            except Exception as e:
                bot.send_message(admin_id, str(e))

        elif message.text == "покажи все мероприятия":
            if message.from_user.id in admin_ids:
                bot.send_message(message_id, sql_requests.get_all_events_admin())
            else:
                bot.send_message(message_id, "Чта?")

        elif "обнови новости" in user_message:
            if message.from_user.id in admin_ids:
                scheduled_update()
            else:
                bot.send_message(message_id, "Чта?")

        elif "сегодн" in user_message and ("событ" in user_message or "мероприят" in user_message):
            text = mark_words.get_today()
            bot.send_message(message_id, text)

        elif "завтр" in user_message and ("событ" in user_message or "мероприят" in user_message):
            text = mark_words.get_tomorrow()
            bot.send_message(message_id, text)

        elif "послезавтр" in user_message and ("событ" in user_message or "мероприят" in user_message):
            text = mark_words.get_after_tomorrow()
            bot.send_message(message_id, text)

        elif "недел" in user_message and ("эту" in user_message or "этой" in user_message) and (
                "событ" in user_message or "мероприят" in user_message):
            text = mark_words.during_the_week()
            bot.send_message(message_id, text)

        elif "недел" in user_message and "следующ" in user_message and (
                "событ" in user_message or "мероприят" in user_message):
            text = mark_words.during_the_next_week()
            bot.send_message(message_id, text)

        elif "месяц" in user_message and ("этом" in user_message or "этого" in user_message) and (
                "событ" in user_message or "мероприят" in user_message):
            text = mark_words.during_the_month()
            bot.send_message(message_id, text)

        elif "месяц" in user_message and "следующ" in user_message and (
                "событ" in user_message or "мероприят" in user_message):
            text = mark_words.during_the_next_month()
            bot.send_message(message_id, text)

        elif "год" in user_message and ("этом" in user_message or "этого" in user_message) and (
                "событ" in user_message or "мероприят" in user_message):
            text = mark_words.during_the_year()
            bot.send_message(message_id, text)

        else:
            msg = bot.send_message(message_id, "Запрос отправлен в нейросеть")
            bot.delete_message(msg.chat.id, msg.message_id)
            bot.send_message(message_id, chatbot.question(message))

    def deleting_sql(message):
        message_id = message.chat.id
        try:
            bot.send_message(message_id, sql_requests.delete_event(message))
        except Exception as e:
            bot.send_message(admin_id, str(e))

    def updating_sql(message):
        message_id = message.chat.id
        try:
            date = message.text[0:10:]
            event = message.text[11::]
            bot.send_message(message_id, sql_requests.update_event(date, event))
        except Exception as e:
            bot.send_message(admin_id, str(e))

    process = mp.Process(target=run_scheduler)
    process.start()
    bot.polling(non_stop=True)
    process.join()