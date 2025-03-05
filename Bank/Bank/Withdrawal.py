class Withdrawal:
    __withdrawals = list()

    def __init__(self, account, acc_date: str, acc_value: int):
        account.set_balance((acc_value-2*acc_value))
        account.set_date(acc_date)
        self.__withdrawals.append([account.get_id(), acc_date, acc_value])

    def get_withdrawals_info(self):
        return self.__withdrawals
