class RateLimitExceededException(Exception):
    """
    Exception raised when rate limit is exceeded.
    
    Attributes:
        message (str): Explanation of the rate limit violation
        retry_after (float): Suggested time to wait before next request
    """
    def __init__(self, message: str, retry_after: float = None):
        self.message = message
        self.retry_after = retry_after
        super().__init__(self.message)

class ConfigurationError(Exception):
    """
    Exception raised for invalid configuration settings.
    """
    pass