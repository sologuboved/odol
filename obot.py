# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
from tkn import TOKEN, MY_ID
from process_commands import *

NOAUTH = "This is a private bot"
ATTEMPT = "%d attempted %s"


def is_authorized(chat_id):
    return chat_id == MY_ID


def start(bot, update):
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        text = NOAUTH
        print(ATTEMPT % (chat_id, '/start'))
    else:
        text = "=-*=-*-=*-="
    bot.send_message(chat_id=chat_id, text=text)


def description(bot, update):
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        text = NOAUTH
        print(ATTEMPT % (chat_id, '/help'))
    else:
        text = "Commands: \n\n" \
               "/first\n" \
               "/nth 26\n" \
               "/whd 02.01.2018\n" \
               "/rewr 02.01.2018"
    bot.send_message(chat_id=chat_id, text=text)


def rewr(bot, update):
    # /rewr 02.01.2018
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/rewr'))
    else:
        query = update['message']['text']
        print('query:', query)
        query = query.split()
        try:
            query = query[1]
        except IndexError:
            query = ''
        reply = rewrite_file(query)
        print('reply:', reply, '\n')
    bot.send_message(chat_id=chat_id, text=reply)


def first(bot, update):
    # /first
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/cur'))
    else:
        query = update['message']['text']
        print('query:', query)
        reply = see_first()
        print('reply:\n', reply, '\n')
    bot.send_message(chat_id=chat_id, text=reply)


def nth(bot, update):
    # /nth 26
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/slew'))
    else:
        query = update['message']['text']
        print('query:', query)
        query = query.split()
        try:
            query = query[1]
        except IndexError:
            query = ''
        reply = get_nth(query)
        print('reply:', reply, '\n')
    bot.send_message(chat_id=chat_id, text=reply)


def whd(bot, update):
    # /nth 26
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/slew'))
    else:
        query = update['message']['text']
        print('query:', query)
        query = query.split()
        try:
            query = query[1]
        except IndexError:
            query = ''
        reply = which_day(query)
        print('reply:', reply, '\n')
    bot.send_message(chat_id=chat_id, text=reply)


if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', description)
    rewr_handler = CommandHandler('rewr', rewr)
    first_handler = CommandHandler('first', first)
    nth_handler = CommandHandler('nth', nth)
    whd_handler = CommandHandler('whd', whd)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(rewr_handler)
    dispatcher.add_handler(first_handler)
    dispatcher.add_handler(nth_handler)
    dispatcher.add_handler(whd_handler)

    updater.start_polling()
