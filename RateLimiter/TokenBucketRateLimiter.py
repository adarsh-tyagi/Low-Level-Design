from RateLimiter import RateLimiter
from collections import deque
import time
import threading

class TokenBucketRateLimiter(RateLimiter):
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = {}
        self.last_refill_timestamp = {}
        self.lock = threading.Lock()
        
    def allow_requests(self, user_id):
        with self.lock:
            current_time = int(time.time() * 1000)
            
            if user_id not in self.last_refill_timestamp:
                self.last_refill_timestamp[user_id] = current_time
            if user_id not in self.tokens:
                self.tokens[user_id] = self.capacity
            
            last_refill = self.last_refill_timestamp[user_id]
            elapsed_time_secs = (current_time - last_refill) // 1000
            
            if elapsed_time_secs > 0:
                new_tokens = min(self.capacity, self.tokens[user_id] + int(elapsed_time_secs * self.refill_rate))
                self.tokens[user_id] = new_tokens
                self.last_refill_timestamp[user_id] = current_time
            
            if self.tokens[user_id] > 0:
                self.tokens[user_id] -= 1
                return True
            return False