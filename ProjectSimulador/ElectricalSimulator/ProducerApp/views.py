import queue
import time
import random
import logging


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

class Producerdevice:   

    def __init__(self):
        self.cola = queue.Queue(maxsize=100)

    def Producer(self):
      
        while True:
            if not self.cola.full():
                item = random.randint(1, 100)
                self.cola.put(item)

                logging.info(f'Nuevo elemento dentro de la cola {item}')

                time_to_sleep = random.randint(1, 3)
                time.sleep(time_to_sleep)
