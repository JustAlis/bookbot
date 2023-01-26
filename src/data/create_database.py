import sqlite3

db = sqlite3.connect('database.db')

c = db.cursor()

c.execute("""CREATE TABLE guests(
    person_id integer,
    amount integer,
    token text,
    paid integer
)""")

db.commit()

c.execute("""CREATE TABLE all_users(
    id integer UNIQUE
)""")

db.commit()

db.close()