from src.shared.ILogger import ILogger
from datetime import date
import logging

class LocalLogger(ILogger):
    
    def __init__(self):
        self.start()
        


    def log_warning(self, message):
        logging.warning(message)
        


    def log_info(self, message):
        logging.info(message)
        


    def log_error(self, message):
        logging.error(message)
        pass


    def start(self):
        today = date.today()
        path = "./LOGS/log" + today.strftime("%b-%d-%Y") + ".log"
        logging.basicConfig(filename=path , level=logging.DEBUG)
        logging.info("Starting logging service")
        
        