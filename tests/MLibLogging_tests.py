import logging
import os.path

from MLibLogging.MLogger import MLogger

# region Fields

test_logger = None


# endregion


# region Methods

def log_test():
    if test_logger is None:
        raise NameError('test_logger was never initialized')

    print(f"logging to '{test_logger.GetLogFile()}'")
    test_logger.Debug("Debug test entry")
    test_logger.Info("Info test entry")
    test_logger.Warning("Warning test entry")
    test_logger.Error("Error test entry")
    test_logger.Critical("Critical test entry")

    # TODO: Validate these entries exist in log file


def logger_setup_test():
    global test_logger

    appName = os.path.splitext(os.path.basename(__file__))[0]
    print(f'Creating logger for {appName}')
    test_logger = MLogger(appName)
    print('Logger created')


    # TODO: Find better validation criteria
    assert test_logger is not None

    print('Logger setup test completed')


# endregion


if __name__ == "__main__":
    # Run tests
    logger_setup_test()
    log_test()
