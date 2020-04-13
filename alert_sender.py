from telegram import Bot
from tkn import TOKEN, MY_ID
from process_commands import which_day
from process_data import delta_to_string
from helpers import write_pid, delete_pid


def send_alert():
    bot = Bot(token=TOKEN)
    delta = which_day(str())
    try:
        day = delta.days
    except AttributeError:
        text = "Alert check failed: {}".format(delta)
        print(text)
        bot.send_message(chat_id=MY_ID, text=text)
    else:
        if day in (24, 25):
            bot.send_message(chat_id=MY_ID, text=delta_to_string(delta) + '!!!')


if __name__ == '__main__':
    pid_fname = write_pid()
    send_alert()
    delete_pid(pid_fname)
