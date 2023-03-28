class LocalStorage(object):
    __jwt_black_jtis=[]


    @classmethod
    def getJwtBlackJtis(cls):
        return cls.__jwt_black_jtis

    @classmethod
    def setJwtBlackJtis(cls, blackJtis):
        cls.__jwt_black_jtis = blackJtis
