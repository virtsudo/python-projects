from tkinter import *
from time import sleep
from random import randint


def main():
    UndTee()


class UndTee:
    def __init__(self):
        self.mode = True
        self.root = Tk()
        self.delay1 = 0.1
        self.x, self.y = True, True
        self.screen = [self.root.winfo_screenwidth()-170, self.root.winfo_screenheight()-70]
        self.coords = (170, 70)
        self.root.title('UndTee')
        self.root.config(bg=self.color_gen((0, 0, 0)))
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', lambda event: self.root.destroy())
        self.root.bind('<Up>', lambda event: self.fast())
        self.root.bind('<Down>', lambda event: self.slow())

        self.label = Label(self.root, text='DVD',
                           fg=self.color_gen((255, 255, 255)),
                           font='arial 120',
                           bg=self.color_gen((0, 0, 0)))
        self.label.place(x=self.coords[0], y=self.coords[1], anchor=CENTER)

        while True:
            sleep(self.delay1)
            self.set_motion()

    def fast(self):
        if self.delay1 > 1/10**10:
            self.delay1 = self.delay1 / 10

    def slow(self):
        if self.delay1 < 1:
            self.delay1 = self.delay1 * 10

    def color_rand(self):
        self.mode = self.mode
        self.root.update()
        self.label['fg'] = self.color_gen((randint(0, 255), randint(0, 255), randint(0, 255)))

    def set_motion(self):
        self.mode = self.mode
        self.root.update()
        self.set_mode_x()
        self.set_mode_y()
        if self.x:
            self.add_x()
        else:
            self.min_x()
        if self.y:
            self.add_y()
        else:
            self.min_y()

    def set_mode_x(self):
        if int(self.label.place_info()['x']) == self.coords[0]:
            self.color_rand()
            self.x = True
        elif int(self.label.place_info()['x']) == self.screen[0]:
            self.color_rand()
            self.x = False

    def set_mode_y(self):
        if int(self.label.place_info()['y']) == self.coords[1]:
            self.color_rand()
            self.y = True
        elif int(self.label.place_info()['y']) == self.screen[1]:
            self.color_rand()
            self.y = False

    def add_x(self):
        self.label.place(x=int(self.label.place_info()['x']) + 1, y=int(self.label.place_info()['y']), anchor=CENTER)

    def add_y(self):
        self.label.place(x=int(self.label.place_info()['x']), y=int(self.label.place_info()['y']) + 1, anchor=CENTER)

    def min_x(self):
        self.label.place(x=int(self.label.place_info()['x']) - 1, y=int(self.label.place_info()['y']), anchor=CENTER)

    def min_y(self):
        self.label.place(x=int(self.label.place_info()['x']), y=int(self.label.place_info()['y']) - 1, anchor=CENTER)

    def color_gen(self, rgb):
        self.mode = self.mode
        return "#%02x%02x%02x" % rgb


if __name__ == '__main__':
    main()
