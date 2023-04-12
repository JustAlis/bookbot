from bot import bot, dp
from services import database, reddb, reddb_admin
from random import choice
from config import conf
import keyboards.reply_keyboard as keyboard
import helpers as help
import replies as rp
from aiogram import types

db = database(conf.database)
rdb = reddb()
rdba = reddb_admin()

#command start handler
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    #add new user to db
    try:
        await db.add_user(message.from_user.id)
    except:
        pass

    await bot.send_message(message.chat.id, rp.start, parse_mode='html',reply_markup=keyboard.main_menu)

#command admin handler
@dp.message_handler(lambda message: message.from_user.id == conf.admin_id_1, commands=['admin'])
async def command_admin(message: types.Message):

    await bot.send_message(message.chat.id, rp.admin_start, parse_mode='html',reply_markup=keyboard.admin_menu)

#handler for admins
@dp.message_handler(lambda message: message.from_user.id == conf.admin_id_1, content_types=types.ContentType.ANY)
async def admin_handler(message: types.Message):

    #if admin wants to send promo
    if message.text == keyboard.send_promo and rdba.get_status(message.from_user.id) is None:
        rdba.admin_send_promo(message.from_user.id)
        await bot.send_message(message.from_user.id, rp.send_promo_start, parse_mode='html', disable_web_page_preview=True)
        await bot.send_message(message.chat.id, rp.promo, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.admin_warning)

    elif rdba.get_status(message.from_user.id) == "send_promo":
        if message.text == 'Yes':
            rdba.delete_status(message.from_user.id)
            users = await db.get_users()
            for user in users:
                await bot.send_message(user, rp.promo, parse_mode='html', disable_web_page_preview=True)

            await bot.send_message(message.from_user.id, rp.send_promo_end, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.admin_menu)

        elif message.text == 'No':
            rdba.delete_status(message.from_user.id)
            await bot.send_message(message.from_user.id, rp.send_promo_denyed, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.admin_menu)
        
    #if admin wants to get stats
    elif message.text == keyboard.get_stats and await rdba.get_status(message.from_user.id) is None:
        users = len(await db.get_users())
        reserved_seats = await db.get_reserved()
        persons_who_booked = await db.get_not_paid()
        bought_tickets = await db.get_paid()
        await bot.send_message(message.chat.id, rp.stats.format(users, persons_who_booked, reserved_seats, bought_tickets), parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.admin_menu)

    #if admin wants to reset table
    elif message.text == keyboard.reset_db and rdba.get_status(message.from_user.id) is None:
        rdba.admin_reset_status(message.from_user.id)
        await bot.send_message(message.chat.id, rp.reset_warning, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.admin_warning)

    elif rdba.get_status(message.from_user.id) == 'reset_table':
        if message.text == keyboard.yes:
            rdba.clear_redis_tables()
            await db.clear_table()
            await bot.send_message(message.chat.id, rp.reset_reply, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.admin_menu)
        
        elif message.text == keyboard.no:
            rdba.delete_status(message.from_user.id)
            await bot.send_message(message.chat.id, rp.denyed_reset, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.admin_menu)

    #if admin wants to set new time and place
    elif message.text == keyboard.edit_date_place and rdba.get_status(message.from_user.id) is None:
        rdba.admin_change_date_time(message.from_user.id)
        await bot.send_message(message.chat.id, rp.time_place_edit_mode, reply_markup=keyboard.remove)
        await bot.send_message(message.chat.id, rp.time_place, disable_web_page_preview=True)

    elif rdba.get_status(message.from_user.id) == 'change_date_time':
        rp.time_place = message.text
        rdba.delete_status(message.from_user.id)
        await bot.send_message(message.chat.id, rp.time_place_edit_mode_end, disable_web_page_preview=True, reply_markup=keyboard.admin_menu)
        await bot.send_message(message.chat.id, rp.time_place, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.admin_menu)

    #if admin wants to set new promo lines
    elif message.text == keyboard.edit_promo and rdba.get_status(message.from_user.id) is None:
        rdba.admin_change_promo(message.from_user.id)
        await bot.send_message(message.chat.id, rp.promo_edit_mode, reply_markup=keyboard.remove)
        await bot.send_message(message.chat.id, rp.promo, disable_web_page_preview=True)

    elif rdba.get_status(message.from_user.id) == 'change_prormo':
        rp.promo = message.text
        rdba.delete_status(message.from_user.id)
        await bot.send_message(message.chat.id, rp.promo_edit_mode_end, disable_web_page_preview=True, reply_markup=keyboard.admin_menu)
        await bot.send_message(message.chat.id, rp.promo, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.admin_menu)

    #if admin input is incorrect:
    else:
        rdba.delete_status(message.from_user.id)
        await bot.send_message(message.chat.id, rp.admin_error, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.admin_menu)

