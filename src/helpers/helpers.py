#check if the message.text is seat(s)
def is_num_of_guests(mess_text):
    try:
        if int(mess_text)>=1 and int(mess_text)<=6:
            return True
        return False
    except:
        return False
        
