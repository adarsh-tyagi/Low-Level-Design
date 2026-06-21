from FixedWindowRateLimiter import FixedWindowRateLimiter
from SlidingWindowRateLimiter import SlidingWindowRateLimiter
from TokenBucketRateLimiter import TokenBucketRateLimiter
from LeakyBucketRateLimiter import LeakyBucketRateLimiter


class RateLimiterFactory:
    @staticmethod
    def create_rate_limiter(type_, max_requests, window_size_millis):
        if type_ == "fixed":
            return FixedWindowRateLimiter(max_requests, window_size_millis)

        elif type_ == "sliding":
            return SlidingWindowRateLimiter(max_requests, window_size_millis)
        
        elif type_ == "token-bucket":
            return TokenBucketRateLimiter(max_requests, (1.0 * max_requests / window_size_millis * 1000))

        elif type_ == "leaky-bucket":
            return LeakyBucketRateLimiter(max_requests, int(1.0 * max_requests / window_size_millis * 1000))
        
        else:
            raise ValueError("Unsupported type")
