get_all_events = 'SELECT * FROM Events ORDER BY date'
delete_event = 'DELETE FROM Events WHERE date = %s'
update_event = 'UPDATE Events SET description = %s WHERE date = %s'
delete_events_by_date = 'DELETE FROM Events WHERE date <= %s'

get_all_users = 'SELECT * FROM Users'
check_user = 'SELECT id_tg FROM Users WHERE id_tg = %s'
add_user = 'INSERT INTO Users (id_tg, nickname) VALUES (%s, %s)'

check_notification = 'SELECT notif FROM Users WHERE id_tg = %s'
change_notif = 'UPDATE Users SET notif = %s WHERE id_tg = %s'

check_admin = 'SELECT is_admin FROM Users WHERE id_tg = %s'
change_admin = 'UPDATE Users SET is_admin = %s WHERE id_tg = %s'

structure_of_users_db = """
id_tg BIGINT,
nickname TEXT,
notif BOOLEAN,
is_admin BOOLEAN
"""

structure_of_events_db = """
date DATE,
description TEXT,
name TEXT
"""
