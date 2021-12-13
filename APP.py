from tkinter import *
import tkinter as tk


class App(tk.Frame):
    # Creates a Frame for the application
    # and populates the GUI ...
    def __init__(self, win):
        super().__init__(master=win)
        self.pack()
        # Add a single label ...
        self.label1 = tk.Label(self, bg='black', fg='white', text="My First Label")
        self.label1.pack(padx=20, pady=20)
        # Now we add two top level menu options
        menubar = tk.Menu(master=win)
        menubar.add_command(label="Quit", command=self.master.destroy)
        # The second option is a cascade sub menu ...
        changeTextMenu = tk.Menu()
        menubar.add_cascade(label="ChangeText", menu=changeTextMenu)
        self.master.config(menu=menubar)
        # Add options to the changeTextMenu sub menu ...
        changeTextMenu.add_command(label="Option1",
                                   command=lambda: self.doChangeText('option 1'))
        changeTextMenu.add_command(label="Option2",
                                   command=lambda: self.doChangeText('option 2'))

    def doChangeText(self, newText):
        self.label1.configure(text=newText)


def main():
    win = tk.Tk()
    win.title("Example")
    win.geometry("400x200")
    win.resizable(False, False)

    Myapp = App(win)
    win.mainloop()


if __name__ == '__main__':
    main()
