from Bank.Errors import *
from datetime import datetime


class Account:
    __id = -1
    __name = ""
    __date = datetime.now()
    __balance = 0.0

    def __init__(self, acc_id: int, acc_name: str, acc_date: datetime, acc_value: float):
        self.__id = acc_id
        self.__name = acc_name
        self.__date = acc_date
        self.__balance += acc_value

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def set_date(self, new_date):
        if new_date > self.__date:
            self.__date = new_date
        else:
            BankError(3)

    def get_balance(self):
        return self.__balance

    def set_balance(self, value: int):
        if value > 0 or self.__balance > abs(value):
            self.__balance += value
        else:
            BankError(2)

    def list_account(self):
        return [self.get_name(), self.get_date(), self.get_balance()]

