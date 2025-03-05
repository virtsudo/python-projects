from Bank.Account import Account
from Bank.Deposit import *
from Bank.Withdrawal import *
from Bank.Errors import *


class Bank:
    __name = ""
    __accounts = dict()

    def __init__(self, bank_name):
        self.account_count = 1
        self.__name = bank_name

    def get_name(self):
        return self.__name

    def get_accounts(self):
        return self.__accounts

    def create_account(self, acc_name, acc_date, acc_deposit):
        account = Account(self.account_count, acc_name, acc_date, acc_deposit)
        self.__accounts[account.get_id()] = account
        self.account_count += 1

    def get_account(self, acc_id: int):
        try:
            return self.__accounts[acc_id]
        except KeyError:
            BankError(1)

    def delete_account(self, acc_id):
        try:
            self.__accounts.pop(acc_id)
        except KeyError:
            BankError(1)

    def deposit(self, acc_id, acc_date, acc_value):
        Deposit(self.get_account(acc_id), acc_date, acc_value)

    def withdrawal(self, acc_id, acc_date, acc_value):
        Withdrawal(self.get_account(acc_id), acc_date, acc_value)

    def transfer(self, acc_id_dep, acc_id_with, acc_date, acc_value):
        Withdrawal(self.get_account(acc_id_with), acc_date, acc_value)
        Deposit(self.get_account(acc_id_dep), acc_date, acc_value)

    def get_total_deposit(self):
        total = 0
        for a in self.__accounts:
            total += a.get_balance()
        return total

    def get_zero_accounts(self):
        result = list()
        for a in self.__accounts:
            if a.get_balance == 0:
                result.append(a)
        return result

    def get_accounts_by_balance(self, b: int, e: int):
        result = list()
        for a in self.__accounts:
            if b <= a.get_balance < e:
                result.append(a)
        return result

    def get_number_higher(self, amount: int):
        result = list()
        for a in self.__accounts:
            if a.get_balance >= amount:
                result.append(a)
        return result


