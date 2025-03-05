from time import sleep
from random import choice, randint
from tkinter import *


my_mood = ['bene', 'male']
root = None
siz = None


def main():
    win()




def win():
    global root, siz
    speed = 1
    angl = 0
    siz = 100
    root = Tk()
    root.attributes('-fullscreen', True)
    root.config(bg="black")
    root.bind('<Escape>', quitt)
    canvas = Canvas(root, bg="black", highlightthickness=0)
    label = canvas.create_text(root.winfo_screenwidth()//2, root.winfo_screenheight()//2, text=choice(my_mood), fill=rgb((randint(00, 255), randint(00, 255), randint(00, 255))), anchor=CENTER, font=f"stencil {siz}")
    canvas.pack(padx=0, pady=0, fill='both', expand=True)
    while True:
        try:
            root.update()
            canvas.itemconfig(label, angle=angl)
            canvas.itemconfig(label, text=choice(my_mood))
            canvas.itemconfig(label, font=f"stencil {siz}")
            canvas.itemconfig(label, fill=rgb((randint(00, 255), randint(00, 255), randint(00, 255))))
            angl += 45
            if siz < 1600:
                siz += 5
            else:
                siz = 100
                speed = 0.01
            sleep(speed)
            speed *= 0.4
        except Exception as e:
           continue



def quitt(event):
    global root
    root.destroy()


    
def rgb(inp):
    return "#%02x%02x%02x" % inp



if __name__ == '__main__':
    main()
