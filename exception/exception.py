from dto import Result
from util import JsonUtil
class InvalidSystemClock(Exception):
    """
    时钟回拨异常
    """
    pass

class TokenNotFound(Exception):
    """
    Indicates that a token could not be found in the database
    """
    pass

class UserAlreadExist(Exception):
    pass


class BussinessException(Exception):
    error_code = 400
 
    def __init__(self,error_code=None,message='fail', payload=None):
        Exception.__init__(self)
        self.message = message
        if error_code is not None:
            self.error_code = error_code
        self.payload = payload
 
    def to_dict(self):
        return JsonUtil.class2dic_no_none(Result.fail(self.error_code, self.message))