from tkinter import *
from apps.main import MainApp
from PIL import ImageTk, Image

def run_main_app():
    root = Tk()
    #icon = ImageTk.PhotoImage(Image.open('salad.ico'))
    #root.call('wm', 'iconphoto', root._w, icon)
    ## root.iconbitmap(bitmap=r'salad.ico')
    root.title("PAŽAISKIME" "\U0001F609")
    root.geometry("500x500")
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_main_app()