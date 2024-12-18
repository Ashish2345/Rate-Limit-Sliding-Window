import time
import pytest
from rate_limiter.throttling import SlidingWindowRateLimiter, RateLimiterConfig, RateLimitExceededException

def test_basic_rate_limiting():
    """Test basic rate limiting functionality"""
    config = RateLimiterConfig(max_requests=3, window_size=1.0)
    rate_limiter = SlidingWindowRateLimiter(config)
    
    # First 3 requests should pass
    for _ in range(3):
        assert rate_limiter.consume() is True
    
    # 4th request should raise exception
    with pytest.raises(RateLimitExceededException):
        rate_limiter.consume()

def test_sliding_window():
    """Test sliding window behavior"""
    config = RateLimiterConfig(max_requests=3, window_size=1.0)
    rate_limiter = SlidingWindowRateLimiter(config)
    
    # Consume 3 requests
    for _ in range(3):
        rate_limiter.consume()
    
    # Wait for 0.5 seconds
    time.sleep(0.5)
    
    # Should allow 1 more request in the sliding window
    assert rate_limiter.consume() is True