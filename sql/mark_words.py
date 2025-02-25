import pendulum
from sql import sql_requests

def get_5_nearest():
    events = sql_requests.events_list()
    current_date = pendulum.now(tz='Europe/Samara')
    counter = 0
    res = ''
    for value in events:
        if counter < 5:
            if value[0] >= current_date:
                res = res + value[0].to_date_string() + '\n\n'
                res = res + value[1] + '\n\n'
                res = res + value[2] + '\n\n\n'
    return res

def get_today():
    events = sql_requests.events_list()
    current_date = pendulum.now(tz='Europe/Samara')
    res = ''
    for value in events:
        if value[0].to_date_string() == current_date.to_date_string():
            res = res + value[0].to_date_string() + '\n\n'
            res = res + value[1] + '\n\n'
            res = res + value[2] + '\n\n\n'
    if len(res) == 0:
        res = 'На сегодня ничего не запланировано.'
    return res

def get_tomorrow():
    events = sql_requests.events_list()
    current_date = pendulum.now(tz='Europe/Samara')
    print(current_date)
    current_date = current_date.add(days=1)
    res = ''
    for value in events:
        if value[0].to_date_string() == current_date.to_date_string():
            res = res + value[0].to_date_string() + '\n\n'
            res = res + value[1] + '\n\n'
            res = res + value[2] + '\n\n\n'
    if len(res) == 0:
        res = 'На завтра ничего не запланировано.'
    return res

def get_after_tomorrow():
    events = sql_requests.events_list()
    current_date = pendulum.now(tz='Europe/Samara')
    print(current_date.day_of_week)
    current_date = current_date.add(days=2)
    res = ''
    for value in events:
        if value[0].to_date_string() == current_date.to_date_string():
            res = res + value[0].to_date_string() + '\n\n'
            res = res + value[1] + '\n\n'
            res = res + value[2] + '\n\n\n'
    if len(res) == 0:
        res = 'На послезавтра ничего не запланировано.'
    return res

def during_the_week():
    events = sql_requests.events_list()
    current_date = pendulum.now(tz='Europe/Samara')
    date_of_week_ending = current_date.add(days=6-current_date.day_of_week)
    res = ''
    for value in events:
        if current_date <= value[0] <= date_of_week_ending:
            res = res + value[0].to_date_string() + '\n\n'
            res = res + value[1] + '\n\n'
            res = res + value[2] + '\n\n\n'
    if len(res) == 0:
        res = 'На эту неделю ничего не запланировано.'
    return res

def during_the_next_week():
    events = sql_requests.events_list()
    current_date = pendulum.now(tz='Europe/Samara')
    current_date = current_date.add(days=6-current_date.day_of_week)
    date_of_week_ending = current_date.add(days=7)
    res = ''
    for value in events:
        if current_date <= value[0] <= date_of_week_ending:
            res = res + value[0].to_date_string() + '\n\n'
            res = res + value[1] + '\n\n'
            res = res + value[2] + '\n\n\n'
    if len(res) == 0:
        res = 'На следующую неделю ничего не запланировано.'
    return res

def during_the_month():
    events = sql_requests.events_list()
    current_date = pendulum.now(tz='Europe/Samara')
    date_of_month_ending = current_date.add(months=1)
    date_of_month_ending = date_of_month_ending.subtract(days=current_date.day)
    res = ''
    for value in events:
        if current_date <= value[0] <= date_of_month_ending:
            res = res + value[0].to_date_string() + '\n\n'
            res = res + value[1] + '\n\n'
            res = res + value[2] + '\n\n\n'
    if len(res) == 0:
        res = 'До конца этого месяца ничего не запланировано.'
    return res

def during_the_next_month():
    events = sql_requests.events_list()
    current_date = pendulum.now(tz='Europe/Samara')
    current_date = current_date.add(months=1)
    current_date = current_date.subtract(days=current_date.day)
    date_of_week_ending = current_date.add(months=1)
    res = ''
    for value in events:
        if current_date < value[0] < date_of_week_ending:
            res = res + value[0].to_date_string() + '\n\n'
            res = res + value[1] + '\n\n'
            res = res + value[2] + '\n\n\n'
    if len(res) == 0:
        res = 'На следующую неделю ничего не запланировано.'
    return res

def during_the_year():
    events = sql_requests.events_list()
    current_date = pendulum.now(tz='Europe/Samara')
    date_of_year_ending = current_date.add(years=1)
    date_of_year_ending = date_of_year_ending.subtract(days=current_date.day_of_year)
    res = ''
    for value in events:
        if current_date <= value[0] <= date_of_year_ending:
            res = res + value[0].to_date_string() + '\n\n'
            res = res + value[1] + '\n\n'
            res = res + value[2] + '\n\n\n'
    if len(res) == 0:
        res = 'На следующую неделю ничего не запланировано.'
    return res
