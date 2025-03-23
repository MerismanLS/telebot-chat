import psycopg2

user_name = "Merisman"
password = "PoPoLiLi0909"
dbname = "telebot_db"
port = 5432
host = "telebot-merisman.db-msk0.amvera.tech"

def get_con():
    con = psycopg2.connect(dbname=dbname, user=user_name,
                           password=password, host=host, port=port)
    cur = con.cursor()
    return con, cur

def update_table():
    con, cur = get_con()
    cur.execute("UPDATE Users SET is_admin = TRUE WHERE id_tg = 1076372910")
    con.commit()
    con.close()
    print("finished")

update_table()