#handler for users
@dp.message_handler(content_types=['text'])
async def user_handler(message: types.Message):
    #one of info buttons
    if message.text == keyboard.timedate:
        await bot.send_message(message.chat.id, rp.time_place, parse_mode='html', disable_web_page_preview=True)

    #and another one
    elif message.text == keyboard.info:
        await bot.send_message(message.chat.id, rp.about, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.info_menu)

    #and another one
    elif message.text == keyboard.show_host:
        await bot.send_message(message.chat.id, rp.host, parse_mode='html', disable_web_page_preview=True)

    #and another one
    elif message.text == keyboard.history:
        await bot.send_message(message.chat.id, rp.background, parse_mode='html', disable_web_page_preview=True)

    #go to menu button
    elif message.text == keyboard.go_to_main:
        #every time user goes to main theirs status resets
        rdb.delete_status(message.from_user.id)
        await bot.send_message(message.chat.id, choice(rp.menu), parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)

    #reserving button
    elif message.text == keyboard.reserv:
        #check if there is no available seats
        reserved = await db.get_reserved()
        if reserved == conf.total_amount_of_seats:
            await bot.send_message(message.chat.id, rp.finished, parse_mode='html', disable_web_page_preview=True)

        else:
            #check if person already exists in db
            person = await db.check_person(message.from_user.id)
            if person is None:
                #add new person to db
                await db.add_person(message.from_user.id)
                #set status for this person, allow them to send numbers
                rdb.allow_nubres(message.from_user.id)
                await bot.send_message(message.chat.id, rp.amount, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.number_of_seats)

            else:
                #chek if this user is in db and did't sent amount of guests yet
                amount = await db.check_amount(message.from_user.id)
                if amount is None:
                    #set status for this person, allow them to send numbers
                    rdb.allow_nubres(message.from_user.id)
                    await bot.send_message(message.chat.id, rp.amount, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.number_of_seats)

                else:
                    await bot.send_message(message.chat.id, rp.error1,  parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)

    #if input is number of guests
    elif help.is_num_of_guests(message.text):
        #get reserved seats
        reserved = await db.get_reserved()
        #if amount of guests is bigger, than amount of free seats
        if int(message.text) > conf.total_amount_of_seats-reserved:
            await bot.send_message(message.chat.id, rp.invalid.format(message.text, conf.total_amount_of_seats-reserved), parse_mode='html', disable_web_page_preview=True)
        
        else:
            #check "callback" in redis db
            if rdb.get_status(message.from_user.id) == "numbers_allowed":
                #generate token and add amount of guests and token to db
                token = await db.add_token_amount_get_token(message.text, message.from_user.id)
                #delete status in rdb
                rdb.delete_status(message.from_user.id)
                await bot.send_message(message.chat.id, rp.booked.format(message.text, token), parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.offer)

            elif rdb.get_status(message.from_user.id) == "change_numbers_allowed":
                #change amount of guests in the db
                await db.change_amount(message.text, message.from_user.id)
                #delete status in rdb
                rdb.delete_status(message.from_user.id)
                await bot.send_message(message.chat.id, rp.changed.format(message.text), parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.offer)
            
            else:
                await bot.send_message(message.chat.id, rp.error8, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)

    #change menu
    elif message.text == keyboard.change:
        #check if this person exists in the db
        person = await db.check_person(message.from_user.id)
        if person is None:
            await bot.send_message(message.chat.id, rp.error5, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)

        else:
            #chek if this person sent amount of guests
            amount = await db.check_amount(message.from_user.id)
            if amount is None:
                await bot.send_message(message.chat.id, rp.error6, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)

            #send chage menu buttons
            else:
                #set status in rdb, allow user to use change menu buttons
                rdb.allow_change_menu(message.from_user.id)
                amount = await db.check_amount(message.from_user.id)
                token = await db.check_token(message.from_user.id)
                if await db.get_payment_method(message.from_user.id) is None:
                    payment = rp.not_paid
                else:
                    payment = rp.not_paid
                await bot.send_message(message.chat.id, rp.status.format(amount, payment, token), parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.change_menu)

    #if user wants to change amount of guests
    elif message.text == keyboard.change_amount:
        #check status in rdb
        if rdb.get_status(message.from_user.id) == "change_menu_allowed":
            #allow programm to update the num of guests
            rdb.allow_change_numbers(message.from_user.id)
            await bot.send_message(message.chat.id, rp.amount, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.number_of_seats)
        else:
            await bot.send_message(message.chat.id, rp.error9, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)

    #if user wants to cansel his book
    elif message.text == keyboard.cansel:
        #check status in rdb
        if rdb.get_status(message.from_user.id) == "change_menu_allowed":
            #allow user to use accident menu buttons
            rdb.allow_accident_menu(message.from_user.id)
            await bot.send_message(message.chat.id, rp.accident, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.accident)
        else:
            await bot.send_message(message.chat.id, rp.error9, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)

    #if missclick
    elif message.text == keyboard.oops:
        #check status in rdb
        if rdb.get_status(message.from_user.id) == "accident_menu_allowed":
            #allow user to use accident menu buttons
            rdb.allow_change_menu(message.from_user.id)
            await bot.send_message(message.chat.id, rp.missclick, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.change_menu)
        else:
            await bot.send_message(message.chat.id, rp.error10, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)
        
    #if user is shure, that he wants to cansel his book
    elif message.text == keyboard.shure:
        if rdb.get_status(message.from_user.id) == "accident_menu_allowed":
            #allow user to use accident menu buttons
            rdb.delete_status(message.from_user.id)
            await db.cancel_book(message.from_user.id)
            await bot.send_message(message.chat.id, rp.canseled, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)
        else:
            await bot.send_message(message.chat.id, rp.error10, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)

    #if user wants to buy a tickets
    elif message.text == keyboard.buy:
        #check status in rdb
        if rdb.get_status(message.from_user.id) == "change_menu_allowed":
            #my payment method:

            pass
        else:
            await bot.send_message(message.chat.id, rp.error9, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)
    
    else:
        rdb.delete_status(message.from_user.id)
        await bot.send_message(message.chat.id, rp.global_error, parse_mode='html', disable_web_page_preview=True, reply_markup=keyboard.main_menu)
