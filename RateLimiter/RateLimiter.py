from abc import ABC, abstractmethod

class RateLimiter(ABC):
    @abstractmethod
    def allow_request(self, userId):
        pass