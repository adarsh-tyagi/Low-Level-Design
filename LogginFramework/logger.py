from log_level import LogLevel
from log_message import LogMessage


class Logger:
    def __init__(self, name, parent):
        self.name = name
        self.level = None
        self.parent = parent
        self.appenders = []
        self.additivity = True
        
    def add_appender(self, appender):
        self.appenders.append(appender)
    
    def get_appenders(self):
        return self.appenders
    
    def set_level(self, level):
        self.level = level
        
    def set_additivity(self, additivity):
        self.additivity = additivity
        
    def get_effective_level(self):
        logger = self
        while logger is not None:
            current_level = logger.level
            if current_level is not None:
                return current_level
            
            logger = logger.parent
        return LogLevel.DEBUG
    
    def log(self, message_level, message):
        if message_level.is_greater_or_equal(self.get_effective_level()):
            log_message = LogMessage(message_level, self.name, message)
            self._call_appender(log_message)
    
    def _call_appenders(self, log_message):
        if self.appenders:
            from log_manager import LogManager
            LogManager.get_instance().get_process().process(log_message, self.appenders)
        if self.additivity and self.parent is not None:
            self.parent._call_appender(log_message)
    
    def debug(self, message):
        self.log(LogLevel.DEBUG, message)
    
    def info(self, message):
        self.log(LogLevel.INFO, message)
    
    def warn(self, message):
        self.log(LogLevel.WARN, message)
    
    def error(self, message):
        self.log(LogLevel.ERROR, message)
    
    def fatal(self, message):
        self.log(LogLevel.FATAL, message)