from tkinter import *
from time import sleep
from random import randint


def main():
    win()


def win():
    count, count1, count2 = 0, 0, 0
    flag, flag1, flag2 = False, False, False
    root = Tk()
    root.title("D'Era")
    root.config(bg='black')
    root.wait_visibility(root)
    root.wm_attributes('-fullscreen', True)
    root.wm_attributes('-topmost', True)
    root.attributes('-alpha', 1.0)
    root.bind('<Escape>', lambda event: root.destroy())

    while True:
        root.config(bg=rgb((count, count1, count2)))
        root.update()
        sleep(0.01)
        if count == 0: flag = False
        elif count == 255: flag = True
        if count1 == 0: flag1 = False
        elif count1 == 255: flag1 = True
        if count2 == 0: flag2 = False
        elif count2 == 255: flag2 = True
        if flag: count -= randint(0, 1)
        elif flag is False: count += randint(0, 1)
        if flag1: count1 -= randint(0, 1)
        elif flag1 is False: count1 += randint(0, 1)
        if flag2: count2 -= randint(0, 1)
        elif flag2 is False: count2 += randint(0, 1)


def rgb(inp):
    return "#%02x%02x%02x" % inp


if __name__ == '__main__':
    main()
