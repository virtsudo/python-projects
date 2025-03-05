from time import sleep
from random import randint, choice
from tkinter import *

color = ["black", "grey", "white"]

def main():
    win()




def win():
    global root
    speed = 0.05
    angl = 0
    diff = 12
    root = Tk()
    res = [root.winfo_screenwidth(), root.winfo_screenheight()]
    root.attributes('-fullscreen', True)
    root.config(bg="black")
    root.bind('<Escape>', quitt)
    canvas = Canvas(root, bg="black", highlightthickness=0)
    label = canvas.create_text(res[0]/2, res[1]/2, text=f"|{diff*' '}|", fill=rgb((randint(0, 255), randint(0, 255), randint(0, 255))), anchor=CENTER, font=f"stencil 70")
    canvas.pack(padx=0, pady=0, fill='both', expand=True)
    while True:
        root.update()
        canvas.itemconfig(label, angle=angl)
        canvas.itemconfig(label, text=f"|{diff*' '}|")
        canvas.itemconfig(label, fill=rgb((randint(0, 255), randint(0, 255), randint(0, 255))))
        angl += 45
        canvas['bg'] = choice(color)
        if diff < 30 :
            diff += 1
        sleep(speed)
        #speed*=0.5



def quitt(event):
    global root
    root.destroy()


    
def rgb(inp):
    return "#%02x%02x%02x" % inp



if __name__ == '__main__':
    main()
