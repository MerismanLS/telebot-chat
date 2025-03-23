import psycopg2

def get_con():
    con = psycopg2.connect(dbname="telebot_db", user="Merisman",
                           password="PoPoLiLi0909", host="telebot-merisman.db-msk0.amvera.tech", port=5432)
    cur = con.cursor()
    return con, cur

con, cur = get_con()
cur.execute("DROP TABLE Users")
cur.execute("DROP TABLE Events")

cur.execute(
    "CREATE TABLE Users (id_tg BIGINT, nickname TEXT, notif BOOLEAN DEFAULT true, is_admin BOOLEAN DEFAULT true)")
print("users created")
cur.execute(
    "CREATE TABLE Events (date DATE, description TEXT, name TEXT)")
print("events created")
con.commit()
con.close()