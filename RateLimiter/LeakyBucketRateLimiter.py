from RateLimiter import RateLimiter
from collections import deque
import time
import threading

class LeakyBucketRateLimiter(RateLimiter):
    def __init__(self, capacity, leak_rate_secs):
        self.capacity = capacity
        self.leak_rate_secs = leak_rate_secs
        self.bucket = deque()
        self.lock = threading.Lock()
        self._stop_event = threading.Event()
        
        self.leak_thread = threading.Thread(target=self._leak_loop, daemon=True)
        self.leak_thread.start()
    
    def allow_request(self, user_id):
        with self.lock:
            current_time = int(time.time() * 1000)
            if len(self.bucket) < self.capacity:
                self.bucket.append(current_time)
                return True
            return False
    
    def _leak_requests(self):
        with self.lock:
            if self.bucket:
                self.bucket.popleft()
    
    def _leak_pop(self):
        while not self._stop_event.is_set():
            self._leak_requests()
            time.sleep(self.leak_rate_secs)
    
    def stop(self):
        self._stop_event.set()
        self.leak_thread.join()
        