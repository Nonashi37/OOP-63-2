class BankAccount:

    def __init__(self, login, balance, password):
        self.login = login
        self._balance = balance
        self.__password = password


    def login(self, login, password):
        if self.login == login and self.__password == password:
            return print("Ok")
        else:
            return print("Nope")

andatr = BankAccount("andatr", 1000, 1235)

print("Hello world")