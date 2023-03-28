class Result(object):
    
    CODE_SUCCESS=200
    CODE_FAIL=9
    MESSAGE_SUCCESS='success'
    def __init__(self):
        self.code=Result.CODE_SUCCESS
        self.message=Result.MESSAGE_SUCCESS
        self.data=None

    @staticmethod
    def fail(code,message):
        r=Result()
        r.code= code
        r.message=message
        return r

    @staticmethod
    def success(data=""):
        r=Result()
        r.data=data
        return r