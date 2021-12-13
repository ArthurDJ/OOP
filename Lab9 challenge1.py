import tkinter as tk
from tkinter import messagebox, Label
from tkinter import TOP, BOTH, LEFT, RIGHT, BOTTOM
from PIL import ImageTk, Image
import random


def ShowAbout():
    messagebox.showinfo("About", "A simple fruit machine application. ")


class App(tk.Frame):

    def __init__(self, win):
        self.imgDict = {}
        super().__init__(master=win)

        self.pack()

        menubar = tk.Menu(master=win)
        menubar.add_command(label="Quit", command=self.master.destroy)
        menubar.add_command(label="About", command=ShowAbout)
        self.master.config(menu=menubar)

        self.imageDict = {'apple': 'apple.png', 'banana': 'banana.png', 'bar': 'bar.png', 'cherries': 'cherries.png',
                          'grapes': 'grapes.png', 'lemon': 'lemon.png', 'melon': 'melon.png', 'orange': 'orange.png'}

        r1 = 'apple'
        r2 = 'lemon'
        r3 = 'grapes'
        self.r1Label = tk.Label(self, image=self.GetImg(name=r1))
        self.r2Label = tk.Label(self, image=self.GetImg(name=r2))
        self.r3Label = tk.Label(self, image=self.GetImg(name=r3))

        self.r1Label.pack(side=LEFT)
        self.r2Label.pack(side=LEFT)
        self.r3Label.pack(side=LEFT)

        self.spin = tk.Button(self, text='Spin', command=self.doSpin)
        self.spin.pack(side=LEFT)

    def doSpin(self):
        r1 = random.choice(list(self.imageDict.keys()))
        r2 = random.choice(list(self.imageDict.keys()))
        r3 = random.choice(list(self.imageDict.keys()))
        self.r1Label.configure(image=self.GetImg(r1))
        self.r2Label.configure(image=self.GetImg(r2))
        self.r3Label.configure(image=self.GetImg(r3))

        if len(set({r1, r2, r3})) == 1:
            if r1 == 'bar':
                messagebox.showinfo("Prize", "Jackpot!")
            else:
                messagebox.showinfo("Prize", "Three of a kind!")
        elif len(set({r1, r2, r3})) == 2:
            messagebox.showinfo("Prize", "Two of a kind!")

    def GetImg(self, name):
        Path = f'D:/study/python/OOP/images/{self.imageDict[name]}'
        if Path in self.imgDict and self.imgDict[Path]:
            return self.imgDict[Path]
        Img = ImageTk.PhotoImage(Image.open(Path))
        self.imgDict[Path] = Img
        return Img


def main():
    win = tk.Tk()  # Create a window
    win.title("Fruit Machine")  # Set window title
    win.geometry("400x300")  # Set window size
    win.resizable(False, False)  # Both x and y dimensions ...

    # Create the GUI as a Frame
    # and attach it to the window ...
    myApp = App(win)

    # Call the GUI mainloop ...
    win.mainloop()


if __name__ == "__main__":
    main()
