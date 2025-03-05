from time import sleep
from random import choice
from tkinter import *


my_mood = ['bene', 'male']
root = None


def main():
    win()


def win():
    global root
    speed = 1
    root = Tk()
    root.attributes('-fullscreen', True)
    root.config(bg="black")
    root.bind('<Escape>', quitt)
    label = Label(root, text=choice(my_mood), bg="black", fg="red", font="stencil 50")
    label.pack(padx=1, pady=1, fill='both', expand=True)
    while True:
        root.update()
        label['text'] = choice(my_mood)
        if int(label['font'][8:]) < 4000:
            label['font'] = f" stencil {int(label['font'][8:])+10}"
        else:
            label['font'] = f" stencil {int(label['font'][8:])-4000}"
        sleep(speed)
        speed = speed * 0.1



def quitt(event):
    global root
    root.destroy()
    





if __name__ == '__main__':
    main()
