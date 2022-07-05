import time
import queue
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)
queue = queue.Queue(maxsize=10)