import schedule
import time
from telegram import Bot
from tkn import *
from process_commands import which_day
from process_data import delta_to_string
from pid_operations import write_pid


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
    write_pid()
    print("Launching alert sender... ")
    schedule.every().day.at('09:00').do(send_alert)
    while True:
        schedule.run_pending()
        time.sleep(1)
