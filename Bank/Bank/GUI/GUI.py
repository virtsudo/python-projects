from tkinter import *
from datetime import datetime


def rgb(color_set):
    return "#%02x%02x%02x" % color_set


language_label1 = ['english', 'italiano', 'РУССКИЙ', 'español', 'deutsch', 'français']
language_label2 = ['language', 'lingua']
language_label3 = ['Choose your language', 'Scegliere la lingua']
bank_label = ['bank', 'banca']
main_label = ['main', 'generale']
theme_label = ['theme', 'tema']
quit_label = ['exit', 'uscita']
deposit_label = ['deposit', 'versamento']
transaction_label = ['transaction', 'transazione']
withdrawal_label = ['withdrawal', 'prelevamento']
balance_label = ['balance', 'saldo']
amount_label = ['amount', 'importo']
conform_label = ['conform', 'conforme']
colors = {'light': {'main_fg': rgb((0, 110, 255)), 'main_bg': rgb((245, 250, 255)), 'quit_bg': rgb((245, 0, 0)),
                    'depo_fg': rgb((0, 225, 0)), 'with_fg': rgb((225, 0, 0)), 'entry_bg': rgb((225, 225, 225)),
                    'w': 'white', 'b': 'black', 'r': 'red'},
          'dark': {'main_fg': rgb((128, 0, 255)), 'main_bg': rgb((50, 50, 50)), 'quit_bg': rgb((245, 0, 0)),
                   'depo_fg': rgb((0, 225, 0)), 'with_fg': rgb((225, 0, 0)), 'entry_bg': rgb((60, 60, 60)),
                   'w': 'white', 'b': 'black', 'r': 'red'}}


class GUI:
    def __init__(self, bank):
        self.bank = bank
        self.elements = {
            'navigate': {'obj': None, 'event': False},
            'main': {'obj': None, 'event': False},
            'language': {'obj': None, 'event': False},
            'deposit': {'obj': None, 'event': False},
            'withdrawal': {'obj': None, 'event': False},
            'balance': {'obj': None, 'event': False}
        }
        self.language_mode = language_label1.index('english')
        self.color_mode = 'light'
        self.messagebox, self.messagebox_label, self.messagebox_button = None, None, None

        self.root = Tk()
        self.root.title('Bank')
        self.root.config(bg=colors[self.color_mode]['b'])
        self.root.attributes('-fullscreen', True)

        Navigate(self)

        self.root.mainloop()

    def attribute_modifier(self, master, attribute, value):
        self.color_mode = self.color_mode
        master[attribute] = value

    def theme_setter(self):
        self.color_mode = 'dark' if self.color_mode == 'light' else 'light'
        for attribute, value in self.elements['navigate']['obj'].__dict__.items():
            if attribute != 'quit_button' and attribute != 'root_frame':
                self.attribute_modifier(value, 'bg', colors[self.color_mode]['main_bg'])
                try:
                    self.attribute_modifier(value, 'fg', colors[self.color_mode]['main_fg'])
                except:
                    continue
            elif attribute == 'root_frame':
                self.attribute_modifier(value, 'bg', colors[self.color_mode]['main_fg'])

        self.root.update()
        for i in self.elements.items():
            if i[1]['event'] and i[0] != 'navigate':
                temp = i[0]
                self.elements[i[0]]['obj'].__dict__['root'].pack_forget()
                self.elements[i[0]]['event'] = False
                break
        match temp:
            case 'main':
                Main(self)
            case 'language':
                Language(self)
            case 'deposit':
                Deposit(self)
            case 'withdrawal':
                Withdrawal(self)
            case 'balance':
                Balance(self)

    def gui_messagebox(self, message):
        self.messagebox = Toplevel(self.root)
        self.messagebox.title('System Error')
        self.messagebox.geometry('300x150+650+350')
        self.messagebox.resizable(width=False, height=False)
        self.messagebox.configure(bg=colors[self.color_mode]['main_bg'])
        self.messagebox_label = Label(self.messagebox, text=message, bg=colors[self.color_mode]['main_bg'],
                                      fg=colors[self.color_mode]['with_fg'], font='arial 20')
        self.messagebox_label.pack(pady=20)
        self.messagebox_button = Button(self.messagebox, text='OK', command=self.messagebox.destroy,
                                        bg=colors[self.color_mode]['main_bg'],
                                        fg=colors[self.color_mode]['main_fg'], font='arial 15', relief='ridge')
        self.messagebox_button.pack(side='bottom', padx=0, pady=0, fil='x')
        self.messagebox.transient(self.root)
        self.messagebox.grab_set()


