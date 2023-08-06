# coding: utf-8
"""Base logging gonfiguration."""

import logging
from logging.handlers import TimedRotatingFileHandler
import os

import pkg_resources

DATA_DIR = pkg_resources.resource_filename('tabassist', 'data/')
LOG_DIR = os.path.join(DATA_DIR, 'logs')


def get_logger(name):
    """Set up base logger for package."""
    logger = logging.getLogger(name)

    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

    handler = TimedRotatingFileHandler(
        filename=os.path.join(LOG_DIR, 'tabassist.log'),
        when='D',
        interval=1,
        backupCount=10)

    formatter = logging.Formatter('%(asctime)s  (%(name)s): %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel('INFO')
    return logger
