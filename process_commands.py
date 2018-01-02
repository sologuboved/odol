from global_vars import *
from process_data import *


def process_output(date):
    try:
        return date.strftime("%d %B %Y, %A")
    except AttributeError:
        return None


def read_out():
    try:
        with open(FILENAME) as handler:
            return handler.readline().strip()
    except FileNotFoundError:
        return NOT_FOUND


def rewrite_file(user_input):
    date = date_to_string(string_to_date(user_input))
    if not date:
        return INVALID_INPUT
    try:
        with open(FILENAME, 'w') as handler:
            handler.write(date)
            return ALRIGHT
    except FileNotFoundError:
        return NOT_FOUND


def see_first():
    raw_date = read_out()
    if raw_date == NOT_FOUND:
        return NOT_FOUND
    date = string_to_date(raw_date)
    if not date:
        return NO_SENSE
    return process_output(date)


def get_next(user_input):
    pass

