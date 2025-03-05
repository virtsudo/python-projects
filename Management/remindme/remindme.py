from tkinter import *
from time import *
from os import name

def main():
    if name == 'nt':
        a = Application()
        a.frame()



class Application:
    def __init__(self):
        self.root = None
        self.counter = -1

    def action(self):
        print('<< PROCESS STARTS >>')
        self.root.destroy()
        print("<< WARNING !!! >>")
        i = 10
        while i > 0:
            self.counter = i
            self.warning()
            print("<< COUNTING ... >>")
            sleep(10)
            i -= 1
        print("<< TIME OUT >>\n\n")
        self.frame()

    def frame(self):
        self.root = Tk()
        self.root.config(bg='black')
        self.root.attributes('-fullscreen', True)
        fr1 = Frame(self.root, bd=5, bg='black', height=1, width=1, highlightcolor='white', relief='ridge')
        fr1.pack(padx=10, pady=5, fill='both', expand=True)
        l1 = Label(fr1, text=f'R{chr(9818)}mindM{chr(9818)}', anchor=N, bg='black', fg='green', font='stencil 80')
        l1.pack()
        l2 = Label(fr1, text='Hidden Label', anchor=CENTER, bg='black', fg='black', font='arial 30', height=5)
        l2.pack()
        l4 = Label(fr1, text="Local Time - " + strftime('%H:%M:%S'), anchor=CENTER, bg='black', fg='grey',
                   font='stencil 25')
        l4.pack()
        b1 = Button(fr1, text='Activate', anchor=CENTER, bg='black', fg='green', font='stencil 50', width=10, height=1,
                    command=self.action)
        b1.pack()
        bq = Button(self.root, text='Exit', anchor=CENTER, bg='black', fg='red', font='stencil 20', width=100,
                    command=self.root.destroy)
        bq.pack(side='bottom')
        self.root.mainloop()

    def warning(self):
        warn = Tk()
        warn.title("Warning")
        warn.config(bg="grey")
        warn.geometry(f'210x310+{warn.winfo_screenwidth()-210}+{warn.winfo_screenheight()-310}')
        warn.resizable(False, False)
        fr1 = Frame(warn, bd=5, bg='black', height=1, width=1, highlightcolor='white', relief='ridge')
        fr1.pack(padx=2, pady=2, fill='both', expand=True)
        if self.counter < 4:
            l1 = Label(fr1, text=self.counter, anchor=CENTER, bg='red', fg='grey', font='stencil 120', width=10, height=1)
        else:
            l1 = Label(fr1, text=self.counter, anchor=CENTER, bg='green', fg='grey', font='stencil 120', width=10, height=1)
        l1.pack()
        warn.update()
        b1 = Button(fr1, text="OKAY", anchor=CENTER, bg='black', fg='grey', font='stencil 40', width=10, command=warn.destroy)
        b1.pack(side='bottom')
        warn.mainloop()






def rgb(inp):
    return "#%02x%02x%02x" % inp




if __name__ == '__main__':
    main()
