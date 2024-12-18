import time
import threading
from collections import defaultdict
from typing import Union, Callable, Any

from .exceptions import RateLimitExceededException, ConfigurationError
from .configs import RateLimiterConfig

class SlidingWindowRateLimiter:
    """
    Sliding Window Rate Limiter implementation with advanced features.
    
    Supports:
    - In-memory rate limiting
    - Configurable window size and request limits
    - Thread-safe operations
    - Optional custom key generation
    """
    
    def __init__(self, config: RateLimiterConfig = None):
        """
        Initialize the rate limiter.
        
        Args:
            config (RateLimiterConfig, optional): Configuration for rate limiting
        """
        self.config = config or RateLimiterConfig()
        self.config.validate()
        
        # Thread-safe storage for request timestamps
        self._request_log = defaultdict(list)
        self._lock = threading.Lock()
    
    def _get_key(self, key: Union[str, Callable[[], Any]] = None) -> str:
        """
        Generate a rate limit key.
        
        Args:
            key (Union[str, Callable], optional): Custom key or key generator
        
        Returns:
            str: Rate limit key
        """
        if key is None:
            return "default"
        
        if callable(key):
            return str(key())
        
        return str(key)
    
    def _prune_old_requests(self, key: str, current_time: float):
        """
        Remove timestamps outside the current sliding window.
        
        Args:
            key (str): Rate limit key
            current_time (float): Current timestamp
        """
        window_start = current_time - self.config.window_size
        self._request_log[key] = [
            timestamp for timestamp in self._request_log[key]
            if timestamp > window_start
        ]
    
    def consume(self, key: Union[str, Callable[[], Any]] = None) -> bool:
        """
        Check and record a request in the rate limit.
        
        Args:
            key (Union[str, Callable], optional): Rate limit key
        
        Returns:
            bool: True if request is allowed, False otherwise
        
        Raises:
            RateLimitExceededException: If rate limit is exceeded
        """
        import pdb; pdb.set_trace()
        current_time = time.time()
        rate_key = self._get_key(key)
        
        with self._lock:
            # Prune old request timestamps
            self._prune_old_requests(rate_key, current_time)
            
            # Check if request limit is exceeded
            if len(self._request_log[rate_key]) >= self.config.max_requests:
                oldest_request = self._request_log[rate_key][0]
                retry_after = self.config.window_size - (current_time - oldest_request)
                
                raise RateLimitExceededException(
                    "Rate limit exceeded", 
                    retry_after
                )
            
            # Record the current request
            self._request_log[rate_key].append(current_time)
            return True
    
    def decorator(self, key: Union[str, Callable[[], Any]] = None):
        """
        Decorator to apply rate limiting to functions.
        
        Args:
            key (Union[str, Callable], optional): Rate limit key
        
        Returns:
            Callable: Decorated function with rate limiting
        """
        def decorator_wrapper(func):
            def wrapper(*args, **kwargs):
                self.consume(key)
                return func(*args, **kwargs)
            return wrapper
        return decorator_wrapper