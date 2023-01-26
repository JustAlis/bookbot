#admin replies
admin_start = 'hello, admin'

#stats
stats = 'Всего пользователей: {}\nСделавших бронь: {}\nЗарезервировано мест:  {}\nБилетов куплено: {}'
#Total users: {}\nBooked: {}\nSeats reserved: {}\nTickets purchased: {}

#reset warning
reset_warning = 'WARNING\n\nВы собираетесь удалить все данные о забронированных и купленных билетах на ближайшее мероприятие.\n\nВы уверены?'
#WARNING\n\nYou are about to delete all booked and purchased tickets for an upcoming event.\n\nAre you sure?

#reset repry
reset_reply = 'Данные успешно удалены'
#Data deleted successfully

#denyed reset reply
denyed_reset = 'Данные не были удалены'
#Data has not been deleted

#place and time
time_place = """my time and place"""

#edit mode of date and place
time_place_edit_mode = 'Вы сейчас находитесь в режиме изменения даты, места проведения события и цене за билет.\n\nWARNING\n\nСодержание вашего следующего сообщения перезапишет информацию.\n\nДанный режим поддерживает html теги:\n<b> - жирный шрифт\n<i> - курсив, наклонный шрифт\n<s> - зачеркнутый текст\nПример использования:\n"<b>Жирный текст</b>"\n<a href="ссылка"> - ссылка.\nССЫЛКУ НУЖНО ПОМЕСТИТЬ В КАВЫЧКИ.\nПример использования:\n"<a href="ссылка">Текст, в котором будет сокрыта ссылка</a>"\nЭто не все возможности. Для получения более подробной информации можете ознакомиться с темой html тегов для оформления текста в интернете\n\nЕСЛИ ВЫ ТУТ СЛУЧАЙНО:\nСледующее сообщение содержит текущую информацию о дате и месте мероприятия, моежете скопировать его и отправить, чтобы не было изменений.'
#You are now in the mode to change the date, venue and ticket price.\n\nWARNING\n\nThe content of your next message will overwrite the information.\n\nThis mode supports html tags:\n<b> - bold\n< i> - italic, italic font\n<s> - strikethrough text\nUsage example:\n"<b>Bold text</b>"\n<a href="link"> - link.\nTHE LINK SHOULD BE PLACED IN QUOTATION MARKS.\nUsage example:\n"<a href="link">Text in which the link will be hidden</a>"\nThese are not all possibilities. For more information, you can read the topic of html tags for decorating text on the Internet\n\nIF YOU ARE HERE BY RANDOM:\nThe following message contains current information about the date and location of the event, you can copy it and send it without any changes.

#edit mode place and date end
time_place_edit_mode_end = 'Новое сообщение о дате и месте проведения мероприятия:'
#Update on the date and location of the event:

#promo
promo = 'my_promo'

#edit mode of promo
promo_edit_mode = 'Вы сейчас находитесь в режиме изменения рекламной рассылки.\n\nWARNING\n\nСодержание вашего следующего сообщения перезапишет информацию.\n\nДанный режим поддерживает html теги:\n<b> - жирный шрифт\n<i> - курсив, наклонный шрифт\n<s> - зачеркнутый текст\nПример использования:\n"<b>Жирный текст</b>"\n<a href="ссылка"> - ссылка.\nССЫЛКУ НУЖНО ПОМЕСТИТЬ В КАВЫЧКИ.\nПример использования:\n"<a href="ссылка">Текст, в котором будет сокрыта ссылка</a>"\nЭто не все возможности. Для получения более подробной информации можете ознакомиться с темой html тегов для оформления текста в интернете\n\nЕСЛИ ВЫ ТУТ СЛУЧАЙНО:\nСледующее сообщение содержит текущую рекламную рассылку, моежете скопировать его и отправить, чтобы не было изменений.'
#You are now in the mode of editing the advertising mailing.\n\nWARNING\n\nThe content of your next message will overwrite the information.\n\nThis mode supports html tags:\n<b> - bold\n<i> - italic, italic \n<s> - strikethrough text\nUse example:\n"<b>Bold text</b>"\n<a href="link"> - link.\nTHE LINK MUST BE IN QUOTATION MARKS.\nUse example:\ n"<a href="link">Text where the link will be hidden</a>"\nThese are not all possibilities. For more information, please refer to the topic of html tags for text styling on the web\n\nIF YOU ARE HERE BY RANDOM:\nThe following message contains the current promotional mailing, you can copy it and send it so that it does not change.

