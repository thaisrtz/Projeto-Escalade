
class Account:

    def __init__(self, number, holder, balance, limit):
        print("Contruindo objeto... {}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        print("Saldo de {} do titular {}".format(self.__balance, self.__holder))

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)