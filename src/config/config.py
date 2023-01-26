from dataclasses import dataclass

@dataclass
class conf:
    total_amount_of_seats: int = 40
    database: str = './data/database.db'
    token: str = ''
    paytoken: str = ''
    admin_id_1: int = 0

    redhost: str = 'localhost'
    redport: int = 6379
    redcharset: str = 'utf-8'
    reddb1: int = 0
    reddb2: int = 1