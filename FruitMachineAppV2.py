# In this example, we use a grid layout, but the App class
# does not subclass tk.Frame. Instead, it creates its own
# instance of tk.Frame and installs it as a 1x1 grid in
# its root (i.e. the window).

# This approach is more useful where the App will have multiple
# frames in a single window.

import tkinter as tk
from tkinter import messagebox
from tkinter import TOP, BOTH, LEFT, RIGHT, BOTTOM
from PIL import ImageTk, Image
import random


class App():

    # Creates a Frame for the application
    # and populates the GUI ...
    def __init__(self, root):
        self.gameFrame = tk.Frame(root, width=400, height=300)
        # Now we add two menu options to the window ...
        menubar = tk.Menu()
        menubar.add_command(label="Quit", command=root.destroy)
        menubar.add_command(label="About", command=self.showAbout)
        root.config(menu=menubar)

        # root has 1 row and 1 column  ...
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        self.gameFrame.grid(row=0, column=0)

        # Configure a grid layout with 3 columns and 3 rows
        self.gameFrame.columnconfigure(0, pad=50)
        self.gameFrame.columnconfigure(1, pad=50)
        self.gameFrame.columnconfigure(2, pad=50)
        self.gameFrame.rowconfigure(0, pad=50)
        self.gameFrame.rowconfigure(1, pad=50)
        self.gameFrame.rowconfigure(2, pad=50)

        # Set up the reels ...
        self.setupReels()

        # Add the button to spin the reels ...
        self.spin = tk.Button(self.gameFrame, text='Spin', command=self.doSpin)
        self.spin.grid(row=1, columnspan=3)

        # Add a Label at the Bottom where we can display messages ...
        self.prize = tk.Label(self.gameFrame, text='   ')
        self.prize.grid(row=2, columnspan=3)

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
        self.r1Label = tk.Label(self.gameFrame, image=self.r1)
        self.r1Label.grid(row=0, column=0)
        self.r2 = ImageTk.PhotoImage(Image.open(self.reel2Image))
        self.r2Label = tk.Label(self.gameFrame, image=self.r2)
        self.r2Label.grid(row=0, column=1)
        self.r3 = ImageTk.PhotoImage(Image.open(self.reel3Image))
        self.r3Label = tk.Label(self.gameFrame, image=self.r3)
        self.r3Label.grid(row=0, column=2)

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
            self.prize.configure(text='Jackpot!')
            messagebox.showinfo("Prize", "Jackpot!")
            # Check for any other 3 of a kind ...
        elif self.reel1 == self.reel2 and self.reel2 == self.reel3:
            self.prize.configure(text='3 of a kind!')
            # Check for any 2 of a kind ...
        elif self.reel1 == self.reel2 or self.reel2 == self.reel3 or self.reel1 == self.reel3:
            self.prize.configure(text='2 of a kind!')
        else:
            self.prize.configure(text='No win')

    def showAbout(self):
        messagebox.showinfo("About", "Fruit Machine V2!")


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