class Navigate:
    def __init__(self, root: GUI):
        if root.elements['navigate']['event']:
            return
        self.root_frame = Frame(root.root, bg=colors[root.color_mode]['main_fg'])
        self.root_frame.pack(padx=1, pady=1, fill='both', expand=True)

        self.main_frame = Frame(self.root_frame, bg=colors[root.color_mode]['main_bg'])
        self.main_frame.pack(padx=5, pady=5, fill='both', expand=True)

        self.main_header = Frame(self.main_frame, bg=colors[root.color_mode]['main_bg'])
        self.main_header.pack(side='top', padx=0, pady=0, fill='x')

        self.title_label = Label(self.main_header, text=bank_label[root.language_mode],
                                 bg=colors[root.color_mode]['main_bg'], fg=colors[root.color_mode]['main_fg'],
                                 font='stencil 30', relief='flat')
        self.title_label.pack(padx=0, pady=10)

        self.main_body = Frame(self.main_frame, bg=colors[root.color_mode]['main_bg'])
        self.main_body.pack(padx=0, pady=0, fill='both', expand=True)
        self.main_body.pack_propagate(False)

        self.main_footer = Frame(self.main_frame, bg=colors[root.color_mode]['main_bg'])
        self.main_footer.pack(side='bottom', pady=0, padx=0, fill='x')

        self.language_button = Button(self.main_footer, text=language_label2[root.language_mode],
                                      bg=colors[root.color_mode]['main_bg'], fg=colors[root.color_mode]['main_fg'],
                                      font='stencil 20', relief='ridge', activebackground=colors[root.color_mode]['w'],
                                      activeforeground=colors[root.color_mode]['main_fg'],
                                      command=lambda: Language(root))
        self.language_button.pack(side="left", padx=0, pady=0, fill='x', expand=True)

        self.cancel_button = Button(self.main_footer, text=main_label[root.language_mode],
                                    bg=colors[root.color_mode]['main_bg'], fg=colors[root.color_mode]['main_fg'],
                                    font='stencil 20', relief='ridge', activebackground=colors[root.color_mode]['w'],
                                    activeforeground=colors[root.color_mode]['main_fg'], command=lambda: Main(root))
        self.cancel_button.pack(side="left", padx=0, pady=0, fill='x', expand=True)

        self.theme_button = Button(self.main_footer, text=theme_label[root.language_mode],
                                   bg=colors[root.color_mode]['main_bg'],
                                   fg=colors[root.color_mode]['main_fg'], font='stencil 20', relief='ridge',
                                   activebackground=colors[root.color_mode]['w'],
                                   activeforeground=colors[root.color_mode]['main_fg'],
                                   command=lambda: root.theme_setter())
        self.theme_button.pack(side="left", padx=0, pady=0, fill='x', expand=True)

        self.quit_button = Button(self.main_footer, text=quit_label[root.language_mode],
                                  bg=colors[root.color_mode]['quit_bg'], fg=colors[root.color_mode]['w'],
                                  font='stencil 20', relief='raised', width=5,
                                  activebackground=colors[root.color_mode]['b'],
                                  activeforeground=colors[root.color_mode]['r'], command=root.root.destroy)
        self.quit_button.pack(side="right", padx=0, pady=0, fill='x', expand=True)

        root.root.update()
        root.elements['navigate']['obj'] = self
        root.elements['navigate']['event'] = True

        Main(root)


