from psutil import sensors_battery as battery
from tkinter import *
from _tkinter import TclError
from time import sleep, strftime
from threading import Thread
import pyautogui
from winsound import Beep  # freq = 37 - 32,767 | in milliseconds
from os import name

# runas /user:(UserNameHere) CMD.exe

win_root = None

def main():
    volume_up()

class SecureScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Secure Screen")
        self.root.config(bg="Black")
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.6)

        self.title_label = Label(self.root, text="secure screen", anchor=CENTER, bg='black', fg=rgb((200, 255, 0)), font='stencil 60')
        self.title_label.pack()

        self.main_frame = Frame(self.root, bg='black', bd=5, height=1, width=1, highlightcolor='white', relief='ridge')
        self.main_frame.pack(padx=1, pady=1, fill='both', expand=True)

        self.battery_label = Label(self.main_frame, text=battery_state(), anchor=CENTER, bg='black', fg=rgb((155, 255, 10)), font='stencil 80')
        self.battery_label.pack(pady=1, padx=1, fill='x', expand=True)

        self.quit_button = Button(self.root, text='exit', anchor=CENTER, bg='black', fg='red', font='stencil 20', command=self.root.destroy)
        self.quit_button.pack(side='bottom', padx=1, fill='x')

        try:
            while True:
                self.root.update()
                self.battery_label['text'] = battery_state()
        except TclError:
            print("Program exited by admin")
            pass

def battery_state():
    if battery().power_plugged is True:
        return "Plugged In"
    else:
        return "On Battery"

def check_battery_state():
    if battery().power_plugged is True:
        return "Ready"
    else:
        return "First Plugged YOUR\nDEVICE In!"

def win():
    global win_root
    win_root = Tk()
    win_root.title("Secure Screen")
    win_root.config(bg="black")
    win_root.geometry("400x500+750+300")
    win_root.resizable(width=False, height=False)
    win_root.overrideredirect(True)

    main_frame = Frame(win_root, bd=1, bg='grey', height=1, width=1, highlightcolor='black', relief='ridge')
    main_frame.pack(padx=2, pady=2, fill='both', expand=True)

    title_label = Label(main_frame, text="secure screen", anchor=CENTER, bg='grey', fg=rgb((200, 255, 0)), font='stencil 30')
    title_label.pack()

    main_label = Label(main_frame, text=check_battery_state(), bg=rgb((200, 200, 200)), fg="red", font="Arial 20 bold", anchor=CENTER)
    main_label.pack(padx=1, pady=1, fill="both", expand=True)
    if battery().power_plugged:
        active_button = Button(win_root, text="ACTIVATE", bg="grey", fg="green", font="arial 20", anchor=CENTER, command=func)
    else:
        active_button = Button(win_root, text="ACTIVATE", bg="grey", fg="green", font="arial 20", anchor=CENTER, command=func, state=DISABLED)
    active_button.pack(pady=1, padx=1, fill='x')

    quit_button = Button(win_root, text="EXIT", bg="grey", fg="red", font="arial 20", anchor=CENTER, command=win_root.destroy)
    quit_button.pack(pady=1, padx=1, fill='x')

    win_root.mainloop()


def func():
    win_root.destroy()
    while battery().power_plugged:
        continue
    else:
        proc1 = Thread(target=SecureScreen)
        proc2 = Thread(target=volume_up)
        proc1.start()
        proc2.start()

def volume_up():
    pyautogui.PAUSE = 0.01
    for i in range(50):
        pyautogui.press('volumeup')
    while True:
        Beep(4000, 125)  # freq = 37 - 32,767 | in milliseconds
        sleep(0.125)

def rgb(inp):
    return "#%02x%02x%02x" % inp


if __name__ == '__main__':
    if name == 'nt':
        main()
