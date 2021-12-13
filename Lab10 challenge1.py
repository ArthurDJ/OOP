import tkinter as tk
from tkinter import messagebox
from tkinter import Button
from TicTacToeModel import TicTacToeModel


class TicTacToeGUI:

    def __init__(self, root):
        # Create the model instance ...
        self.model = TicTacToeModel()

        # Create a 2D list to hold an array of buttons ...
        self.b = []
        for row in range(self.model.boardSize):
            q = []
            for col in range(self.model.boardSize):
                q.append(None)
            self.b.append(q)
        # You can now address b like a 2D matrix e.g. b[0][0]

        # Create the GUI .....
        menubar = tk.Menu()
        menubar.add_command(label='Quit', command=root.destroy)
        menubar.add_command(label='Reset', command=self.resetGUI)
        root.config(menu=menubar)
        self.frame1 = tk.Frame(root, width=400, height=300, bg="GREY", borderwidth=2)
        self.createGUIAssets()
        self.frame1.pack()
        messagebox.showinfo("Hello", "Human player to start!")

    def createGUIAssets(self):
        for x in range(self.model.boardSize):
            self.frame1.columnconfigure(x, pad=20)
            self.frame1.grid_rowconfigure(x, pad=20)

        for row in range(self.model.boardSize):
            for col in range(self.model.boardSize):
                self.b[row][col] = Button(self.frame1, text='', bg='WHITE',
                                          relief='groove', borderwidth=20,
                                          height=3, width=8,
                                          command=lambda row=row, col=col: self.takeTurn(row, col))
                self.b[row][col].grid(row=row, column=col)

    def takeTurn(self, row, col):
        if not self.model.playSpace(row, col):
            return
        else:
            self.b[row][col].configure(bg="Green")
            status = self.model.checkWinStatus()
            if status == 1:  # Player win
                messagebox.showinfo("Result", "Player wins!!!!")
                self.resetGUI()
            elif status == 0:  # Draw
                messagebox.showinfo("Result", "Draw!!!!")
                self.resetGUI()
            elif status == -2:  # On going ...
                (r, c) = self.model.computerTurn()
                self.b[r][c].configure(bg='red')
                if self.model.checkWinStatus() == -1:
                    messagebox.showinfo("Result", "Computer wins!!!!")
                    self.resetGUI()
            else:
                # Should not get here ...
                pass

    def resetGUI(self):
        for row in range(self.model.boardSize):
            for col in range(self.model.boardSize):
                self.b[row][col].configure(bg='WHITE')
        # And reset the model ...
        self.model.resetBoard()


def main():
    win = tk.Tk()  # Create a window
    win.title("TicTacToe")  # Set window title
    win.geometry("400x380")  # Set window size
    win.resizable(False, False)  # Both x and y dimensions ...

    # Create the GUI as a Frame
    # and attach it to the window ...
    myApp = TicTacToeGUI(win)

    # Call the GUI mainloop ...
    win.mainloop()


if __name__ == "__main__":
    main()
