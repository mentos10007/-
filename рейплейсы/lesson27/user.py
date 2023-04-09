import requests

class User:
    def __init__(self, im="", fam="", pas="", log=""):
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.login = self.__data["Login"] if not log else log
        self.__password = self.__data["Password"] if not pas else pas
        self.imya = self.__data["FirstName"] if not im else im
        self.familiya = self.__data["LastName"] if not fam else fam
        self.podpiski = []
        self.podpischiki = []

    def log_in(self, i, p):
        if i == self.login and p == self.__password:
            return True