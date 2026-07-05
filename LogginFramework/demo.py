from log_manager import LogManager
from log_level import LogLevel
from log_appender import ConsoleAppender
import time


class Demo:
    @staticmethod
    def main():
        # intial config
        log_manager = LogManager.get_instance()
        root_logger = log_manager.get_root_logger()
        root_logger.set_level(LogLevel.INFO)
        
        # add console appender to root logger
        root_logger.add_appender(ConsoleAppender())
        
        main_logger = log_manager.get_logger("com.example.Main")
        main_logger.info("Application startiung up")
        main_logger.debug("This is debug message")
        main_logger.warn("This is warning message")
        
        print("--- Logger Hierarchy Demo ---")
        db_logger = log_manager.get_logger("com.example.db")
        db_logger.info("Database connection pool initializing")
        
        service_logger = log_manager.get_logger("com.example.service.UserService")
        service_logger.set_level(LogLevel.DEBUG)
        service_logger.info("User servuce starting")
        service_logger.debug("This debug message should not appear for this service logger")
        
        print("Changing root log level to debug...")
        root_logger.set_level(LogLevel.DEBUG)
        main_logger.debug("This will appear")
        
        try:
            time.sleep(0.5)
            log_manager.shutdown()
        except Exception as e:
            print("Error occured while shutting down the log manager.", e)
    

if __name__ == "__main__":
    Demo.main()