class Language:
    def __init__(self, root: GUI):
        if root.elements['language']['event']:
            return
        for i in root.elements.items():
            if i[1]['event'] and i[0] != 'navigate':
                root.elements[i[0]]['obj'].__dict__['root'].pack_forget()
                root.elements[i[0]]['event'] = False
        self.root = Frame(root.elements['navigate']['obj'].__dict__['main_body'], bg=colors[root.color_mode]['main_bg'])
        self.root.pack(pady=100, padx=300, fill='both', expand=True)
        self.root.pack_propagate(False)
        self.languages = dict()

        self.inner_frame = Frame(self.root, bg=colors[root.color_mode]['main_bg'])
        self.inner_frame.pack(padx=1, pady=1, fill='both', expand=True)

        self.title_frame = Frame(self.inner_frame, bg=colors[root.color_mode]['main_bg'])
        self.title_frame.pack(padx=1, pady=1, fill='x')

        self.title = Label(self.title_frame, text="", bg=colors[root.color_mode]['main_bg'],
                           fg=colors[root.color_mode]['main_fg'], font='stencil 30', width=10)
        self.title.pack(side='top')

        self.language_frame1 = Frame(self.inner_frame, bg=colors[root.color_mode]['main_bg'])
        self.language_frame1.pack(padx=1, pady=1, fill='both', expand=True)

        self.language_frame2 = Frame(self.inner_frame, bg=colors[root.color_mode]['main_bg'])
        self.language_frame2.pack(padx=1, pady=1, fill='both', expand=True)

        self.language_frame3 = Frame(self.inner_frame, bg=colors[root.color_mode]['main_bg'])
        self.language_frame3.pack(padx=1, pady=1, fill='both', expand=True)

        self.languages['en'] = Button(self.language_frame1, text=language_label1[0],
                                      bg=colors[root.color_mode]['main_bg'], fg=colors[root.color_mode]['main_fg'],
                                      font='stencil 30', activebackground=colors[root.color_mode]['w'],
                                      activeforeground=colors[root.color_mode]['main_fg'],
                                      command=lambda: self.language_setter([root, 'english']), relief='ridge')
        self.languages['en'].pack(side='left', padx=1, pady=1, fill='x', expand=True)

        self.languages['it'] = Button(self.language_frame1, text=language_label1[1],
                                      bg=colors[root.color_mode]['main_bg'], fg=colors[root.color_mode]['main_fg'],
                                      font='stencil 30', activebackground=colors[root.color_mode]['w'],
                                      activeforeground=colors[root.color_mode]['main_fg'],
                                      command=lambda: self.language_setter([root, 'italiano']), relief='ridge')
        self.languages['it'].pack(side='right', padx=1, pady=1, fill='x', expand=True)

        self.languages['ru'] = Button(self.language_frame2, text=language_label1[2],
                                      bg=colors[root.color_mode]['main_bg'], fg=colors[root.color_mode]['main_fg'],
                                      font='stencil 30', activebackground=colors[root.color_mode]['w'],
                                      activeforeground=colors[root.color_mode]['w'], state='disabled',
                                      command=lambda: self.language_setter([root, 'english']), relief='ridge')
        self.languages['ru'].pack(side='left', padx=1, pady=1, fill='x', expand=True)

        self.languages['es'] = Button(self.language_frame2, text=language_label1[3],
                                      bg=colors[root.color_mode]['main_bg'], fg=colors[root.color_mode]['main_fg'],
                                      font='stencil 30', activebackground=colors[root.color_mode]['w'],
                                      activeforeground=colors[root.color_mode]['w'], state='disabled',
                                      command=lambda: self.language_setter([root, 'italiano']), relief='ridge')
        self.languages['es'].pack(side='right', padx=1, pady=1, fill='x', expand=True)

        self.languages['de'] = Button(self.language_frame3, text=language_label1[4],
                                      bg=colors[root.color_mode]['main_bg'], fg=colors[root.color_mode]['main_fg'],
                                      font='stencil 30', activebackground=colors[root.color_mode]['w'],
                                      activeforeground=colors[root.color_mode]['w'], state='disabled',
                                      command=lambda: self.language_setter([root, 'english']), relief='ridge')
        self.languages['de'].pack(side='left', padx=1, pady=1, fill='x', expand=True)

        self.languages['fr'] = Button(self.language_frame3, text=language_label1[5],
                                      bg=colors[root.color_mode]['main_bg'], fg=colors[root.color_mode]['main_fg'],
                                      font='stencil 30', activebackground=colors[root.color_mode]['w'],
                                      activeforeground=colors[root.color_mode]['w'], state='disabled',
                                      command=lambda: self.language_setter([root, 'italiano']), relief='ridge')
        self.languages['fr'].pack(side='right', padx=1, pady=1, fill='x', expand=True)

        root.root.update()
        root.elements['language']['obj'] = self
        root.elements['language']['event'] = True

    def language_setter(self, args: list):
        self.title = self.title
        root, mode = args[0], args[1]
        root.language_mode = language_label1.index(mode)
        root.elements['navigate']['obj'].__dict__['title_label']['text'] = bank_label[root.language_mode]
        root.elements['navigate']['obj'].__dict__['language_button']['text'] = language_label2[root.language_mode]
        root.elements['navigate']['obj'].__dict__['cancel_button']['text'] = main_label[root.language_mode]
        root.elements['navigate']['obj'].__dict__['theme_button']['text'] = theme_label[root.language_mode]
        root.elements['navigate']['obj'].__dict__['quit_button']['text'] = quit_label[root.language_mode]
        Main(root)


