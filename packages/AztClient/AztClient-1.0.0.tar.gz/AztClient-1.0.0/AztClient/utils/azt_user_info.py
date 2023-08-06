class AztUserInfo:
    def __init__(self, account=None, passwd=None, stgyid=None, stgycheck=None):
        self.__account = account
        self.__passwd = passwd
        self.__stgyid = stgyid
        self.__stgycheck = stgycheck

    def set(self, account=None, passwd=None, stgyid=None, stgycheck=None):
        if account:
            self.__account = account
        if passwd:
            self.__passwd = passwd
        if stgyid:
            self.__stgyid = stgyid
        if stgycheck:
            self.__stgycheck = stgycheck

    def getaccount(self):
        return self.__account

    def getpasswd(self):
        return self.__passwd

    def getstgyid(self):
        return self.__stgyid

    def getstgycheck(self):
        return self.__stgycheck
