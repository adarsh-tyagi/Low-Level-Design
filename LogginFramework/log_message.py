import threading
from datetime import datetime

class LogMessage:
    def __init__(self, level, logger_name, message):
        self.timestamp = datetime.now()
        self.level = level
        self.logger_name = logger_name
        self.message = message
        self.thread_name = threading.current_thread().name
        
    def get_timestamp(self):
        return self.timestamp
    
    def get_level(self):
        return self.level
    
    def get_logger_name(self):
        return self.logger_name
    
    def get_thread_name(self):
        return self.thread_name
    
    def get_message(self):
        return self.message
    