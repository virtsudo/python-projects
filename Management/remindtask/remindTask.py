from tkinter import *
from time import *
from os import name
from tkinter import messagebox


def main():
    if name == 'nt':
        a = Application()
        a.frame()


class Application:
    def __init__(self):
        self.root = None
        self.task_list = list()
        self.task_time = None
        self.time_const = [None, None, None, None]
        self.temp = None
        self.task = None
        self.task_label = None
        self.time_mode = False

    def action(self):
        if self.time_mode is False:
            messagebox.showerror("Error", "Set Task's Time!!!")
            return
        elif self.task_time < 300 * (len(self.task_list) - 1):
            messagebox.showwarning("Warning", "Impossible Task Period!!!")
            self.root.destroy()
            self.frame()
            return
        elif len(self.task_list) < 2:
            messagebox.showwarning("Warning", "Minimum 2 Tasks!!!")
            self.root.destroy()
            self.frame()
            return
        else:
            self.root.destroy()
        for i in self.task_list:
            self.task = word_completer(i)
            tm = [(((self.task_time - 300 * (len(self.task_list) - 1)) // len(self.task_list)) // 3600),
                  ((((self.task_time - 300 * (len(self.task_list) - 1)) // len(self.task_list)) % 3600) // 60),
                  ((((self.task_time - 300 * (len(self.task_list) - 1)) // len(self.task_list)) % 3600) % 60)]
            self.warning(tm)
            sleep((self.task_time - 300 * ((len(self.task_list)) - 1)) / len(self.task_list))
            break_window()
            sleep(300)
        self.frame()

    def frame(self):
        self.root = Tk()
        self.root.config(bg='black')
        self.root.attributes('-fullscreen', True)
        title = Label(self.root, text="REMIND TASK", anchor=CENTER, bg='black', fg=rgb((180, 150, 207)),
                      font='stencil 60 underline')
        title.pack(side='top')
        self.task_time = [StringVar(), StringVar(), StringVar()]
        self.temp = StringVar()
        fr0 = Frame(self.root, bd=5, bg='black', height=1, width=1, highlightcolor='white', relief='ridge')
        fr0.pack(padx=10, pady=5, fill='both', expand=True)

        fr1 = Frame(fr0, bd=5, bg='black', height=1, width=1, highlightcolor='white', relief='ridge')
        fr1.pack(padx=10, pady=10, fill='both', expand=True, side='left')

        fr2 = Frame(fr0, bd=5, bg='black', height=1, width=1, highlightcolor='white', relief='ridge')
        fr2.pack(padx=10, pady=10, fill='both', expand=True, side='right')

        fr21 = Frame(fr2, bd=5, bg='black', height=1, width=1, highlightcolor='white', relief='ridge')
        fr21.pack(padx=10, pady=10, fill='both', expand=True, side='top')

        fr22 = Frame(fr2, bd=5, bg='black', height=1, width=1, highlightcolor='white', relief='ridge')
        fr22.pack(padx=10, pady=10, fill='both', expand=True, side='top')

        fr23 = Frame(fr2, bd=5, bg='black', height=1, width=1, highlightcolor='white', relief='ridge')
        fr23.pack(padx=10, pady=10, fill='both', expand=True, side='top')

        time_label = Label(fr21, text="Tasks' Total Time", anchor=CENTER, bg='black', fg=rgb((180, 150, 207)),
                           font='stencil 40')
        time_label.pack(side='top', padx=10, pady=10)

        fr211 = Frame(fr21, bg='black')
        fr211.pack()

        self.time_const[0] = Entry(fr211, textvariable=self.task_time[0], bg='grey', fg='black', font='stencil 20',
                                   width=3)
        self.time_const[0].grid(column=0, row=0)
        self.time_const[0].focus()

        time_entry_hour_label = Label(fr211, text="H", anchor=CENTER, bg='black', fg='grey',
                                      font='stencil 20')
        time_entry_hour_label.grid(column=1, row=0, padx=10)

        self.time_const[1] = Entry(fr211, textvariable=self.task_time[1], bg='grey', fg='black', font='stencil 20',
                                   width=3)
        self.time_const[1].grid(column=2, row=0)
        self.time_const[1].focus()

        time_entry_minute_label = Label(fr211, text="M", anchor=CENTER, bg='black', fg='grey',
                                        font='stencil 20')
        time_entry_minute_label.grid(column=3, row=0, padx=10)

        self.time_const[2] = Entry(fr211, textvariable=self.task_time[2], bg='grey', fg='black', font='stencil 20',
                                   width=3)
        self.time_const[2].grid(column=4, row=0)
        self.time_const[2].focus()

        time_entry_second_label = Label(fr211, text="S", anchor=CENTER, bg='black', fg='grey',
                                        font='stencil 20')
        time_entry_second_label.grid(column=5, row=0, padx=10)

        self.time_const[3] = Button(fr21, text="submit", anchor=CENTER, bg='black', fg=rgb((180, 150, 207)),
                                    font='stencil 25', command=self.set_time)
        self.time_const[3].pack(pady=10, padx=10, fill='x', expand=True)

        task_label = Label(fr22, text="Tasks", anchor=CENTER, bg='black', fg=rgb((180, 150, 207)), font='stencil 40')
        task_label.pack(pady=10, padx=10)

        task_entry = Entry(fr22, textvariable=self.temp, bg='grey', fg='black', font='stencil 30')
        task_entry.pack(padx=10, pady=10, fill='x', expand=True)
        task_entry.focus()

        task_button = Button(fr22, text="add", anchor=CENTER, bg='black', fg=rgb((180, 150, 207)), font='stencil 25',
                             command=self.set_task)
        task_button.pack(side='bottom', padx=10, pady=10, fill='x', expand=True)

        quit_button = Button(self.root, text='Exit', anchor=CENTER, bg='black', fg='red', font='stencil 20', width=100,
                             command=self.root.destroy)

        self.task_label = Label(fr1, text="\n\n\n\n\n         No Task         ", anchor=CENTER, bg='black', fg='grey',
                                font='stencil 30')
        self.task_label.pack()

        activate_button = Button(fr23, text="ACTIVATE", anchor=CENTER, bg='black', fg=rgb((0, 255, 0)),
                                 font='stencil 30', command=self.action)
        activate_button.pack(side='bottom', padx=10, pady=10, fill='x', expand=True)

        quit_button.pack(side='bottom')
        self.root.mainloop()

    def set_time(self):
        try:
            if int(self.task_time[0].get()) > 23 or int(self.task_time[1].get()) > 59 or int(
                    self.task_time[2].get()) > 59:
                messagebox.showwarning("Warning", "Enter The Real Time Values!!!")
            else:
                self.task_time = (int(self.task_time[0].get()) * 3600) + (int(self.task_time[1].get()) * 60) + (
                    int(self.task_time[2].get()))
                messagebox.showinfo("Information", "You Successfully Set Tasks' Time!")
                self.time_const[3]['state'] = DISABLED
                self.time_const[3]['text'] = "Time Selected"
                self.time_const[0]['state'] = DISABLED
                self.time_const[1]['state'] = DISABLED
                self.time_const[2]['state'] = DISABLED
                self.time_mode = True
        except ValueError:
            messagebox.showerror("Error", "You Miss One or More Entry!!!")

    def set_task(self):
        if len(self.temp.get()) > 50:
            messagebox.showerror("Error", "Many Words Than Enough!!!")
            return
        self.task_list.append(self.temp.get())
        if self.task_label['text'] == '\n\n\n\n\n         No Task         ':
            self.task_label['fg'] = rgb((180, 150, 207))
            self.task_label['text'] = f"* {self.temp.get()}"
        else:
            self.task_label['fg'] = rgb((180, 150, 207))
            self.task_label['text'] += f"\n* {self.temp.get()}"
        self.temp.set("")
        self.root.update()

    def warning(self, tm):
        warn = Tk()
        warn.title("Warning")
        warn.config(bg="black")
        warn.geometry('600x250+936+614') # 1536x864
        warn.resizable(False, False)
        warn.overrideredirect('True')

        fr1 = Frame(warn, bd=5, bg='black', height=40, width=30, highlightcolor='white', relief='ridge')
        fr1.pack()
        fr2 = Frame(warn, bg='black')
        fr2.pack()

        l1 = Label(fr1, text=self.task, anchor=N, bg='grey', fg='red', font='stencil 30', width=40,
                   height=2)
        l1.pack()

        l2 = Label(fr2, text="time for single task:", anchor=NW, bg='black', fg='red', font='stencil 10')
        l2.pack()

        fr3 = Frame(fr2, bg='black')
        fr3.pack()

        lh = Label(fr3, text=tm[0], bg='black', fg='white', font='stencil 35')
        lh.grid(column=0, row=0, padx=10)

        lhl = Label(fr3, text="hours", bg='black', fg='red', font='stencil 15')
        lhl.grid(column=1, row=0)

        lm = Label(fr3, text=tm[1], bg='black', fg='white', font='stencil 35')
        lm.grid(column=2, row=0, padx=10)

        lml = Label(fr3, text="minutes", bg='black', fg='red', font='stencil 15')
        lml.grid(column=3, row=0)

        ls = Label(fr3, text=tm[2], bg='black', fg='white', font='stencil 35')
        ls.grid(column=4, row=0, padx=10)

        lsl = Label(fr3, text="seconds", bg='black', fg='red', font='stencil 15')
        lsl.grid(column=5, row=0)

        b1 = Button(warn, text="Task Starts", anchor=CENTER, bg='black', fg='white', font='stencil 25', width=40,
                    height=10, command=warn.destroy)
        b1.pack(side='bottom')

        warn.mainloop()

def break_window():
    warn = Tk()
    warn.title("Warning")
    warn.config(bg="black")
    warn.geometry('600x250+936+614') # 1536x864
    warn.overrideredirect('True')
    warn.resizable(False, False)

    fr1 = Frame(warn, bd=5, bg='black', height=40, width=30, highlightcolor='white', relief='ridge')
    fr1.pack()

    l1 = Label(fr1, text="Now Break Time, You have\n5 minutes to have a rest", anchor=N, bg='grey', fg='red',
               font='stencil 30', width=40,
               height=2)
    l1.pack()

    b1 = Label(warn, text="Break Starts after - 3", anchor=CENTER, bg='black', fg='white', font='stencil 25', width=40,
                height=10)
    b1.pack(side='bottom')
    warn.update()
    sleep(1)
    b1['text'] = b1['text'][:len(b1['text'])-1]+"2"
    warn.update()
    sleep(1)
    b1['text'] = b1['text'][:len(b1['text']) - 1] + "1"
    warn.update()
    sleep(1)
    b1['text'] = "Starts"
    b1['font'] = "stencil 40"
    b1['fg'] = "green"
    warn.update()
    sleep(0.5)
    warn.destroy()





def word_completer(inp):
    maximum = 25
    result = " "
    size = 0
    inp = inp.split()
    for i in range(len(inp)):
        size += len(inp[i]) + 1
        if size < maximum:
            result += inp[i] + " "
        else:
            result += '\n'
            maximum = 50
            result += inp[i] + " "
    return result


def rgb(inp):
    return "#%02x%02x%02x" % inp


if __name__ == '__main__':
    main()
