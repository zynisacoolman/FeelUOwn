# -*- coding:utf8 -*-

import logging

import setting


"""
log messages for developers
"""


# CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
if setting.MODE == setting.DEBUG:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] [%(filename)s line:%(lineno)d] : %(message)s"
    )
else:
    logging.basicConfig(
        level=logging.WARNING,
        format="[%(levelname)s] [%(filename)s line:%(lineno)d] : %(message)s",
    )

LOG = logging.getLogger("log")
