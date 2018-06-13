#!./venv/bin/python

import logging
from config import LOGLEVEL
from server import main

stdout = logging.StreamHandler()
stdout.formatter = logging.Formatter(
    "{asctime} [{levelname}] <{name}:{funcName}> {message}", style="{")
stdout.level = logging._nameToLevel[LOGLEVEL]

logging.root.handlers = [stdout]
logging.root.level = stdout.level

main()
