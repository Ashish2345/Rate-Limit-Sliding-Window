# Sliding Window Rate Limiter

## Overview

A flexible, high-performance rate limiting library for Python applications, supporting seamless integration with Django, Flask, FastAPI, and standalone Python projects.

## Features

- 🚀 Sliding Window Algorithm
- 🔒 Thread-safe implementation
- 🛠️ Highly configurable
- 🔌 Framework agnostic
- 📊 Customizable rate limiting

## Installation

```bash
pip install sliding-window-rate-limiter
```

## Quick Start

### Basic Usage

```python
from rate_limiter import SlidingWindowRateLimiter, RateLimiterConfig

# Default configuration
rate_limiter = SlidingWindowRateLimiter()

# Custom configuration
config = RateLimiterConfig(
    max_requests=50,  # 50 requests
    window_size=60.0  # per minute
)
custom_rate_limiter = SlidingWindowRateLimiter(config)

# As a decorator
@custom_rate_limiter.decorator()
def my_api_endpoint():
    # Your code here
    pass

# Manual consumption
try:
    rate_limiter.consume()  # Default key
    # Process request
except RateLimitExceededException as e:
    # Handle rate limit
    print(f"Wait {e.retry_after} seconds")
```

## Configuration Options

- `max_requests`: Maximum requests allowed
- `window_size`: Time window in seconds
- `precision`: Time tracking precision
- `distributed`: Distributed rate limiting flag
- `key_generator`: Custom key generation function

## Integration Examples

### Flask
```python
from flask import Flask
from rate_limiter import SlidingWindowRateLimiter

app = Flask(__name__)
rate_limiter = SlidingWindowRateLimiter()

@app.route('/endpoint')
def protected_endpoint():
    try:
        rate_limiter.consume()
        # Your route logic
    except RateLimitExceededException:
        return "Too Many Requests", 429
```

### Django
```python
from rate_limiter import SlidingWindowRateLimiter

rate_limiter = SlidingWindowRateLimiter()

def my_view(request):
    try:
        rate_limiter.consume()
        # View logic
    except RateLimitExceededException:
        return HttpResponseTooManyRequests()
```

## License

MIT License
