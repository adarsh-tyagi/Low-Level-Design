from RateLimiterFactory import RateLimiterFactory

class RateLimiterService:
    def __init__(self):
        self.user_rate_limiters = {}
    
    def register_user(self, user_id, algorithm, max_requests, window_size_seconds):
        self.user_rate_limiters[user_id] = RateLimiterFactory.create_rate_limiter(algorithm, max_requests, window_size_seconds*1000)
    
    def allow_request(self, user_id):
        rate_limiter = self.user_rate_limiters.get(user_id)
        if rate_limiter is None:
            raise ValueError("User not registered")
        
        return rate_limiter.allow_request(user_id)
    