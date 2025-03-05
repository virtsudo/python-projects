from tkinter import *
from time import sleep
from random import randint, choice


def main():
    App()


class App:
    def __init__(self):
        self.cells = []
        self.mode = 0
        self.size = 6
        self.root = Tk()
        self.root.title("Binary")
        self.root.config(bg=self.color_gen((0, 0, 0)))
        self.root.wait_visibility(self.root)
        self.root.wm_attributes("-fullscreen", True)
        self.root.bind('<Escape>', lambda event: self.root.destroy())
        self.root.update()

        for i in range(9 * self.size):
            self.cells.append([])
            for j in range(16 * self.size):
                if True:
                    f = Frame(self.root,
                              bg=self.color_gen((randint(0, 255),
                                                 randint(0, 255),
                                                 randint(0, 255))),
                              width=120 // self.size, height=120 // self.size)
                    f.grid(row=i, column=j, padx=0, pady=0)
                    self.cells[i].append(f)
                else:
                    f = Frame(self.root,
                              bg=self.color_gen((0, 0, 0)),
                              width=120 // self.size, height=120 // self.size)
                    f.grid(row=i, column=j, padx=0, pady=0)
                    self.cells[i].append(f)

        self.root.update()

        while True:
            self.root.update()
            sleep(1/1000)
            for i in range(len(self.cells)):
                for j in range(len(self.cells[i])):
                    if True:
                        self.cells[i][j]['bg'] = self.color_gen((randint(0, 255),
                                                                 randint(0, 255),
                                                                 randint(0, 255)))
                    else:
                        self.cells[i][j]['bg'] = self.color_gen((0, 0, 0))

    def color_gen(self, rgb):
        self.mode = self.mode
        return "#%02x%02x%02x" % rgb


if __name__ == '__main__':
    main()

"""
V2

class E:
    def __init__(self):
        self.mode = 0
        self.frames = []
        self.root = Tk()
        self.root.title("U")
        self.root.config(bg=self.color_gen((0, 0, 0)))
        self.root.wait_visibility(self.root)
        self.root.wm_attributes('-fullscreen', True)
        self.root.bind('<Escape>', lambda event: self.root.destroy())

        for i in range(500):
            f = Frame(self.root, bg=self.color_gen((0, 0, 0)))
            f.pack(side=TOP, fill=BOTH, expand=True)
            self.frames.append(f)

        while True:
            self.root.update()
            sleep(0.0000001)
            if self.mode < 500:
                c = self.color_gen((randint(0, 255), randint(0, 255), randint(0, 255)))
                self.frames[self.mode]['bg'] = c
                self.mode += 1
            else:
                self.mode = 0

    def color_gen(self, rgb):
        self.mode = self.mode
        return "#%02x%02x%02x" % rgb

"""
