from tkinter import *
from time import sleep
from random import randint


def main():
    Marshall()


class Marshall:
    def __init__(self):
        self.mode = True
        self.root = Tk()
        self.coord = [self.root.winfo_screenwidth(), self.root.winfo_screenheight()]
        print(self.coord)
        self.set_cord1 = [0, 1000, 0, 0]  # w, h, ow, oh
        self.set_cord2 = [1400, 0, 0, 0]  # w, h, ow, oh
        self.set_cord3 = [1400, 0, 1400, 0]  # w, h, ow, oh
        self.set_cord4 = [0, 700, 0, 1000]  # w, h, ow, oh
        self.input = StringVar()
        self.root.title('marshall')
        self.root.config(bg=self.color_gen((0, 0, 0)))
        self.root.wait_visibility(self.root)
        self.root.wm_attributes('-alpha', 0.1)
        self.root.wm_attributes('-fullscreen', True)
        self.root.bind('<Escape>', lambda event: self.root.destroy())

        self.top_root1 = Toplevel(self.root)
        self.top_root1.geometry(f'{self.coord[0]-self.set_cord1[0]}x{self.coord[1]-self.set_cord1[1]}+{self.set_cord1[2]}+{self.set_cord1[3]}')
        self.top_root1.overrideredirect('True')
        self.top_root1.config(bg='black')
        self.top_root1.config(relief='ridge')

        self.top_root2 = Toplevel(self.root)
        self.top_root2.geometry(f'{self.coord[0]-self.set_cord2[0]}x{self.coord[1]-self.set_cord2[1]}+{self.set_cord2[2]}+{self.set_cord2[3]}')
        self.top_root2.overrideredirect('True')
        self.top_root2.config(bg='black')
        self.top_root2.config(relief='ridge')

        self.top_root3 = Toplevel(self.root)
        self.top_root3.geometry(f'{self.coord[0]-self.set_cord3[0]}x{self.coord[1]-self.set_cord3[1]}+{self.set_cord3[2]}+{self.set_cord3[3]}')
        self.top_root3.overrideredirect('True')
        self.top_root3.config(bg='black')
        self.top_root3.config(relief='ridge')

        self.top_root4 = Toplevel(self.root)
        self.top_root4.geometry(f'{self.coord[0]-self.set_cord4[0]}x{self.coord[1]-self.set_cord4[1]}+{self.set_cord4[2]}+{self.set_cord4[3]}')
        self.top_root4.overrideredirect('True')
        self.top_root4.config(bg='black')
        self.top_root4.config(relief='ridge')

        while True:
            self.root.update()
            sleep(0.2)
            self.top_root1.config(bg=self.color_gen((randint(0, 255), randint(0, 255), randint(0, 255))))
            self.top_root2.config(bg=self.color_gen((randint(0, 255), randint(0, 255), randint(0, 255))))
            self.top_root3.config(bg=self.color_gen((randint(0, 255), randint(0, 255), randint(0, 255))))
            self.top_root4.config(bg=self.color_gen((randint(0, 255), randint(0, 255), randint(0, 255))))

            self.set_cord1 = [0, randint(0, (self.coord[1])), 0, 0]  # w, h, ow, oh
            self.set_cord2 = [randint(0, (self.coord[0])), 0, 0, 0]  # w, h, ow, oh
            self.set_cord3 = [randint(0, (self.coord[0])), 0, randint(0, int(self.coord[0]/2)), 0]  # w, h, ow, oh
            self.set_cord4 = [0, randint(0, (self.coord[1])), 0, randint(0, int(self.coord[1]/2))]  # w, h, ow, oh

            self.top_root1.geometry(
                f'{self.coord[0] - self.set_cord1[0]}x{self.coord[1] - self.set_cord1[1]}+{self.set_cord1[2]}+{self.set_cord1[3]}')
            self.top_root2.geometry(
                f'{self.coord[0] - self.set_cord2[0]}x{self.coord[1] - self.set_cord2[1]}+{self.set_cord2[2]}+{self.set_cord2[3]}')
            self.top_root3.geometry(
                f'{self.coord[0] - self.set_cord3[0]}x{self.coord[1] - self.set_cord3[1]}+{self.set_cord3[2]}+{self.set_cord3[3]}')
            self.top_root4.geometry(
                f'{self.coord[0] - self.set_cord4[0]}x{self.coord[1] - self.set_cord4[1]}+{self.set_cord4[2]}+{self.set_cord4[3]}')

    def color_gen(self, rgb):
        self.mode = self.mode
        return "#%02x%02x%02x" % rgb


if __name__ == '__main__':
    main()
