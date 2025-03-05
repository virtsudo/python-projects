from tkinter import *
from time import strftime, sleep
from random import randint
from os import name



class Main:
    def __init__(self):
        self.mode = False

    def main(self):
        self.mode = True
        Emit()



class Emit:
    def __init__(self):
        self.root = Tk()
        self.root.title("F")
        self.root.attributes('-fullscreen', True)
        self.root.overrideredirect('True')
        self.root.config(bg='black')
        self.root.lift()
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "black")

        self.label = Label(self.root, text=f"{strftime('%H:%M:%S')}", bg="black", fg="black", font="stencil 50")
        self.label.place(x=1250, y=790)  # x_max = 1400 y_max = 790

        while True:
            self.root.update()
            sleep(1/randint(1, 1000))
            self.label['text'] = f"{strftime('%H:%M:%S')}"
            self.label.place(x=randint(0, 1250), y=randint(0, 790))
            self.label['fg'] = rgb((randint(0, 255), randint(0, 255), randint(0, 255)))
            #self.label['font'] = f"stencil {int(self.label['font'][8:])+1}"



def rgb(inp):
    return "#%02x%02x%02x" % inp

if __name__ == '__main__':
    if name == 'nt':
        try:
            Main().main()
        except KeyboardInterrupt:
            pass
