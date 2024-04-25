from tkinter import Tk, Frame, Entry, Button, END


class Calculadora:
    def __init__(self):
        self.window = Tk()
        self.window.title('Calculadora         OPS!corp.')
        self.window.resizable(0, 0)
        self.cor_bg = '#1a284a'
        self.cor_fg = '#99fff8'
        self.cor_button = '#1a284a'
        self.font_text = 'arial 20 bold'

        self.window.configure(bg=self.cor_bg)

        self.screen_entrada = Entry(self.window, font=self.font_text, bg=self.cor_bg, fg=self.cor_fg, width=18)
        self.screen_entrada.pack()

        self.frame = Frame(self.window, bg='#1a284a')
        self.frame.pack()

        self.button_0 = Button(self.frame, bg=self.cor_button, bd=0, text='0', font=self.font_text,
                               fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('0'))
        self.button_1 = Button(self.frame, bg=self.cor_button, bd=0, text='1', font=self.font_text,
                               fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('1'))
        self.button_2 = Button(self.frame, bg=self.cor_button, bd=0, text='2', font=self.font_text,
                               fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('2'))
        self.button_3 = Button(self.frame, bg=self.cor_button, bd=0, text='3', font=self.font_text,
                               fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('3'))
        self.button_4 = Button(self.frame, bg=self.cor_button, bd=0, text='4', font=self.font_text,
                               fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('4'))
        self.button_5 = Button(self.frame, bg=self.cor_button, bd=0, text='5', font=self.font_text,
                               fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('5'))
        self.button_6 = Button(self.frame, bg=self.cor_button, bd=0, text='6', font=self.font_text,
                               fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('6'))
        self.button_7 = Button(self.frame, bg=self.cor_button, bd=0, text='7', font=self.font_text,
                               fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('7'))
        self.button_8 = Button(self.frame, bg=self.cor_button, bd=0, text='8', font=self.font_text,
                               fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('8'))
        self.button_9 = Button(self.frame, bg=self.cor_button, bd=0, text='9', font=self.font_text,
                               fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('9'))
        self.button_add = Button(self.frame, bg=self.cor_button, bd=0, text='+', font=self.font_text,
                                 fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('+'))
        self.button_subtra = Button(self.frame, bg=self.cor_button, bd=0, text='-', font=self.font_text,
                                    fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('-'))
        self.button_dividir = Button(self.frame, bg=self.cor_button, bd=0, text='÷', font=self.font_text,
                                     fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('/'))
        self.button_mult = Button(self.frame, bg=self.cor_button, bd=0, text='x', font=self.font_text,
                                  fg=self.cor_fg, width=4, height=1, command=lambda: self.touch('*'))
        self.button_igual = Button(self.frame, bg=self.cor_button, bd=0, text='=', font=self.font_text,
                                   fg=self.cor_fg, width=4, height=1, command=self.total)
        self.button_clean = Button(self.frame, bg=self.cor_button, bd=0, text='Clean', font=self.font_text,
                                   fg=self.cor_fg, width=5, height=1, command=self.clean)

        self.button_7.grid(row=0, column=0)
        self.button_8.grid(row=0, column=1)
        self.button_9.grid(row=0, column=2)
        self.button_dividir.grid(row=0, column=3)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_mult.grid(row=1, column=3)
        self.button_1.grid(row=2, column=0)
        self.button_2.grid(row=2, column=1)
        self.button_3.grid(row=2, column=2)
        self.button_add.grid(row=2, column=3)
        self.button_subtra.grid(row=3, column=3)
        self.button_clean.grid(row=3, column=2)
        self.button_igual.grid(row=3, column=1)
        self.button_0.grid(row=3, column=0)

        self.window.mainloop()

    def touch(self, num):
        self.screen_entrada.insert(END, num)

    def clean(self):
        self.screen_entrada.delete(0, END)

    def total(self):
        total = eval(self.screen_entrada.get())
        self.screen_entrada.delete(0, END)
        self.screen_entrada.insert(0, str(total))


Calculadora()
