from msilib.schema import Class
import queue

class ColaClass:
    def __init__(self):
        self.colainit = queue.Queue(maxsize=100)