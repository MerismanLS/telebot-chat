from sql import sql_scripts, mark_words
import psycopg2
import pendulum
import os

user_name = os.environ["USER_NAME"]
password = os.environ["PASSWORD"]
dbname = os.environ["DBNAME"]
port = os.environ["PORT"]
host = os.environ["HOST"]

def get_con():
    con = psycopg2.connect(dbname=dbname, user=user_name,
                           password=password, host=host, port=port)
    cur = con.cursor()
    return con, cur

def update():
    con, cur = get_con()
    cur.execute("DROP TABLE Users")
    cur.execute("CREATE TABLE Users (id_tg BIGINT, nickname TEXT, notif BOOLEAN DEFAULT true)")
    print("success")
    con.commit()
    con.close()

def check_user(message):
    con, cur = get_con()
    id_tg = message.chat.id
    username = message.from_user.username
    cur.execute(sql_scripts.check_user, (id_tg, ))
    result = cur.fetchall()
    if len(result) == 0:
        if username is None:
            username = "None"
        cur.execute(sql_scripts.add_user, (id_tg, username))
        con.commit()
    con.close()

def get_all_events():
    cur_week = mark_words.during_the_week()
    next_week = mark_words.during_the_next_week()
    res = f"Мероприятия на эту неделю:\n\n{cur_week}\n\n\nМероприятия на следующую неделю:\n\n{next_week}"
    return res

def get_all_events_admin():
    con, cur = get_con()
    cur.execute(sql_scripts.get_all_events)
    events = cur.fetchall()
    res = ''
    for elem in events:
        res = res + str(elem[0]) + '\n\n'
        res = res + elem[1] + '\n\n'
        res = res + elem[2] + '\n\n\n'
    con.close()
    return res

def events_list():
    con, cur = get_con()
    cur.execute(sql_scripts.get_all_events)
    events = cur.fetchall()
    l = []
    for values in events:
        date = pendulum.from_format(str(values[0]), 'YYYY-MM-DD')
        date.add(hours=23, minutes=58)
        l.append([date, values[1], values[2]])
    con.close()
    return l

def get_all_users():
    con, cur = get_con()
    cur.execute(sql_scripts.get_all_users)
    users = cur.fetchall()
    res = ''
    for elem in users:
        res = res + str(elem[0]) + ' | '
        res = res + str(elem[1]) + ' | '
        res = res + str(elem[2]) + ' | '
        res = res + str(elem[3]) + '\n\n'
    con.close()
    return res

def users_list():
    con, cur = get_con()
    cur.execute(sql_scripts.get_all_users)
    users = cur.fetchall()
    l = {}
    for elem in users:
        l[elem[0]] = elem[2]
    con.close()
    return l

def delete_event(message):
    con, cur = get_con()
    answer = ""
    try:
        events = events_list()
        date = pendulum.from_format(message.text, 'YYYY-MM-DD')
        date = date.to_date_string()
        for elem in events:
            if date == elem[0].to_date_string():
                cur.execute(sql_scripts.delete_event, (date, ))
                answer = "Успешно удалено!"
                con.commit()
                break
    except Exception as e:
        answer = "еррор 404"
    con.close()
    return answer

def delete_events_by_date(message):
    con, cur = get_con()
    answer = ""
    try:
        date = pendulum.from_format(message.text, 'YYYY-MM-DD')
        date = date.to_date_string()
        cur.execute(sql_scripts.delete_events_by_date, (date, ))
        answer = "Успешно удалено!"
        con.commit()
    except Exception as e:
        answer = "еррор 404"
    con.close()
    return answer

def update_event(date_from, event):
    con, cur = get_con()
    answer = ""
    try:
        events = events_list()
        date = pendulum.from_format(date_from, 'YYYY-MM-DD')
        date = date.to_date_string()
        for elem in events:
            if date == elem[0].to_date_string():
                cur.execute(sql_scripts.update_event, (event, date))
                answer = "Успешно изменено"
                con.commit()
                break
    except Exception as e:
        answer = "еррор 404"
    con.close()
    return answer

def notif_checker(id_tg):
    con, cur = get_con()
    cur.execute(sql_scripts.check_notification, (id_tg, ))
    answer = cur.fetchone()
    con.close()
    return answer[0]

def change_notif(id_tg):
    con, cur = get_con()
    current = notif_checker(id_tg)
    cur.execute(sql_scripts.change_notif, (not current, id_tg))
    con.commit()
    con.close()

def admin_checker(id_tg):
    con, cur = get_con()
    cur.execute(sql_scripts.check_admin, (id_tg, ))
    answer = cur.fetchone()
    con.close()
    return answer[0]

def change_admin(id_tg):
    con, cur = get_con()
    current = admin_checker(id_tg)
    cur.execute(sql_scripts.change_admin, (not current, id_tg))
    con.commit()
    con.close()
