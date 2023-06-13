import datetime


def get_date(day: int):
    """Получение даты"""
    today = datetime.date.today()
    date = today - datetime.timedelta(days=day)
    return date