class Main:
    def __init__(self, root: GUI):
        if root.elements['main']['event']:
            return
        for i in root.elements.items():
            if i[1]['event'] and i[0] != 'navigate':
                root.elements[i[0]]['obj'].__dict__['root'].pack_forget()
                root.elements[i[0]]['event'] = False
        self.root = Frame(root.elements['navigate']['obj'].__dict__['main_body'], bg=colors[root.color_mode]['main_bg'])
        self.root.pack(pady=20, padx=20, fill='both', expand=True)

        self.options = list()
        self.operations = dict()

        self.left_frame = Frame(self.root, bg=colors[root.color_mode]['main_bg'], width=750, height=650)
        self.left_frame.pack(side='left', padx=1, pady=1, ipadx=1, ipady=1, fill='y')
        self.left_frame.pack_propagate(False)

        self.options.append(
            Button(self.left_frame, text="10", bg=colors[root.color_mode]['main_bg'],
                   fg=colors[root.color_mode]['main_fg'], font='stencil 30',
                   activebackground=colors[root.color_mode]['w'],
                   activeforeground=colors[root.color_mode]['main_fg'], width=15,
                   command=lambda: Withdrawal(root, value='10')))
        self.options[0].grid(row=0, column=0, pady=20, padx=10)
        self.options.append(
            Button(self.left_frame, text="20", bg=colors[root.color_mode]['main_bg'],
                   fg=colors[root.color_mode]['main_fg'], font='stencil 30',
                   activebackground=colors[root.color_mode]['w'],
                   activeforeground=colors[root.color_mode]['main_fg'], width=15,
                   command=lambda: Withdrawal(root, value='20')))
        self.options[1].grid(row=0, column=1, pady=20, padx=10)

        self.options.append(
            Button(self.left_frame, text="30", bg=colors[root.color_mode]['main_bg'],
                   fg=colors[root.color_mode]['main_fg'], font='stencil 30',
                   activebackground=colors[root.color_mode]['w'],
                   activeforeground=colors[root.color_mode]['main_fg'], width=15,
                   command=lambda: Withdrawal(root, value='30')))
        self.options[2].grid(row=1, column=0, pady=20, padx=10)
        self.options.append(
            Button(self.left_frame, text="50", bg=colors[root.color_mode]['main_bg'],
                   fg=colors[root.color_mode]['main_fg'], font='stencil 30',
                   activebackground=colors[root.color_mode]['w'],
                   activeforeground=colors[root.color_mode]['main_fg'], width=15,
                   command=lambda: Withdrawal(root, value='50')))
        self.options[3].grid(row=1, column=1, pady=20, padx=10)

        self.options.append(
            Button(self.left_frame, text="100", bg=colors[root.color_mode]['main_bg'],
                   fg=colors[root.color_mode]['main_fg'], font='stencil 30',
                   activebackground=colors[root.color_mode]['w'],
                   activeforeground=colors[root.color_mode]['main_fg'], width=15,
                   command=lambda: Withdrawal(root, value='100')))
        self.options[4].grid(row=2, column=0, pady=20, padx=10)
        self.options.append(
            Button(self.left_frame, text="200", bg=colors[root.color_mode]['main_bg'],
                   fg=colors[root.color_mode]['main_fg'], font='stencil 30',
                   activebackground=colors[root.color_mode]['w'],
                   activeforeground=colors[root.color_mode]['main_fg'], width=15,
                   command=lambda: Withdrawal(root, value='200')))
        self.options[5].grid(row=2, column=1, pady=20, padx=10)

        self.right_frame = Frame(self.root, bg=colors[root.color_mode]['main_bg'], width=750, height=650)
        self.right_frame.pack(side='right', padx=1, pady=1, ipadx=1, ipady=1)
        self.right_frame.pack_propagate(False)

        self.operations['deposit'] = Button(self.right_frame, text=deposit_label[root.language_mode],
                                            bg=colors[root.color_mode]['main_bg'],
                                            fg=colors[root.color_mode]['main_fg'], font='stencil 30',
                                            activebackground=colors[root.color_mode]['w'],
                                            activeforeground=colors[root.color_mode]['main_fg'], width=20,
                                            command=lambda: Deposit(root))
        self.operations['deposit'].pack(pady=30, padx=30, fill='y', expand=True)

        self.operations['withdrawal'] = Button(self.right_frame, text=withdrawal_label[root.language_mode],
                                               bg=colors[root.color_mode]['main_bg'],
                                               fg=colors[root.color_mode]['main_fg'], font='stencil 30',
                                               activebackground=colors[root.color_mode]['w'],
                                               activeforeground=colors[root.color_mode]['main_fg'], width=20,
                                               command=lambda: Withdrawal(root))
        self.operations['withdrawal'].pack(pady=30, padx=30, fill='y', expand=True)

        self.operations['balance'] = Button(self.right_frame, text=balance_label[root.language_mode],
                                            bg=colors[root.color_mode]['main_bg'],
                                            fg=colors[root.color_mode]['main_fg'], font='stencil 30',
                                            activebackground=colors[root.color_mode]['w'],
                                            activeforeground=colors[root.color_mode]['main_fg'], width=20,
                                            command=lambda: Balance(root))
        self.operations['balance'].pack(pady=30, padx=30, fill='y', expand=True)

        root.root.update()
        root.elements['main']['obj'] = self
        root.elements['main']['event'] = True


