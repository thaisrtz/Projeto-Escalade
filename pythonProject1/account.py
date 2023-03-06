
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

    def can_withdraw(self, withdrawal_amount):
        available = self.__balance + self.__limit
        return withdrawal_amount <= available

    def withdraw(self, value):
        if(self.can_withdraw(value)):
            self.__balance -= value
        else:
            print("O valor ultrapassa o limite de sua conta.")

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def banks():
        return {"Banco do Brasil": "001", "Caixa": "104", "Bradesco": "237"}