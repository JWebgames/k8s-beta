from os import getenv

LOGLEVEL = getenv("MESSAGER_LOGLEVEL", "DEBUG")
PULL_ADDRESS = getenv("MESSAGER_PULL_ADDR", "tcp://127.0.0.1:22549")
PUB_ADDRESS = getenv("MESSAGE_PUB_ADDR", "tcp://127.0.0.1:22550")
