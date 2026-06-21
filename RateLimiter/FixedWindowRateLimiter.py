from RateLimiter import RateLimiter
import time
import threading


class FixedWindowRateLimiter(RateLimiter):
    def __init__(self, max_request, window_size_millis):
        self.max_requests = max_request
        self.window_size_millis = window_size_millis
        self.request_counts = {}
        self.window_start = int(time.time() * 1000)
        self.lock = threading.Lock()
        
    def allow_requests(self, user_id):
        with self.lock:
            current_time = int(time.time() * 1000)
            if current_time - self.window_start >= self.window_size_millis:
                self.request_counts.pop(user_id, None)
                self.window_start = current_time
            
            self.request_counts[user_id] = self.request_counts.get(user_id, 0) + 1
            return self.request_counts[user_id] <= self.max_requests
    