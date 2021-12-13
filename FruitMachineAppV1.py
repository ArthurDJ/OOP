# In this version, we use a pack layout.
# Control of positioning can be a nuisance with
# this very simple layout manager

import tkinter as tk
from tkinter import messagebox
from tkinter import TOP, BOTH, LEFT, RIGHT, BOTTOM
from PIL import ImageTk, Image
import random


def showAbout():
    messagebox.showinfo("About", "Fruit Machine!")


class App(tk.Frame):
    # Creates a Frame for the application
    # and populates the GUI ...
    def __init__(self, win):

        super().__init__(master=win)
        self.pack()

        # Now we add two menu options ...
        menubar = tk.Menu(master=win)
        menubar.add_command(label="Quit", command=self.master.destroy)
        menubar.add_command(label="About", command=showAbout)
        self.master.config(menu=menubar)

        # Set up the reels ...
        self.setupReels()

        # Add the button to spin the reels ...
        self.spin = tk.Button(self, text='Spin', command=self.doSpin)
        self.spin.pack(side=LEFT)

    def setupReels(self):
        self.imageDict = {'apple': 'apple.png', 'banana': 'banana.png', 'bar': 'bar.png', 'cherries': 'cherries.png',
                          'grapes': 'grapes.png', 'lemon': 'lemon.png', 'melon': 'melon.png', 'orange': 'orange.png'}
        self.reel1 = 'apple'
        self.reel2 = 'lemon'
        self.reel3 = 'grapes'
        self.reel1Image = f'D:/study/python/OOP/images/{self.imageDict[self.reel1]}'
        self.reel2Image = f'D:/study/python/OOP/images/{self.imageDict[self.reel2]}'
        self.reel3Image = f'D:/study/python/OOP/images/{self.imageDict[self.reel3]}'

        # Now we add images. These are stored in the images/ folder
        self.r1 = ImageTk.PhotoImage(Image.open(self.reel1Image))
        self.r1Label = tk.Label(self, image=self.r1)
        self.r1Label.pack(side=LEFT)
        self.r2 = ImageTk.PhotoImage(Image.open(self.reel2Image))
        self.r2Label = tk.Label(self, image=self.r2)
        self.r2Label.pack(side=LEFT)
        self.r3 = ImageTk.PhotoImage(Image.open(self.reel3Image))
        self.r3Label = tk.Label(self, image=self.r3)
        self.r3Label.pack(side=LEFT)

    def doSpin(self):
        # Choose new reel values and update the images ...
        self.reel1 = random.choice(list(self.imageDict.keys()))
        self.reel2 = random.choice(list(self.imageDict.keys()))
        self.reel3 = random.choice(list(self.imageDict.keys()))
        self.reel1Image = ImageTk.PhotoImage(Image.open(f'D:/study/python/OOP/images/{self.imageDict[self.reel1]}'))
        self.r1Label.configure(image=self.reel1Image)
        self.reel2Image = ImageTk.PhotoImage(Image.open(f'D:/study/python/OOP/images/{self.imageDict[self.reel2]}'))
        self.r2Label.configure(image=self.reel2Image)
        self.reel3Image = ImageTk.PhotoImage(Image.open(f'D:/study/python/OOP/images/{self.imageDict[self.reel3]}'))
        self.r3Label.configure(image=self.reel3Image)

        # Now check whether we have a winning condition
        # First, check for 3 bars ...
        if self.reel1 == self.reel2 and self.reel2 == self.reel3 and self.reel3 == 'bar':
            messagebox.showinfo("Prize", "Jackpot!")
            # Check for any other 3 of a kind ...
        elif self.reel1 == self.reel2 and self.reel2 == self.reel3:
            messagebox.showinfo("Prize", "Three of a kind!")
            # Check for any 2 of a kind ...
        elif self.reel1 == self.reel2 or self.reel2 == self.reel3 or self.reel1 == self.reel3:
            messagebox.showinfo("Prize", "Two of a kind!")


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
