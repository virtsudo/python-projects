from tkinter import *
from _tkinter import TclError
from time import sleep, strftime
from os import name


def main():
    if name == 'nt':
        Window()




class Window:
    def __init__(self):
        self.date = [[0, 0, 0], [0, 0, 0]]
        self.topic = "Demo Text"
        self.root = Tk()
        self.root.config(bg="black")
        self.root.geometry(f"700x300+{(int(self.root.winfo_screenwidth())-700)}+{(int(self.root.winfo_screenheight())-350)}")
        self.root.resizable(False, False)
        self.root.overrideredirect('True')
        self.root.lift()
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "black")

        self.root.title("Window")

        self.label = Label(self.root, text=f"{self.topic}", anchor=CENTER, bg='black', fg=rgb((0, 255, 0)), font='stencil 30 ', wraplength=600)
        self.label.pack()

        self.time_line_label = Label(self.root, text=f"{self.age_decorator_version2()}", anchor=CENTER, bg='black', fg=rgb((255, 0, 0)), font='stencil 30 ')
        self.time_line_label.pack(padx=1, pady=1, fill='both')

        self.label = Label(self.root, text="left to exam.", anchor=CENTER, bg='black', fg=rgb((255, 0, 0)), font='stencil 30 ')
        self.label.pack()
        
        while True:
            self.root.update()
            self.time_line_label['text'] = f"{self.age_decorator_version2()}"
            sleep(1)




    def year_to_day_converter(self, y):
        dt = self.date
        star_year = (y // 4) * 366
        simple_year = (y - (y // 4)) * 365
        return int(star_year + simple_year)

    def day_to_year_converter(self, d):
        dt = self.date
        return int((d-int(d/1461))/365)


    def month_to_day_converter(self, y, m):
        dt = self.date
        if m == 0:
            return 0
        month_list1 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        month_list2 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        if y % 4 != 0:
            return month_list1[m-1]
        else:
            return month_list2[m-1]

    def day_to_month_converter(self, y, d):
        dt = self.date
        month_list1 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        month_list2 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        if y % 4 == 0:
            for i in range(len(month_list2)-1):
                if month_list2[i] <= d < month_list2[i + 1]:
                    return i
        else:
            for i in range(len(month_list1)-1):
                if month_list1[i] <= d < month_list1[i + 1]:
                    return i

    def day_to_second_converter(self, d):
        dt = self.date
        return int(d*((23*60+56)*60+4))

    def second_to_day_converter(self, s):
        d = self.date
        return int(s / ((23 * 60 + 56) * 60 + 4))

    def date_to_second_converter(self, date):
        return int(self.day_to_second_converter(self.year_to_day_converter(date[0][0])+self.month_to_day_converter(date[0][0], date[0][1])+date[0][2])+date[1][0]*3600+date[1][1]*60+date[1][2])

    def second_to_date_converter(self, s):
        year = self.day_to_year_converter(self.second_to_day_converter(s))
        month = self.day_to_month_converter(year, self.second_to_day_converter(s)-self.year_to_day_converter(year))
        day = self.second_to_day_converter(s)-self.year_to_day_converter(year)-self.month_to_day_converter(year, month+1)
        hour = (s-self.day_to_second_converter(self.second_to_day_converter(s)))//3600
        minute = ((s-self.day_to_second_converter(self.second_to_day_converter(s))) % 3600)//60
        second = ((s-self.day_to_second_converter(self.second_to_day_converter(s))) % 3600) % 60
        return [[year, month, day], [hour, minute, second]]

    def age_converter(self):
        return self.second_to_date_converter(abs((self.date_to_second_converter(self.date))-(self.date_to_second_converter([[int(strftime("%Y")), int(strftime("%m")), int(strftime("%d"))], [int(strftime("%H")), int(strftime("%M")), int(strftime("%S"))]]))))

    def age_decorator_version1(self):
        return f"{int(self.age_converter()[0][0]) if int(self.age_converter()[0][0])>9 else '0'+str(int(self.age_converter()[0][0]))}.{int(self.age_converter()[0][1]) if int(self.age_converter()[0][1])>9 else '0'+str(int(self.age_converter()[0][1]))}.{int(self.age_converter()[0][2]) if int(self.age_converter()[0][2])>9 else '0'+str(int(self.age_converter()[0][2]))}  {int(self.age_converter()[1][0]) if int(self.age_converter()[1][0])>9 else '0'+str(int(self.age_converter()[1][0]))}:{int(self.age_converter()[1][1]) if int(self.age_converter()[1][1])>9 else '0'+str(int(self.age_converter()[1][1]))}:{int(self.age_converter()[1][2]) if int(self.age_converter()[1][2])>9 else '0'+str(int(self.age_converter()[1][2]))}"

    def age_decorator_version2(self):
        output = ""
        year = self.age_converter()[0][0]
        if year > 0:
            output += f"{int(self.age_converter()[0][0]) if int(self.age_converter()[0][0]) > 9 else ' '+str(int(self.age_converter()[0][0]))} year(s) "
        month = self.age_converter()[0][1]
        if month > 0:
            output += f"{int(self.age_converter()[0][1]) if int(self.age_converter()[0][1])>9 else ' '+str(int(self.age_converter()[0][1]))} month(s)"
        day = self.age_converter()[0][2]
        if day > 0:
            output += f"{int(self.age_converter()[0][2]) if int(self.age_converter()[0][2])>9 else ' '+str(int(self.age_converter()[0][2]))} day(s)\n"
        output += f"{int(self.age_converter()[1][0]) if int(self.age_converter()[1][0]) > 9 else '0' + str(int(self.age_converter()[1][0]))}:"
        output += f"{int(self.age_converter()[1][1]) if int(self.age_converter()[1][1]) > 9 else '0' + str(int(self.age_converter()[1][1]))}:"
        output += f"{int(self.age_converter()[1][2]) if int(self.age_converter()[1][2])>9 else '0'+str(int(self.age_converter()[1][2]))}"

        return output


def set_data():
    root = Tk()
    root.config(bg="black")
    root.geometry('400x200+600+300')
    root.resizable(width=False, height=False)
    root.overrideredirect('True') # remove title bar
    root.lift()

    label = Label()

    root.mainloop()


def rgb(inp):
    return "#%02x%02x%02x" % inp



if __name__ == '__main__':
    try:
        main()
    except TclError:
        print("Exit successes!")
