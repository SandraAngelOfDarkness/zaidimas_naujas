from tkinter import *
import webbrowser
from PIL import ImageTk, Image
from lengvas import *

class Sandra():
    def __init__(self, main):
        self.main = main
        self.main.title("Žaidimai")
        self.f_demo = Frame(self.main)
        self.l_pasiulymai = Label(self.f_demo, text="Poilsis")
        self.b_close = Button(self.f_demo, width=30, text="Uzdaryti", command=self.close_window)
        
        self.l_pasiulymai.pack(side=TOP)
        self.b_close.pack()
        self.f_demo.pack(side=BOTTOM)

        self.main.mainloop()

    def close_window(self):
        self.main.destroy()

    
