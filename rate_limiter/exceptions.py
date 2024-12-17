from collections import namedtuple

EXCEPTION_CODE = namedtuple("EXCEPTION_CODE", ["data", "message"])

RATELIMIT_EXCEEDED_EXCEPTION = EXCEPTION_CODE("Request exceeded", "Request Exceeded: Try again after few minutes")

class BaseException(Exception):

    def __init__(self, exec_code: EXCEPTION_CODE):
        super().__init__(exec_code.message)
        self.data = exec_code.data

    @classmethod
    def default_exception(cls):
        # Raise the default exception with a predefined error code
        raise cls(RATELIMIT_EXCEEDED_EXCEPTION)

class RatelimitExceedException(BaseException):
    def __init__(self, exec_code: EXCEPTION_CODE, exec_status: str):
        super().__init__(exec_code)
        self.exec_status = exec_status