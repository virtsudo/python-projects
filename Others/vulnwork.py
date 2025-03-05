import pyautogui as gmod
import ctypes as cmod
from time import sleep
import os
import sys


def main():
    run_as_admin()


def run_as_admin():
    if cmod.windll.shell32.IsUserAnAdmin():
        key_locker()
        sleep(2)
        key_unlocker()
        return
    script_path = os.path.abspath(__file__)
    try:
        cmod.windll.shell32.ShellExecuteW(
            None,
            'runas',
            sys.executable,
            script_path,
            None,
            1
        )
    except Exception as e:
        print(f'Error: {e}')


def key_locker():
    return cmod.windll.user32.BlockInput(True)


def key_unlocker():
    return cmod.windll.user32.BlockInput(False)


if __name__ == '__main__':
    if os.name == 'nt':
        main()


