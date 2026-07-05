import sys
from concurrent.futures import ThreadPoolExecutor

class AsyncLogProcessor:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="AsyncLogProcessor")
        self.shutdown_flag = False
        
    def process(self, log_message, appenders):
        if self.shutdown_flag:
            print("Logger is shut down. Can not process log message", file=sys.stderr)
            return 
        
        def process_task():
            for appender in appenders:
                appender.append(log_message)
        
        self.executor.submit(process_task)
    
    def stop(self):
        self.shutdown_flag = True
        self.executor.shutdown(wait=True, timeout=2)
        if not self.executor._shutdown:
            print("Logger executor did not terminate in the specified time.", file=sys.stderr)