class Deposit:
    def __init__(self, root: GUI):
        if root.elements['deposit']['event']:
            return
        for i in root.elements.items():
            if i[1]['event'] and i[0] != 'navigate':
                root.elements[i[0]]['obj'].__dict__['root'].pack_forget()
                root.elements[i[0]]['event'] = False
        self.root = Frame(root.elements['navigate']['obj'].__dict__['main_body'], bg=colors[root.color_mode]['main_bg'])
        self.root.pack(pady=100, padx=300, fill='both', expand=True)
        self.root.pack_propagate(False)

        self.text = Variable()

        self.inner_frame = Frame(self.root, bg=colors[root.color_mode]['main_bg'])
        self.inner_frame.pack(padx=1, pady=1, fill='both', expand=True)

        self.title = Label(self.inner_frame, text=deposit_label[root.language_mode], anchor=W,
                           bg=colors[root.color_mode]['main_bg'],
                           fg=colors[root.color_mode]['main_fg'],
                           font='stencil 30 underline', width=10)
        self.title.pack(side='top', fill='x', padx=0, pady=0)

        self.entry_frame = Frame(self.inner_frame, bg=colors[root.color_mode]['main_bg'])
        self.entry_frame.pack(padx=100, pady=100, fill='x')

        self.entry_label1 = Label(self.entry_frame, text=f'{amount_label[root.language_mode]} : ', anchor=W,
                                  bg=colors[root.color_mode]['main_bg'],
                                  fg=colors[root.color_mode]['main_fg'],
                                  font='stencil 20', width=30)
        self.entry_label1.grid(row=0, column=0)

        self.entry_label2 = Label(self.entry_frame, text=' €  +', anchor=W, bg=colors[root.color_mode]['main_bg'],
                                  fg=colors[root.color_mode]['main_fg'],
                                  font='stencil 20', width=3)
        self.entry_label2.grid(row=0, column=1)

        self.entry = Entry(self.entry_frame, textvariable=self.text, bg=colors[root.color_mode]['entry_bg'],
                           fg=colors[root.color_mode]['depo_fg'],
                           insertbackground=colors[root.color_mode]['main_fg'], font='stencil 20', width=4,
                           borderwidth=0, validate='key', validatecommand=(self.root.register(self.validator), "%P"))
        self.entry.grid(row=0, column=2)

        self.submit_button = Button(self.inner_frame, text=conform_label[root.language_mode],
                                    bg=colors[root.color_mode]['main_bg'],
                                    fg=colors[root.color_mode]['main_fg'], font='stencil 20',
                                    command=lambda: self.submit([root, self.text.get()]),
                                    activeforeground=colors[root.color_mode]['main_fg'], activebackground='white')
        self.submit_button.pack(side='bottom', pady=0, padx=0, fill='x')

        root.root.update()
        root.elements['deposit']['obj'] = self
        root.elements['deposit']['event'] = True

    def validator(self, text):
        self.title = self.title
        return text.isdigit() and len(text) <= 4

    def submit(self, args: list):
        self.title = self.title
        root, value = args
        if len(value) == 0:
            root.gui_messagebox("Invalid Value")
        else:
            root.bank.deposit(1, datetime.now(), float(value))
            Main(root)


