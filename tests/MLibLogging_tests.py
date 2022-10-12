import logging
import os.path

from MLibLogging.MLogger import MLogger


# region Methods

def log_test(logger):
    logger.debug("Here's a debugger")
    logger.info("Here's some information")
    logger.warning("And here's a warning")
    logger.error("Here's an error")
    logger.critical("This is critical")


def logger_setup_test():
    app = os.path.splitext(os.path.basename(__file__))[0]
    logger = MLogger(app)
    assert logger is not None


# endregion


if __name__ == "__main__":

    # Run tests
    logger_setup_test()
    log_test()