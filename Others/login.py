from tkinter import *
from time import sleep


def main():
    Marshall()


class Marshall:
    def __init__(self):
        self.mode = True
        self.root = Tk()
        self.coord = [self.root.winfo_screenwidth(), self.root.winfo_screenheight()]
        self.input = StringVar()
        self.root.title('marshall')
        self.root.config(bg=self.color_gen((0, 0, 0)))
        self.root.wait_visibility(self.root)
        self.root.wm_attributes('-alpha', 0.5)
        self.root.wm_attributes('-fullscreen', True)
        self.root.wm_attributes('-topmost', True)
        self.root.bind('<Escape>', lambda event: self.root.destroy())

        self.top_root = Toplevel(self.root)
        self.top_root.geometry(f'{self.coord[0] - 1400}x{self.coord[1] - 700}+700+350')
        self.top_root.overrideredirect('True')
        self.top_root.resizable(width=False, height=False)
        self.top_root.config(bg=self.color_gen((100, 100, 100)))
        self.top_root.config(relief='ridge')

        self.label = Label(self.top_root, text='Login', bg=self.color_gen((100, 100, 100)),
                           fg=self.color_gen((200, 200, 200)), font='stencil 40')
        self.label.pack(fill='x', pady=30)

        self.entry = Entry(self.top_root, textvariable=self.input, bg=self.color_gen((125, 125, 125)),
                           fg=self.color_gen((50, 50, 50)), insertbackground=self.color_gen((50, 50, 50)),
                           font='stencil 40', borderwidth=0, validate='key', width=7,
                           validatecommand=(self.root.register(lambda text: self.validator(text)), "%P"),
                           show='*', justify=CENTER)
        self.entry.bind('<Escape>', lambda event: self.root.destroy())
        self.root.bind('<Enter>', lambda event: self.on_focus())
        self.entry.pack(padx=10, pady=10)

        self.info = Label(self.top_root, text='password is wrong', bg=self.color_gen((100, 100, 100)),
                          fg=self.color_gen((200, 0, 0)), font='stencil 15')

        self.button = Button(self.top_root, text='Submit', bg=self.color_gen((100, 100, 100)),
                             fg=self.color_gen((200, 200, 200)), font='stencil 40',
                             activebackground=self.color_gen((200, 0, 0)),
                             activeforeground=self.color_gen((0, 0, 0)),
                             command=lambda: self.log_check(self.input),
                             disabledforeground=self.color_gen((10, 10, 10)))
        self.button.pack(padx=20, pady=20, fill='x')

        while True:
            if self.mode:
                self.root.update()
                sleep(0.0001)
                if len(self.input.get()) > 8: self.input.set(self.input.get()[:7])

    def validator(self, text):
        self.mode = self.mode
        if len(text) == 0 or len(text) <= 8:
            return True
        return False

    def on_focus(self):
        if len(self.input.get()) > 0:
            self.log_check(self.input)

    def log_check(self, password):
        if str(password.get()) == 'password':
            self.root.destroy()

        else:
            self.mode = False
            self.button['state'] = DISABLED
            self.info.pack()
            self.root.update()
            sleep(0.5)
            self.info.pack_forget()
            self.button['state'] = NORMAL
            self.mode = True
            self.input.set('')

    def color_gen(self, rgb):
        self.mode = self.mode
        return "#%02x%02x%02x" % rgb


if __name__ == '__main__':
    main()
