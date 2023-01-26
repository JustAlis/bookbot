import redis
from config import conf

#parent class
class redis_parent:
    def __init__(self, db):
        self.red = redis.Redis(host=conf.redhost, port=conf.redport, charset=conf.redcharset, decode_responses=True, db=db)

    async def get_status(self, id):
        return self.red.get(id)

    async def delete_status(self, id):
        self.red.delete(id)  

#db for users
class reddb(redis_parent):

    def __init__(self):
        super().__init__(conf.reddb1)

    async def allow_nubres(self, id):
        self.red.set(id, "numbers_allowed")

    async def allow_change_numbers(self, id):
        self.red.set(id, "change_numbers_allowed")

    async def allow_change_menu(self, id):
        self.red.set(id, "change_menu_allowed")

    async def allow_accident_menu(self, id):
        self.red.set(id, "accident_menu_allowed")

#db for admins
class reddb_admin(redis_parent):
    def __init__(self):
        super().__init__(conf.reddb2)

    async def admin_change_promo(self, id):
        self.red.set(id, "change_prormo")

    async def admin_change_date_time(self, id):
        self.red.set(id, "change_date_time")
    
    async def admin_reset_status(self, id):
        self.red.set(id, "reset_table")
    
    async def admin_send_promo(self,id):
        self.red.set(id, "send_promo")

    async def clear_redis_tables(self):
        self.red.flushall()