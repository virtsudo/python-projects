from time import sleep
from random import choice, randint
from tkinter import *

color = ["black", "grey", "white"]
root = None


def main():
    win()




def win():
    global root
    speed = 1
    siz = 12
    root = Tk()
    root.attributes('-fullscreen', True)
    root.config(bg="black")
    root.bind('<Escape>', quitt)
    label = Label(root, text=chr(9818), bg=choice(color), fg=rgb((randint(00, 255), randint(00, 255), randint(00, 255))), font="stencil 50")
    label.pack(padx=1, pady=1, fill='both', expand=True)
    while True:
        root.update()
        label['bg'] = choice(color)
        label['fg'] = rgb((randint(00, 255), randint(00, 255), randint(00, 255)))
        if int(label['font'][8:]) < 2500:
            label['font'] = f" stencil {int(label['font'][8:])+10}"
        else:
            label['font'] = f" stencil {int(label['font'][8:])-4000}"
        siz += 2
        sleep(speed)
        speed = speed * 0.1



def quitt(event):
    global root
    root.destroy()


def rgb(inp):
    return "#%02x%02x%02x" % inp
    





if __name__ == '__main__':
    main()
