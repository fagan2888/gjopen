# -*- coding: utf-8 -*-
"""
code for managing state of the program of this repository
"""
import sys
import logging

# Configure logger
def configure_logger(name='',
                     console_logging_level=logging.INFO):
    """
    Configures logger
    from https://github.com/gmum/toolkit/blob/master/pytorch_project_template/src/utils.py
    :param name: logger name (default=module name, __name__)
    :param console_logging_level: level of logging to console (stdout), None = no logging
    :return instance of Logger class
    """

    if len(logging.getLogger(name).handlers) != 0:
        print("Already configured logger '{}'".format(name))
        return

    if console_logging_level is None and file_logging_level is None:
        return  # no logging

    logger = logging.getLogger(name)
    logger.handlers = []
    logger.setLevel(logging.DEBUG)
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    if console_logging_level is not None:
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(format)
        ch.setLevel(console_logging_level)
        logger.addHandler(ch)

    logger.info("Logging configured!")

    return logger
