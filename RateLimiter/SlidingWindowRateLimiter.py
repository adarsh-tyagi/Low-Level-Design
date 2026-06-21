from RateLimiter import RateLimiter
from collections import deque
import time
import threading


class SlidingWindowRateLimiter(RateLimiter):
    def __init__(self, max_requests, window_size_millis):
        self.max_requests = max_requests
        self.window_size_millis = window_size_millis
        self.request_logs = {}
        self.lock = threading.Lock()
        
    def allow_request(self, user_id):
        with self.lock:
            current_time = int(time.time() * 1000)
            if user_id not in self.request_logs:
                self.request_logs[user_id] = deque()
            
            timestamps = self.request_logs[user_id]
            
            while timestamps and current_time - timestamps[0] >= self.window_size_millis:
                timestamps.popleft()
            
            if len(timestamps) < self.max_requests:
                timestamps.append(current_time)
                return True
            
            return False