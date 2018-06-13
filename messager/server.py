import atexit
from logging import getLogger
import zmq
from config import PUB_ADDRESS, PULL_ADDRESS

logger = getLogger(__name__)

def main():
    context = zmq.Context()

    puber = context.socket(zmq.PUB)
    puber.bind(PUB_ADDRESS)
    logger.info("Publisher listening on %s", PUB_ADDRESS)

    puller = context.socket(zmq.PULL)
    puller.bind(PULL_ADDRESS)
    logger.info("Puller listening on %s", PULL_ADDRESS)

    @atexit.register
    def close():
        logger.info("Closing sockets...")
        puber.close()
        puller.close()
        logger.info("Closed.")

    logger.info("Starting main loop")
    while True:
        msg = puller.recv()
        logger.debug("New message: %s", msg)
        puber.send(msg)