#edit mode of promo end
promo_edit_mode_end = 'Новое рекламное сообщение:'
#New ad message:

#if admin wants to send promo
send_promo_start = 'WARNING\n\nСледующее сообщение содержит текущую рекламную рассылку.\n\nВы уверены, что хотите её совершить?'
#WARNING\n\nThe following message contains the current promotional mailout.\n\nAre you sure you want to send it?

#end on sending of the promo
send_promo_end = 'Рекламная рассылка успешно завершена'
#Advertising mailing successfully completed

#sending of the promo denyed
send_promo_denyed = 'Рекламная рассылка отменена'
#Promotion has been canceled

#user replies
#random replys from bot, when use "go to main"
menu = ['my reply 1', 'my reply 2', 'and so on']

#start command reply
start = 'hello, user'

#info about the show
about = 'about the show...' 

#info about the host
host = 'about the host...'


#background of the show
background = 'my background'

#all of the seats are booked
finished = 'Места закончились('
#Seats are over

#ask how many peple are going to visit the show in the group
amount = 'Сколько вас будет?'
#How many of you will be?

#if amount is bigger, than amount of available seats
invalid = 'К сожалению {} мест не осталось.\nОсталось мест: {}'
#Unfortunately {} places are not left.\nSeats left: {}

#if book is chanded
changed = 'Бронь успешно изменена!\n{} мест успешно зобронировано\nХотите оплатить бронь?'
#Reservation successfully changed!\n{} Seats successfully reserved\nDo you want to pay for your reservation?

#after the book
booked = '{} мест успешно зобронировано!\n\nВаш уникальный токен бронирования:\n{}\n\nХотите оплатить бронь?'
#{} seats reserved successfully!\n\nYour unique reservation token:\n{}\n\nWould you like to pay for your reservation?

#if user wants to change his book
status = 'Cтатус вашей брони\n\nКоличество гостей: {}\nОплата: {}\nТокен: {}\n\nЧто вы хотите сделать?'
#Status of your booking\n\nNumber of guests: {}\nPayment: {}\nToken: {}\n\nWhat do you want to do?

#check if user is shure
accident = 'Вы уверены, что хотите отменить бронь?'
#Are you sure you want to cancel your booking?

#if missclicked
missclick = 'Ну вот и славно)'
#Well, that's nice)

#book is canseled
canseled = 'Бронь успешно отменена'
#Booking canceled successfully

#payment satus
paid = 'оплачено'
#paid

not_paid = 'на входе'
#not paid

#errors
admin_error = 'admin error'

error1 = 'ошибка. указано количество мест. попытка начать бронь повторно'
#error. the number of places indicated. attempt to start booking again

error5 = 'ошибка. вы не начали процесс бронирования. попытка управлять бронированием'
#error. you have not started the booking process. trying to manage a booking

error6 = 'ошибка. ещё не указано количество мест. попытка выбрать управлять бронированием'
#error. The number of seats has not been specified yet. trying to select manage booking

error8 = 'РЕДИС. ошибка. вы не начали процесс бронирования. попытка выбрать количество гостей'
#RADISH. error. you have not started the booking process. trying to select the number of guests

error9 = 'РЕДИС. ошибка. попытка доступа к кнопке меню управления бронью'
#REDIS. error. attempting to access the menu button for managing a booking

error10 = 'РЕДИС. ошибка. попытка дуступа к кнопке меню случаность'
#REDIS. error. attempt to access menu button randomness

global_error = 'НЕКОРРЕКТНЫЙ ВВОД'
#incorrect input
