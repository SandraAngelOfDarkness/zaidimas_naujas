from tkinter import *
import webbrowser
from PIL import ImageTk, Image
#from lengvas import *

class Sandra():
    def __init__(self, main):
        self.main = main
        self.main.title("Žaidimai")
        self.f_demo = Frame(self.main)
        self.l_pasiulymai = Label(self.f_demo, text="Poilsis")
        #self.b_lengvas = Button(self.f_demo, width=30, text="Atsipalaiduokime", command=self.run_lengvas)
        self.b_close = Button(self.f_demo, width=30, text="Uzdaryti", command=self.close_window)
        #self.f_demo(Tk)
        #self.f_demo.geometry("1000x1000")
        ##self.l_paveiksliukas = Label(self.main, image=photo)
        #self.b_linkas = Button(self.f_demo, text="mano kodas?", width=10, command=self.open_sandra_github)
        
        #self.l_paveiksliukas.pack(side=TOP, fill=BOTH, expand=YES)
        #self.b_linkas.pack()
        self.l_pasiulymai.pack(side=TOP)
        self.b_close.pack()
        #self.b_lengvas.pack()
        self.f_demo.pack(side=BOTTOM)

        self.main.mainloop()

    #def open_sandra_github(self):
        #webbrowser.open_new_tab("")


    #def run_lengvas(self):
        #self.window_lengvas = Toplevel(self.main)
        #self.app = Lengvas(self.window_lengvas)

    def close_window(self):
        self.main.destroy()

    
