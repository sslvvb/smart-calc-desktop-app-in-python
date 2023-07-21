import logging.handlers
import datetime
import pytz


class CustomTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, filename, when='h', backupCount=0, encoding=None, delay=False, utc=False):
        current_time = datetime.datetime.now(pytz.timezone('Asia/Novosibirsk')).strftime("%d-%m-%y-%H-%M-%S")
        filename = filename.format(current_time=current_time)
        super().__init__(filename, when=when, backupCount=backupCount, encoding=encoding, delay=delay, utc=utc)
