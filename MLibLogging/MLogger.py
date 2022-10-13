import logging
import os
import sys
from datetime import date

from dotenv import load_dotenv

full_file_path = None


def __setup_logfile__(project_name, log_location_override):
    global full_file_path

    # Initializing

    today = date.today()
    filename = f'Log_{today.strftime("%d%m%Y")}.log'
    if log_location_override is not None:
        file_base = f'{log_location_override}\\{project_name}'
    else:
        file_base = f'{os.getenv("DEFAULT_LOG_LOC")}\\{project_name}'
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

    # region Constructors

    def __init__(self, project_name, log_location_override=None, log_level=logging.INFO):
        load_dotenv()
        __setup_logfile__(project_name=project_name, log_location_override=log_location_override)

        try:
            cwd = sys.argv[0]
        except:
            cwd = os.getcwd()

        logging.basicConfig(filename=full_file_path,
                            format=f'{cwd} %(asctime)s %(levelname)s: %(message)s',
                            level=log_level,
                            filemode='a')

    # endregion Constructors

    # region Methods

    def Debug(self, message):
        logging.debug(message)
        print(f'Debug:{message}')

    def Info(self, message):
        logging.info(message)
        print(f'Info:{message}')

    def Warning(self, message):
        logging.warning(message)
        print(f'Warning:{message}')

    def Error(self, message):
        logging.error(message)
        print(f'Error:{message}')

    def Critical(self, message):
        logging.critical(message)
        print(f'Critical:{message}')

    def GetLogFile(self):
        return full_file_path

    # endregion
