from tkinter import *
from time import sleep


def main():
    FunTasTic()


class FunTasTic:
    def __init__(self):
        self.frames = []
        self.buttons = {}
        self.fronts = {
            'king': chr(9818),
            'queen': chr(9819),
            'knight': chr(9822),
            'bishop': chr(9821),
            'rook': chr(9820),
            'pawn': chr(9823),
            'empty': ' '
        }
        self.colors = {
            'dark_bg': self.color_gen((55, 55, 55)),
            'light_bg': self.color_gen((205, 205, 205)),
            'black_side': self.color_gen((0, 0, 0)),
            'white_side': self.color_gen((255, 255, 255)),
            'hold_bg': self.color_gen((255, 0, 0))
        }
        self.root = Tk()
        self.root.title("FunTasTic")
        self.root.config(bg=self.color_gen((0, 0, 0)))
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda event: self.root.destroy())

        self.main_frame = Frame(self.root, bg=self.color_gen((0, 0, 0)))
        self.main_frame.pack(fill=BOTH, expand=True, padx=400, pady=0)

        for i in range(8):
            frame = Frame(self.main_frame, bg=self.color_gen((255, 255, 255)))
            frame.pack(fill=BOTH, expand=True)
            self.frames.append(frame)

        self.space_loader()
        self.front_loader()

        try:
            while True:
                self.root.update()
                sleep(0.0001)
        except KeyboardInterrupt:
            pass

    def color_gen(self, inp):
        self.frames = self.frames
        return "#%02x%02x%02x" % inp

    def front_loader(self):
        self.front_updater('8A', 'rook', side='black_side')
        self.front_updater('8B', 'knight', side='black_side')
        self.front_updater('8C', 'bishop', side='black_side')
        self.front_updater('8D', 'queen', side='black_side')
        self.front_updater('8E', 'king', side='black_side')
        self.front_updater('8F', 'bishop', side='black_side')
        self.front_updater('8G', 'knight', side='black_side')
        self.front_updater('8H', 'rook', side='black_side')

        self.front_updater('1A', 'rook', side='white_side')
        self.front_updater('1B', 'knight', side='white_side')
        self.front_updater('1C', 'bishop', side='white_side')
        self.front_updater('1D', 'queen', side='white_side')
        self.front_updater('1E', 'king', side='white_side')
        self.front_updater('1F', 'bishop', side='white_side')
        self.front_updater('1G', 'knight', side='white_side')
        self.front_updater('1H', 'rook', side='white_side')

        for i in range(ord('A'), ord('I')):
            self.front_updater(f'7{chr(i)}', 'pawn', side='black_side')
        for i in range(ord('A'), ord('I')):
            self.front_updater(f'2{chr(i)}', 'pawn', side='white_side')

    def space_loader(self):
        for i in range(len(self.frames)):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.button_creator(self.frames[i], position=f"{8-i}{chr(j+65)}", dark=True)
                    else:
                        self.button_creator(self.frames[i], position=f"{8-i}{chr(j+65)}", dark=False)
                else:
                    if j % 2 == 0:
                        self.button_creator(self.frames[i], position=f"{8-i}{chr(j+65)}", dark=False)
                    else:
                        self.button_creator(self.frames[i], position=f"{8-i}{chr(j+65)}", dark=True)

    def button_creator(self, root, position, dark=True):
        if dark:
            button = Button(root, text="", bg=self.colors['dark_bg'], font="arial 80")
        else:
            button = Button(root, text="", bg=self.colors['light_bg'], font="arial 80")
        button.pack(side=LEFT, fill=BOTH, expand=True)
        self.buttons[position] = button

    def front_updater(self, pos, front, side='black_side'):
        self.buttons[pos]['text'] = self.fronts[front]
        self.buttons[pos]['fg'] = self.colors[side]


if __name__ == '__main__':
    main()
