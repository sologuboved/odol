# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
from tkn import TOKEN, MY_ID
from process_commands import *
from pid_operations import write_pid

NOAUTH = "This is a private bot"
ATTEMPT = "%d attempted %s"


def is_authorized(chat_id):
    return chat_id == MY_ID


def start(update, context):
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        text = NOAUTH
        print(ATTEMPT % (chat_id, '/start'))
    else:
        text = "=-*=-*-=*-="
    context.bot.send_message(chat_id=chat_id, text=text)


def description(update, context):
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
    context.bot.send_message(chat_id=chat_id, text=text)


def rewr(update, context):
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
    context.bot.send_message(chat_id=chat_id, text=reply)


def first(update, context):
    # /first
    chat_id = update.message.chat_id
    if not is_authorized(chat_id):
        reply = NOAUTH
        print(ATTEMPT % (chat_id, '/cur'))
    else:
        query = update['message']['text']
        print('query:', query)
        reply = date_to_string(see_first())
        print('reply:\n', reply, '\n')
    context.bot.send_message(chat_id=chat_id, text=reply)


def nth(update, context):
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
        reply = date_to_string(get_nth(query))
        print('reply:', reply, '\n')
    context.bot.send_message(chat_id=chat_id, text=reply)


def whd(update, context):
    # /whd
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
            query = str()
        reply = delta_to_string(which_day(query))
        print('reply:', reply, '\n')
    context.bot.send_message(chat_id=chat_id, text=reply)


def surv(update, context):
    # /surv
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
            query = str()
        reply = see_all(query)
        print('reply:', reply, '\n')
    context.bot.send_message(chat_id=chat_id, text=reply)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', description)
    rewr_handler = CommandHandler('rewr', rewr)
    first_handler = CommandHandler('first', first)
    nth_handler = CommandHandler('nth', nth)
    whd_handler = CommandHandler('whd', whd)
    surv_handler = CommandHandler('surv', surv)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(rewr_handler)
    dispatcher.add_handler(first_handler)
    dispatcher.add_handler(nth_handler)
    dispatcher.add_handler(whd_handler)
    dispatcher.add_handler(surv_handler)

    updater.start_polling()


if __name__ == '__main__':
    write_pid()
    main()
