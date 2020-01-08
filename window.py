# coding:utf-8
from tkinter import *

class Window():
    def __init__(self):
        self.frame = Tk()
        self.frame.title('Test window')
        self.frame.geometry('500x300')

    def Search(self):
        chindWindow = Tk()
        chindWindow.mainloop()

    def Menu(self):
        menubar = Menu(self.frame)
        self.frame.config(menu = menubar)
        menubar.add_cascade(label='Search', command=self.Search)
        self.frame.mainloop()

def main():
    a = Window()
    a.Menu()

if __name__ == '__main__':
    main()
