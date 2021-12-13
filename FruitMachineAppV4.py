# In this example, we use a grid layout, and the App class
# subclasses tk.Frame.

# This approach is more useful where the App will have multiple
# frames in a single window. It then installs itself in a 1x1
# grid in the root (the window).

# This approach is only generally suited where there is a single
# frame for the window.

# This version adds the hold buttons as described in the lab sheet.

import tkinter as tk
from tkinter import messagebox
from tkinter import TOP, BOTH, LEFT, RIGHT, BOTTOM, DISABLED, NORMAL
from PIL import ImageTk, Image
import random


def doHold(b):
    # Change the colour of button b ...
    b.configure(bg='red')


def showAbout():
    messagebox.showinfo("About", "Fruit Machine V4\nHold when buttons are green!")


class App(tk.Frame):

    # Creates a Frame for the application
    # and populates the GUI ...
    def __init__(self, root):
        super().__init__(master=root)

        # Now we add two menu options to the window ...
        menubar = tk.Menu()
        menubar.add_command(label="Quit", command=root.destroy)
        menubar.add_command(label="About", command=showAbout)
        root.config(menu=menubar)

        # root has 1 row and 1 columns ...
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        self.grid(row=0, column=0)

        # Configure a grid layout with 3 columns and 4 rows
        self.columnconfigure(0, pad=50)
        self.columnconfigure(1, pad=50)
        self.columnconfigure(2, pad=50)
        self.rowconfigure(0, pad=50)
        self.rowconfigure(1, pad=50)
        self.rowconfigure(2, pad=50)
        self.rowconfigure(3, pad=50)

        # Set up the reels ...
        self.setupReels()

        # Add the hold buttons ...
        self.addHoldButtons()

        # Add the button to spin the reels ...
        self.spin = tk.Button(self, text='Spin', command=self.doSpin)
        self.spin.grid(row=2, columnspan=3)

        # Add a Label at the Bottom where we can display messages ...
        self.prize = tk.Label(self, text=None)
        self.prize.grid(row=3, columnspan=3)

        self.mainloop()

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
        self.r1Label.grid(row=0, column=0)
        self.r2 = ImageTk.PhotoImage(Image.open(self.reel2Image))
        self.r2Label = tk.Label(self, image=self.r2)
        self.r2Label.grid(row=0, column=1)
        self.r3 = ImageTk.PhotoImage(Image.open(self.reel3Image))
        self.r3Label = tk.Label(self, image=self.r3)
        self.r3Label.grid(row=0, column=2)

    def addHoldButtons(self):
        self.hold1 = tk.Button(self, text='Hold', bg='SystemButtonFace', command=lambda: doHold(self.hold1))
        self.hold1.grid(row=1, column=0)
        self.hold2 = tk.Button(self, text='Hold', bg='SystemButtonFace', command=lambda: doHold(self.hold2))
        self.hold2.grid(row=1, column=1)
        self.hold3 = tk.Button(self, text='Hold', bg='SystemButtonFace', command=lambda: doHold(self.hold3))
        self.hold3.grid(row=1, column=2)
        # Initially disable (grey out) the hold buttons ...
        self.hold1.configure(state=DISABLED)
        self.hold2.configure(state=DISABLED)
        self.hold3.configure(state=DISABLED)

    def doSpin(self):
        # Choose new reel values and update the images ...
        # Don't spin a reel if the hold button is ON (red)
        if self.hold1.cget("bg") != 'red':
            self.reel1 = random.choice(list(self.imageDict.keys()))
            self.reel1Image = ImageTk.PhotoImage(Image.open(f'D:/study/python/OOP/images/{self.imageDict[self.reel1]}'))
            self.r1Label.configure(image=self.reel1Image)
        if self.hold2.cget("bg") != 'red':
            self.reel2 = random.choice(list(self.imageDict.keys()))
            self.reel2Image = ImageTk.PhotoImage(Image.open(f'D:/study/python/OOP/images/{self.imageDict[self.reel2]}'))
            self.r2Label.configure(image=self.reel2Image)
        if self.hold3.cget("bg") != 'red':
            self.reel3 = random.choice(list(self.imageDict.keys()))
            self.reel3Image = ImageTk.PhotoImage(Image.open(f'D:/study/python/OOP/images/{self.imageDict[self.reel3]}'))
            self.r3Label.configure(image=self.reel3Image)
        print(self.r1Label.__dict__)
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

        # Now decide whether we give the player a HOLD condition ...
        h = random.randrange(4)  # 0 to 4 ...
        if h == 0:
            self.hold1.configure(state=NORMAL)
            self.hold2.configure(state=NORMAL)
            self.hold3.configure(state=NORMAL)
            self.hold1.configure(bg='green2')
            self.hold2.configure(bg='green2')
            self.hold3.configure(bg='green2')
        else:
            # Clear the hold option ...
            self.hold1.configure(bg='SystemButtonFace')
            self.hold2.configure(bg='SystemButtonFace')
            self.hold3.configure(bg='SystemButtonFace')
            self.hold1.configure(state=DISABLED)
            self.hold2.configure(state=DISABLED)
            self.hold3.configure(state=DISABLED)


def main():
    win = tk.Tk()  # Create a window
    win.title("Fruit Machine")  # Set window title
    win.geometry("400x400")  # Set window size
    win.resizable(False, False)  # Both x and y dimensions ...

    # Create the GUI as a Frame
    # and attach it to the window ...
    myApp = App(win)

    # Call the GUI mainloop ...
    win.mainloop()


if __name__ == "__main__":
    main()
