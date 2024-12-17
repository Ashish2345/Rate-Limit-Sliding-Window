import time

from django.core.cache import cache


class SlidingWindowsthrottle:

    def __init__(self, max_request, window_size):
        self.max_request = max_request
        self.window_size = window_size

    def allow_request(self):
        ...
