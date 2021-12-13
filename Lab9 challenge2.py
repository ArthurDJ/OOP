import tkinter as tk
from tkinter import messagebox, Label
from tkinter import *
from PIL import ImageTk, Image
import random
from os import path


def DoHold(button):
    if button.cget('bg') == 'red':
        button.configure(bg='green2', text="Not Hold")
    else:
        button.configure(bg='red', text="Hold")


def ShowAbout():
    messagebox.showinfo("About", "A simple fruit machine application. ")


class App(tk.Frame):

    def __init__(self, win):
        super().__init__(master=win)
        self.initComponent(win)

    def initComponent(self, win):
        menubar = tk.Menu(master=win)
        menubar.add_command(label="Quit", command=self.master.destroy)
        menubar.add_command(label="About", command=ShowAbout)
        self.master.config(menu=menubar)
        # 设置行列权重，保证内建子组件会拉伸填充
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # 设置grid布局位置，并向四个方向拉伸以填充顶级窗体
        self.grid(row=0, column=0, sticky=tk.NSEW)

        # 第一行图片，第二行Hold按钮，第三行Spin按钮和奖项
        self.rowconfigure(0, pad=50)
        self.rowconfigure(1, pad=50)
        self.rowconfigure(2, pad=50)

        self.columnconfigure(0, pad=50)
        self.columnconfigure(1, pad=50)
        self.columnconfigure(2, pad=50)

        self.imgDict = {}
        self.imageDict = {'apple': 'apple.png', 'banana': 'banana.png', 'bar': 'bar.png', 'cherries': 'cherries.png',
                          'grapes': 'grapes.png', 'lemon': 'lemon.png', 'melon': 'melon.png', 'orange': 'orange.png'}

        self.r1 = 'apple'
        self.r2 = 'lemon'
        self.r3 = 'grapes'
        self.r1Label = tk.Label(self, image=self.GetImg(name=self.r1))
        self.r2Label = tk.Label(self, image=self.GetImg(name=self.r2))
        self.r3Label = tk.Label(self, image=self.GetImg(name=self.r3))

        self.r1Label.grid(row=0, column=0)
        self.r2Label.grid(row=0, column=1)
        self.r3Label.grid(row=0, column=2)

        self.spin = tk.Button(self, text='Spin', command=self.DoSpin)
        self.spin.grid(row=2, columnspan=3)

        # Add a Label at the Bottom where we can display messages ...
        self.prize = tk.Label(self, text=None)
        self.prize.grid(row=2, columnspan=1)

        self.AddHoldButtons()

    def DoSpin(self):
        if self.hold1.cget('bg') != 'red':
            self.r1 = random.choice(list(self.imageDict.keys()))
            self.r1Label.configure(image=self.GetImg(self.r1))
        if self.hold2.cget('bg') != 'red':
            self.r2 = random.choice(list(self.imageDict.keys()))
            self.r2Label.configure(image=self.GetImg(self.r2))
        if self.hold3.cget('bg') != 'red':
            self.r3 = random.choice(list(self.imageDict.keys()))
            self.r3Label.configure(image=self.GetImg(self.r3))

        ans = len(set({self.r1, self.r2, self.r3}))
        if ans == 1:
            if self.r1 == 'bar':
                self.prize.configure(text='Jackpot!')
                messagebox.showinfo("Prize", "Jackpot!")
            else:
                self.prize.configure(text='3 of a kind!')
                messagebox.showinfo("Prize", "Three of a kind!")
        elif ans == 2:
            self.prize.configure(text='2 of a kind!')
            messagebox.showinfo("Prize", "Two of a kind!")
        else:
            self.prize.configure(text='No win')

        if random.randint(0, 1) == 0:
            self.hold1.configure(state=NORMAL)
            self.hold2.configure(state=NORMAL)
            self.hold3.configure(state=NORMAL)
            self.hold1.configure(bg='green2', text="Not Hold")
            self.hold2.configure(bg='green2', text="Not Hold")
            self.hold3.configure(bg='green2', text="Not Hold")
        else:
            # Clear the hold option ...
            self.hold1.configure(bg='SystemButtonFace')
            self.hold2.configure(bg='SystemButtonFace')
            self.hold3.configure(bg='SystemButtonFace')
            self.hold1.configure(state=DISABLED)
            self.hold2.configure(state=DISABLED)
            self.hold3.configure(state=DISABLED)

    def GetImg(self, name):
        Path = f'{path.dirname(__file__)}/images/{self.imageDict[name]}'
        if Path in self.imgDict and self.imgDict[Path]:
            return self.imgDict[Path]
        Img = ImageTk.PhotoImage(Image.open(Path))
        self.imgDict[Path] = Img
        return Img

    def AddHoldButtons(self):
        self.hold1 = tk.Button(self, text='Hold', bg='SystemButtonFace', command=lambda: DoHold(self.hold1))
        self.hold1.grid(row=1, column=0)
        self.hold2 = tk.Button(self, text='Hold', bg='SystemButtonFace', command=lambda: DoHold(self.hold2))
        self.hold2.grid(row=1, column=1)
        self.hold3 = tk.Button(self, text='Hold', bg='SystemButtonFace', command=lambda: DoHold(self.hold3))
        self.hold3.grid(row=1, column=2)
        # Initially disable (grey out) the hold buttons ...
        self.hold1.configure(state=DISABLED)
        self.hold2.configure(state=DISABLED)
        self.hold3.configure(state=DISABLED)


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
