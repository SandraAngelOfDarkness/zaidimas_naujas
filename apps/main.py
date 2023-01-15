from tkinter import *
from apps.sandra import Sandra

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="♥ Sveiki atvykę ♥ \n" "♥ Tegul sekmė visada Jus lydi ♥")
        self.b_sandra = Button(self.f_catalog, width=10, text="MENIU", command=self.run_sandra)

        self.l_pasirinkimai.pack(side=TOP)
        self.b_sandra.pack()
        self.f_catalog.pack()

    def run_sandra(self):
        self.window_sandra = Toplevel(self.main)
        self.app = Sandra(self.window_sandra)

