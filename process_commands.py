from global_vars import *
from process_data import *


def read_out():
    try:
        with open(FILENAME) as handler:
            return handler.readlines()[-1].strip()
    except FileNotFoundError:
        return NOT_FOUND


def rewrite_file(user_input):
    date = string_to_date(user_input)
    str_date = date_to_string(date, to_file=True)
    if not str_date:
        return INVALID_INPUT
    try:
        with open(FILENAME, 'a') as handler:
            handler.write('{}\n'.format(str_date))
            return "Wrote in %s" % date_to_string(date)
    except FileNotFoundError:
        return NOT_FOUND


def see_first():
    raw_date = read_out()
    if raw_date == NOT_FOUND:
        return NOT_FOUND
    date = string_to_date(raw_date)
    if not date:
        return NO_SENSE
    return date


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
    return date + lapse - timedelta(1)


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
    return new_date - first_date + timedelta(1)


def see_all(user_input):
    try:
        with open(FILENAME) as handler:
            lines = handler.readlines()
            try:
                start = int(user_input)
            except (ValueError, TypeError):
                start = 0
            return ''.join(lines[-start:]).strip()
    except FileNotFoundError:
        return NOT_FOUND
