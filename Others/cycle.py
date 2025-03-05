from tkinter import *
from time import sleep
from random import randint


def main():
    App()


class App:
    def __init__(self):
        self.mode = True
        self.frames = list()
        self.delta = 10
        self.temp = 0
        self.root = Tk()
        self.coord = [self.root.winfo_screenwidth(), self.root.winfo_screenheight()]
        self.root.title('App')
        self.root.config(bg=self.color_gen((0, 0, 0)))
        self.root.wait_visibility(self.root)
        self.root.wm_attributes('-alpha', 1.0)
        self.root.wm_attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda event: self.root.destroy())

        self.temp = randint(0, 255)
        f = Frame(self.root, bg=self.color_gen((self.temp, self.temp, self.temp)))
        f.pack(padx=self.delta, pady=self.delta, fill=BOTH, expand=True)
        self.frames.append(f)
        for i in range(60):
            self.temp = randint(0, 255)
            f = Frame(self.frames[len(self.frames)-1], bg=self.color_gen((self.temp, self.temp, self.temp)))
            f.pack(padx=self.delta, pady=self.delta, fill=BOTH, expand=True)
            self.frames.append(f)

        while True:
            self.root.update()
            sleep(0.1)
            self.temp = randint(0, 255)
            self.frames[randint(0, len(self.frames)-1)]['bg'] = self.color_gen((self.temp, self.temp, self.temp))

    def color_gen(self, rgb):
        self.mode = self.mode
        return "#%02x%02x%02x" % rgb


if __name__ == '__main__':
    main()


"""

V2

class App:
    def __init__(self):
        self.mode = True
        self.frames = list()
        self.delta = 10
        self.temp = 0
        self.root = Tk()
        self.coord = [self.root.winfo_screenwidth(), self.root.winfo_screenheight()]
        self.root.title('App')
        self.root.config(bg=self.color_gen((0, 0, 0)))
        self.root.wait_visibility(self.root)
        self.root.wm_attributes('-alpha', 1.0)
        self.root.wm_attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda event: self.root.destroy())

        self.temp = randint(0, 255)
        f = Frame(self.root, bg=self.color_gen((self.temp, self.temp, self.temp)))
        f.pack(padx=self.delta, pady=self.delta, fill=BOTH, expand=True)
        self.frames.append(f)
        #self.delta += 10
        for i in range(60):
            self.temp = randint(0, 255)
            f = Frame(self.frames[len(self.frames)-1], bg=self.color_gen((self.temp, self.temp, self.temp)))
            f.pack(padx=self.delta, pady=self.delta, fill=BOTH, expand=True)
            self.frames.append(f)
            #self.delta += 10

        while True:
            self.temp = randint(0, 255)
            for i in range(len(self.frames)):
                self.frames[i]['bg'] = self.color_gen((self.temp, self.temp, self.temp))
                self.temp = self.temp+5 if self.temp < 255 else 0
                sleep(0.01)
                self.root.update()

    def color_gen(self, rgb):
        self.mode = self.mode
        return "#%02x%02x%02x" % rgb
       
V3       
        
class App:
    def __init__(self):
        self.mode = True
        self.frames = list()
        self.delta = 10
        self.temp = 0
        self.root = Tk()
        self.coord = [self.root.winfo_screenwidth(), self.root.winfo_screenheight()]
        self.root.title('App')
        self.root.config(bg=self.color_gen((0, 0, 0)))
        self.root.wait_visibility(self.root)
        self.root.wm_attributes('-alpha', 1.0)
        self.root.wm_attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda event: self.root.destroy())

        self.temp = randint(0, 255)
        f = Frame(self.root, bg=self.color_gen((self.temp, self.temp, self.temp)))
        f.pack(padx=self.delta, pady=self.delta, fill=BOTH, expand=True)
        self.frames.append(f)
        for i in range(60):
            self.temp = randint(0, 255)
            f = Frame(self.frames[len(self.frames)-1], bg=self.color_gen((self.temp, self.temp, self.temp)))
            f.pack(padx=self.delta, pady=self.delta, fill=BOTH, expand=True)
            self.frames.append(f)

        while True:
            try:
                self.temp = randint(0, 255)
                temp = [(self.temp, self.temp, self.temp), (self.temp, 0, 0), (self.temp, self.temp, 0), (0, self.temp, self.temp)]
                temp1 = randint(0, 3)
                for i in range(len(self.frames)):
                    temp = [(self.temp, self.temp, self.temp), (self.temp, 0, 0), (self.temp, self.temp, 0),
                            (0, self.temp, self.temp)]
                    self.frames[i]['bg'] = self.color_gen(temp[temp1])
                    self.temp = self.temp + 5 if self.temp < 255 else 0
                    sleep(0.005)
                    self.root.update()
            except _tkinter.TclError as e:
                continue

    def color_gen(self, rgb):
        self.mode = self.mode
        return "#%02x%02x%02x" % rgb

"""
