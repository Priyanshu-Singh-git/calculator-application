import tkinter

class calc:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Calculator")
        self.e = tkinter.Entry(self.root, width=44, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10,ipady=30)

        self.button_1 = tkinter.Button(self.root,text='1', padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = tkinter.Button(self.root, text='2', padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = tkinter.Button(self.root, text='3', padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = tkinter.Button(self.root, text='4', padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = tkinter.Button(self.root, text='5', padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = tkinter.Button(self.root, text='6', padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = tkinter.Button(self.root, text='7', padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = tkinter.Button(self.root, text='8', padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = tkinter.Button(self.root, text='9', padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = tkinter.Button(self.root, text='0', padx=40, pady=20, command=lambda: self.button_click(0))
        self.button_dot = tkinter.Button(self.root, text=" .", padx=40, pady=20, command=lambda: self.button_click('.'))
        self.button_equal = tkinter.Button(self.root, text="=", padx=40, pady=20, command=lambda: self.button_click('='))
        self.button_m = tkinter.Button(self.root, text="*", padx=40, pady=20, command=lambda: self.button_click('*'))
        self.button_a = tkinter.Button(self.root, text="+", padx=40, pady=20, command=lambda: self.button_click("+"))
        self.button_s = tkinter.Button(self.root, text="-", padx=40, pady=20, command=lambda: self.button_click("-"))
        self.button_d = tkinter.Button(self.root, text="/", padx=40, pady=20, command=lambda: self.button_click("/"))
        self.button_clear = tkinter.Button(self.root, text="clear", padx=30, pady=20, command=lambda: self.button_clear(3))


        self.button_0.grid(row=5, column=1)
        self.button_1.grid(row=4, column=0)
        self.button_2.grid(row=4, column=1)

        self.button_3.grid(row=4, column=2)
        self.button_4.grid(row=3, column=0)
        self.button_5.grid(row=3, column=1)

        self.button_6.grid(row=3, column=2)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)

        self.button_9.grid(row=2, column=2)
        self.button_dot.grid(row=4, column=2)
        self.button_equal.grid(row=5, column=0)

        self.button_d.grid(row=1, column=0)
        self.button_m.grid(row=1, column=1)
        self.button_s.grid(row=1, column=2)
        self.button_a.grid(row=4, column=0)

        self.button_clear.grid(row=5, column=2)

        self.root.mainloop()

    def button_click(self, number):
        self.current=self.e.get()
        self.e.delete(0, "end")
        self.n=str(number)
        self.mix=self.current+self.n
        self.e.delete(0)
        self.e.insert(0, self.mix)

    def button_clear(self,c):
        pass



if __name__=="__main__":
    calcobject=calc()