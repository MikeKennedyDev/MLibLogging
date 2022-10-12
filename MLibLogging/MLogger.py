import logging
import os
from datetime import date

from dotenv import load_dotenv

full_file_path = ''


def __setup_logfile__(app_name):
    today = date.today()
    filename = f'Log_{today.strftime("%d%m%Y")}.log'
    file_base = f'{os.getenv("LOG_LOCATION_BASE")}\\{app_name}'

    global full_file_path
    full_file_path = f'{file_base}\\{filename}'

    # ensure the instance folder exists
    try:
        os.makedirs(file_base)
    except OSError:
        pass

    # ensure file exists
    f = open(full_file_path, 'a')
    f.close()


class MLogger:

    def __init__(self, application):
        load_dotenv()
        __setup_logfile__(app_name=application)

        logging.basicConfig(filename=full_file_path,
                            format='%(asctime)s %(levelname)s: %(message)s',
                            level=logging.INFO,
                            filemode='a')

    def debug(self, message):
        logging.debug(message)

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def critical(self, message):
        logging.critical(message)