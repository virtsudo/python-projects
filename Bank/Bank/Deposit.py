class Deposit:
    __deposits = list()

    def __init__(self, account, acc_date: str, acc_value: int):
        account.set_balance(acc_value)
        account.set_date(acc_date)
        self.__deposits.append([account.get_id(), acc_date, acc_value])

    def get_deposits_info(self):
        return self.__deposits
