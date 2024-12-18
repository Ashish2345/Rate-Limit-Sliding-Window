from dataclasses import dataclass
from typing import Optional, Union

from .exceptions import ConfigurationError

@dataclass
class RateLimiterConfig:
    """
    Configuration class for rate limiter settings.
    
    Attributes:
        max_requests (int): Maximum number of requests allowed in the time window
        window_size (float): Size of the sliding window in seconds
        precision (int): Number of decimal places for time tracking
        distributed (bool): Flag for distributed rate limiting
        key_generator (Optional[callable]): Custom function to generate rate limit keys
    """
    max_requests: int = 100
    window_size: float = 60.0  # 1 minute default
    precision: int = 3
    distributed: bool = False
    key_generator: Optional[callable] = None

    def validate(self):
        """
        Validate configuration settings.
        
        Raises:
            ConfigurationError: If configuration is invalid
        """
        if self.max_requests <= 0:
            raise ConfigurationError("Max requests must be a positive integer")
        
        if self.window_size <= 0:
            raise ConfigurationError("Window size must be a positive number")