class Withdrawal:
    def __init__(self, root: GUI, value=''):
        if root.elements['withdrawal']['event']:
            return
        for i in root.elements.items():
            if i[1]['event'] and i[0] != 'navigate':
                root.elements[i[0]]['obj'].__dict__['root'].pack_forget()
                root.elements[i[0]]['event'] = False
        self.root = Frame(root.elements['navigate']['obj'].__dict__['main_body'], bg=colors[root.color_mode]['main_bg'])
        self.root.pack(pady=100, padx=300, fill='both', expand=True)
        self.root.pack_propagate(False)

        self.text = Variable()
        self.text.set(value)

        self.inner_frame = Frame(self.root, bg=colors[root.color_mode]['main_bg'])
        self.inner_frame.pack(padx=1, pady=1, fill='both', expand=True)

        self.title = Label(self.inner_frame, text=withdrawal_label[root.language_mode], anchor=W,
                           bg=colors[root.color_mode]['main_bg'],
                           fg=colors[root.color_mode]['main_fg'],
                           font='stencil 30 underline', width=10)
        self.title.pack(side='top', fill='x', padx=0, pady=0)

        self.entry_frame = Frame(self.inner_frame, bg=colors[root.color_mode]['main_bg'])
        self.entry_frame.pack(padx=100, pady=100, fill='x')

        self.entry_label1 = Label(self.entry_frame, text=f'{amount_label[root.language_mode]} : ', anchor=W,
                                  bg=colors[root.color_mode]['main_bg'],
                                  fg=colors[root.color_mode]['main_fg'],
                                  font='stencil 20', width=30)
        self.entry_label1.grid(row=0, column=0)

        self.entry_label2 = Label(self.entry_frame, text=' €  -', anchor=W, bg=colors[root.color_mode]['main_bg'],
                                  fg=colors[root.color_mode]['main_fg'],
                                  font='stencil 20', width=3)
        self.entry_label2.grid(row=0, column=1)

        self.entry = Entry(self.entry_frame, textvariable=self.text, bg=colors[root.color_mode]['entry_bg'],
                           fg=colors[root.color_mode]['with_fg'],
                           insertbackground=colors[root.color_mode]['main_fg'], font='stencil 20', width=4,
                           borderwidth=0, validate='key', validatecommand=(self.root.register(self.validator), "%P"))
        self.entry.grid(row=0, column=2)

        self.submit_button = Button(self.inner_frame, text=conform_label[root.language_mode],
                                    bg=colors[root.color_mode]['main_bg'],
                                    fg=colors[root.color_mode]['main_fg'], font='stencil 20',
                                    command=lambda: self.submit([root, self.text.get()]),
                                    activeforeground=colors[root.color_mode]['main_fg'], activebackground='white')
        self.submit_button.pack(side='bottom', pady=0, padx=0, fill='x')

        root.root.update()
        root.elements['withdrawal']['obj'] = self
        root.elements['withdrawal']['event'] = True

    def validator(self, text):
        self.title = self.title
        return text.isdigit() and len(text) <= 4

    def submit(self, args: list):
        self.title = self.title
        root, value = args
        if len(value) == 0:
            root.gui_messagebo("Invalid Value")
        else:
            root.bank.withdrawal(1, datetime.now(), float(value))
            Main(root)


