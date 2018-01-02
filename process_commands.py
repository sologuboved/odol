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


def get_nth(user_input):
    lapse = string_to_delta(user_input)
    if not lapse:
        return INVALID_INPUT
    raw_date = read_out()
    if raw_date == NOT_FOUND:
        return NOT_FOUND
    date = string_to_date(raw_date)
    if not date:
        return NO_SENSE
    forecast = date + lapse - timedelta(1)
    return process_output(forecast)


def which_day(user_input):
    new_date = string_to_date(user_input)
    if not new_date:
        return INVALID_INPUT
    first_date = read_out()
    if first_date == NOT_FOUND:
        return NOT_FOUND
    first_date = string_to_date(first_date)
    if not first_date:
        return NO_SENSE
    if new_date <= first_date:
        return INVALID_INPUT
    lapse = new_date - first_date + timedelta(1)
    return delta_to_string(lapse)

