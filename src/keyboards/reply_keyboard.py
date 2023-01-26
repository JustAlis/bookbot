from aiogram import types

#admin menu buttons
send_promo = 'send promo'
get_stats = 'stats'
reset_db = 'reset'
edit_date_place = 'edit date place'
edit_promo = 'edit promo'
admin_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
admin_menu.add(get_stats, edit_date_place, edit_promo, send_promo, reset_db)

#admn warning buttons
yes = 'Yes'
no = 'No'
admin_warning = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
admin_warning.add(no, yes)

#main menu buttons
info = 'Инфо о пректе'
#Project info
reserv = 'Забронировать места'
#Book seats
timedate = 'Когда, где, сколько стоит?'
#When, where, how much?
change = 'Управлять бронью'
#Manage booking
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
main_menu.add(info, reserv, timedate, change)

#info menu buttons
show_host = 'А кто ведущий?'
#And who is the show host?
history = 'История нашего шоу'
#History of our show
go_to_main = 'Главное меню'
#Main menu
info_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
info_menu.add(show_host, history, go_to_main)

#buttons for charnge menu
buy = 'Оплатить билеты'
#buy the tickets
change_amount = 'Изменить количество гостей'
#change amount of guests
cansel = 'Отменить бронь'
#cansel book
change_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
change_menu.add(buy, change_amount, cansel, go_to_main)

#buttons for amount of peple
one='1'
two='2'
three='3'
four='4'
five='5'
six='6'
number_of_seats= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
number_of_seats.add(one, two, three, four, five, six, go_to_main)

#buttons for accidend press of cansel
shure = 'Уверен'
#shure
oops = 'Вернуться назад'
#go back
accident = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
accident.add(shure, oops, go_to_main)

#buttons after the book, offering to buy
offer = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
offer.add(buy, change, go_to_main)

#remove replykeyboard
remove = types.ReplyKeyboardRemove()