class Balance:
    def __init__(self, root: GUI):
        if root.elements['balance']['event']:
            return
        for i in root.elements.items():
            if i[1]['event'] and i[0] != 'navigate':
                root.elements[i[0]]['obj'].__dict__['root'].pack_forget()
                root.elements[i[0]]['event'] = False
        self.root = Frame(root.elements['navigate']['obj'].__dict__['main_body'], bg=colors[root.color_mode]['main_bg'])
        self.root.pack(pady=100, padx=300, fill='both', expand=True)
        self.root.pack_propagate(False)

        self.inner_frame = Frame(self.root, bg=colors[root.color_mode]['main_bg'])
        self.inner_frame.pack(padx=1, pady=1, fill='both', expand=True)

        self.title = Label(self.inner_frame, text=balance_label[root.language_mode], anchor=W,
                           bg=colors[root.color_mode]['main_bg'],
                           fg=colors[root.color_mode]['main_fg'],
                           font='stencil 30 underline', width=10)
        self.title.pack(side='top', fill='x', padx=0, pady=0)

        self.data = root.bank.get_account(1).get_balance()

        self.balance_label = Label(self.inner_frame, text=f'{balance_label[root.language_mode]} : {self.data}', anchor=CENTER,
                                   bg=colors[root.color_mode]['main_bg'], fg=colors[root.color_mode]['main_fg'],
                                   font='stencil 20')
        self.balance_label.pack(padx=0, pady=0, fill='both', expand=True)

        self.ok_button = Button(self.inner_frame, text="ok", bg=colors[root.color_mode]['main_bg'],
                                fg=colors[root.color_mode]['main_fg'], font='stencil 20',
                                command=lambda: self.submit(root),
                                activeforeground=colors[root.color_mode]['main_fg'], activebackground='white')
        self.ok_button.pack(side='bottom', pady=0, padx=0, fill='x')

        root.root.update()
        root.elements['balance']['obj'] = self
        root.elements['balance']['event'] = True

    def submit(self, root: GUI):
        Main(root)
