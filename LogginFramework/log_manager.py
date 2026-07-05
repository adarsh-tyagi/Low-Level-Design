import threading
from logger import Logger
from async_log_processor import AsyncLogProcessor


class LogManager:
    _instance = None
    _lock = threading.Lock()
    
    def __init__(self):
        if LogManager._instance is not None:
            raise Exception("This class is a singleton")
        self.loggers = {}
        self.root_logger = Logger("root", None)
        self.loggers["root"] = self.root_logger
        self.processor = AsyncLogProcessor()
        
    @staticmethod
    def get_instance():
        if LogManager._instance is None:
            with LogManager._lock:
                if LogManager._instance is None:
                    LogManager._instance = LogManager()
        return LogManager._instance
    
    def get_logger(self, name):
        if name not in self.loggers:
            self.loggers[name] = self._create_logger(name)
        return self.loggers[name]

    def _create_logger(self, name):
        if name == "root":
            return self.root_logger
        last_dot = name.rfind(".")
        parent_name = "root" if last_dot == -1 else name[:last_dot]
        parent = self.get_logger[parent_name]
        return Logger(name, parent)

    def get_root_logger(self):
        return self.root_logger
    
    def get_processor(self):
        return self.processor
    
    def shutdown(self):
        self.processor.stop()
        
        all_appenders = set()
        for logger in self.loggers.values():
            for appender in logger.get_appenders():
                all_appenders.add(appender)
        
        for appender in all_appenders:
            appender.close()
            
        print("Logging framework shutdown successfully")