HELLO GITHUB!

    This bot is my first project and I will be glad to get some comments, if something is wrong)

FAQ

So what this bot can do?

        -This bot can book seats for the show.
        -Send promo to users

Why can't this bot book exact seats?

    -It was the requeriment. My friend has a show and he asked for this, every time different small stage. There was no need to add this.

Why there is no inline keyboards?

    -I don't like them. Reply keyboard for me looks mutch better. This is just my taste.

Why did I add redis?

    -main reason to use redis is to get rid of a lot of checks for incorrect input from users. Not to allow them to send text, 
    which will fit in the handler, and to activate submenus, if their status doesnt allow that, otherwise there can be mistakes, 
    for example: person isn't in the db, but if they will press some submenu button, programm will try to get some value, according 
    to this persons ID, and it will couse error. Previous version had so many operations with the sql db, it just started to look 
    dumb and I decided to add redis to get "callback" data, which is unavailable in aiogram with inlinekeyboard.
    -I just wanted to use redis, it is pet project, and I wanteded to understand this technology better, to practice

But there are still a lot of operations in sqlite, which could be replased with redis?

    -becouse I don't have a big amount of RAM on my server. It is actually very small.

ENV

    -python 3.11
    -redis 6.0.16
    -(read requirements.txt)

NAVIGATION

    src:
        config:
            1)total amount of seats
            2)admins ids
            3)path to db
            4)config for redis
            5)bot token(CHANGE IT)
        data:
            1)pictures
            2)script creating database(run it from src/data directory)
            3)database(will be created after the script)
        handlers:
            1)admin handlers
            2)user handlers
        helpers:
            1)function to check, if message is the amount of seats
            -here you can add other functions, which don't fit in other categories if you need
        keyboards:
            1)all keyboards are here
        replies:
            1)all replies are here, including errors
        services:
            1)class database with all the functions(sqlite database)
            2)class reddb(redis database for users)
            3)class reddb_admin(redis database for admins)
        bot.py - bot itself
    readme.md(you are here)
    requirements.txt

DB schema:

        -table all_users:
        contains IDs of all users, who enteracted with this bot

        -table guests:
        contains 4 collumns for users, who booked seats:
        1)person_id
        2)amount (amount of seast)
        3)token (uniq token for every book)
        4)paid (not in use)

HOW TO RUN

    -install and run redis
    -change values in config(token, admin id, total amount of seats(if you need), you can chnge redis configuration if you want to)
    -from src/data run create.py
    -from src run bot.py

USSAGE

    ####ADMIN
    1)admin cant use handler for users
    2)admin have to set promo and time place lines(every time you restart bot). Replies can use html tags
    3)admin can get statistics
    4)admin can send promo

    ####USER
    1)user can book seats(1 - 6)
    2)user can recive promo, when admin send it
    3)user can get info about the show(host info, time_place info, and so on(check replies))

ALSO

    -you have to set you own replies and buttons in keyboards
    -You can add pictures, but you will have to change send_message in handlers
    -You can add function for admin to add/change photos in src/data/pictures directory
    -this bot suposed to be able to send payments via binance, but the person, who asked about this bot doesnt have merchant status yet. Maybe there will be an update and I will add this function, but for now bot is able to book only. You can add your payment system as well.
