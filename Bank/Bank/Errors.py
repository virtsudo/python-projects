from tkinter import messagebox


class BankError:
    def __init__(self, mode: int):
        match mode:
            case 1:
                messagebox.showerror('System', 'Account not exists')
                raise RuntimeError("NotExistsAccountError")
            case 2:
                messagebox.showerror('System', 'Not enough money in your balance')
                raise RuntimeError("NotEnoughBalanceError")
            case 3:
                messagebox.showerror('System', 'Past time')
                raise RuntimeError("PastTimeError")
            case 4:
                messagebox.showerror('System', 'Invalid value')
                raise RuntimeError('InvalidValueError')
