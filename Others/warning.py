from tkinter import *
from time import sleep
from threading import Thread
from os import name


class Main:
    def __init__(self):
        self.mode = False

    def main(self):
        self.mode = True
        BackPack()


class BackPack:
    def __init__(self):
        Thread(target=Front).start()
        Thread(target=Background).start()


class Front:
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

        self.frame1 = Frame(self.root, bg="black")
        self.frame1.pack(pady=0, padx=0, fill='both', expand=True)

        self.frame2 = Frame(self.root, bg="black")
        self.uno = Label(self.frame2, text="", bg="black")
        self.uno.pack(side='left', fill='both',expand=True)
        self.uno = Label(self.frame2, text="", bg="white")
        self.uno.pack(side='left', fill='both', expand=True)
        self.uno = Label(self.frame2, text="", bg="grey")
        self.uno.pack(side='left', fill='both', expand=True)

        #self.frame2.pack(padx=0, pady=0, fill='both', expand=True)



        self.label = Label(self.frame1, text=f"Warning", bg="black", fg="red", font="stencil 90")
        self.label.pack(padx=0, pady=0, expand=True, fill="both")

        while True:
            self.root.update()
            sleep(0.125)
            self.label['fg'] = "black"
            self.label['font'] = f"stencil {int(self.label['font'][8:])+10}"
            #self.frame2.pack_forget()
            #self.frame1.pack(pady=0, padx=0, fill='both', expand=True)
            self.root.update()
            sleep(0.125)
            self.label['fg'] = "red"
            self.root.update()
            sleep(0.125)
            #self.frame1.pack_forget()
            #self.frame2.pack(padx=0, pady=0, fill='both', expand=True)


class Background:
    def __init__(self):
        self.root = Tk()
        self.root.title("B")
        self.root.attributes('-fullscreen', True)
        self.root.overrideredirect('True')
        self.root.config(bg='black')
        self.root.attributes('-alpha', 0.35)
        self.root.lift()
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-disabled", True)

        self.root.mainloop()


if __name__ == '__main__':
    if name == 'nt':
        Main().main()

