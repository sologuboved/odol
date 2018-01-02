from datetime import datetime, timedelta
from global_vars import DEFAULT
DOT = '.'


def date_to_string(date):
    try:
        return date.strftime("%d.%m.%Y")
    except AttributeError:
        return


def string_to_date(raw_date):
    if raw_date == 'today':
        return datetime.today()

    try:
        date = list(map(int, map(lambda i: i.strip(), raw_date.split(DOT))))
    except (ValueError, AttributeError):
        return

    date.reverse()
    length = len(date)

    if not length or length > 3:
        return

    if length == 3:
        try:
            return datetime(*date)
        except (TypeError, ValueError):
            return

    this_year = datetime.today().year

    if length == 1:
        this_month = datetime.today().month
        try:
            return datetime(this_year, this_month, *date)
        except (TypeError, ValueError):
            return

    try:
        return datetime(this_year, *date)
    except (TypeError, ValueError):
        return


def string_to_delta(raw_delta):
    raw_delta = raw_delta.strip()
    if not raw_delta:
        return timedelta(DEFAULT)
    try:
        delta = int(raw_delta.strip())
        if delta <= 0:
            return
    except ValueError:
        return
    return timedelta(delta)

