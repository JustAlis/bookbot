import sqlite3
import string
from random import choices

class database:

    def __init__(self, db):
        self.connect = sqlite3.connect(db)
        self.coursor = self.connect.cursor()
    
    async def get_payment_method(self, id):
        with self.connect:
            c = self.coursor
            query = """SELECT paid FROM guests WHERE person_id = ?"""
            params = (id,)
            c.execute(query, params)
            paid = c.fetchone()
        return paid[0]

    #add id into all table to send promo
    async def add_user(self, id):
        with self.connect:
            c = self.coursor
            query = """INSERT INTO all_users (id) VALUES (?)"""
            params = (id,)
            c.execute(query, params)

    #get reserved seats
    async def get_reserved(self):
        with self.connect:
            c = self.coursor
            c.execute('SELECT amount FROM guests')
            seats = c.fetchall()

            reserved = 0
            for i in range(len(seats)):
                try:
                    reserved = reserved + seats[i][0]
                except:
                    continue
        return reserved

    #check if the person is in db
    async def check_person(self, id):
        with self.connect:
            c = self.coursor
            query = """SELECT person_id FROM guests WHERE person_id = ?"""
            params = (id,)
            c.execute(query, params)
            person = c.fetchone()
        return person

    #chek if this persion sent amount of guests
    async def check_amount(self, id):
        with self.connect:
            c = self.coursor
            query = """SELECT amount FROM guests WHERE person_id = ?"""
            params = (id,)
            c.execute(query, params)
            amount = c.fetchone()
        return amount[0]

    #add new person to db
    async def add_person(self, id):
        with self.connect:
            c = self.coursor
            query = """INSERT INTO guests (person_id) VALUES (?)"""
            params = (id,)
            c.execute(query, params)

    #check if there is a token
    async def check_token(self, id):
        with self.connect:
            c = self.coursor
            query = """SELECT token FROM guests WHERE person_id = ?"""
            params = (id,)
            c.execute(query, params)
            token_tmp = c.fetchone() 
        return token_tmp[0]

    #change amount of guests in the db
    async def change_amount(self, text, id):
        with self.connect:
            c = self.coursor
            query = """UPDATE guests SET (amount) = (?) WHERE person_id = ?"""
            params = (text,id)
            c.execute(query, params)

    #generate token and add amount of guests and token to db
    async def add_token_amount_get_token(self, text, id):
        with self.connect:
            c = self.coursor
            token = 'f'
            while True:
                token = (''.join(choices(string.ascii_letters + string.digits, k=16)))
                #check if this token is in the db
                query = """SELECT token FROM guests WHERE token = ?"""
                params = (token,)
                c.execute(query, params)
                copy = c.fetchone()
                self.connect.commit()
                if copy is None:
                    break
            #add amount of guests and token to db
            query = """UPDATE guests SET (amount,token) = (?,?) WHERE person_id = ?"""
            params = (text, token, id)
            c.execute(query, params)
        return token
    
    #cancel book
    async def cancel_book(self, id):
        with self.connect:
            c = self.coursor
            query = """DELETE FROM guests WHERE person_id = ?"""
            params = (id,)
            c.execute(query, params)

    #admin get info
    async def get_not_paid(self):
        with self.connect:
            c = self.coursor
            c.execute('SELECT COUNT(person_id) FROM guests WHERE amount IS NOT NULL')
            ids = c.fetchone()
        return ids[0]
    
    #admin get info
    async def get_paid(self):
        with self.connect:
            c = self.coursor
            c.execute('SELECT amount FROM guests WHERE paid = 1')
            tmp = c.fetchall()

            paid = 0
            for bought in tmp:
                paid = paid + bought[0]
        return paid
    
    #admin reset table
    async def clear_table(self):
        with self.connect:
            c = self.coursor
            c.execute('DELETE FROM guests')

    #admin get ids from all table to send promo
    async def get_users(self):
        with self.connect:
            c = self.coursor
            c.execute('SELECT id FROM all_users')
            all_users = c.fetchall()

            users = []
            for user in all_users:
                users.append(user[0])
        return users
