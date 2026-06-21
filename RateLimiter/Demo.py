from Service import RateLimiterService
from LeakyBucketRateLimiter import LeakyBucketRateLimiter
import time

class Demo:
    def __init__(self):
        self.service = RateLimiterService()
    
    def main(self):
        self.service.register_user("user_1", "fixed", 3, 10)
        self.service.register_user("user_2", "sliding", 3, 10)
        self.service.register_user("user_3", "token-bucket", 3, 10)
        self.service.register_user("user_4", "leaky-bucket", 3, 10)
        
        for i in range(5):
            print(f"User 1 request {i+1} : {self.service.allow_request('user_1')}")
            print(f"User 2 request {i+1} : {self.service.allow_request('user_2')}")
            print(f"User 3 request {i+1} : {self.service.allow_request('user_3')}")
            print(f"User 4 request {i+1} : {self.service.allow_request('user_4')}")
            time.sleep(1)
        
        limiter = self.service.user_rate_limiters.get("user_4")
        if isinstance(limiter, LeakyBucketRateLimiter):
            limiter.stop()
            
if __name__ == "__main__":
    Demo().main()