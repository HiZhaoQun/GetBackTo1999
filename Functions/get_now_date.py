from datetime import datetime


def get_date():
    return datetime.now().date().strftime("%Y-%m-%d")


def get_now():
    return datetime.now()

