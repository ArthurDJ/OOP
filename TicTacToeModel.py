import numpy as np
import random


class TicTacToeModel:
    """ The board is represented as 2D numpy array.
        A player marks their space with a 1, the
        computer with a -1"""

    def __init__(self):
        """Create the board as a 2D matrix"""
        self.resetBoard()

    def resetBoard(self):
        self.boardSize = 3
        a = (self.boardSize, self.boardSize)
        self.board = np.zeros(a)

    def playSpace(self, row, col):
        """User plays a space
        Return True if space can be played, False otherwise"""
        if row > self.boardSize or row < 0 \
                or col > self.boardSize or col < 0:
            return False
        else:
            # Check if space is occupied ...
            if self.board[row][col] != 0:
                return False
            else:
                self.board[row][col] = 1
                return True

    def checkWinStatus(self):
        """ Looks for 3 in a row, column or diagonal
            Return 0 if draw, 1 if the player has won
            and -1 if the computer has won, and -2 is the game is
            ongoing"""
        # Check the columns ...
        for row in range(self.boardSize):
            sum = 0
            for col in range(self.boardSize):
                sum += self.board[row][col]
            if sum == 3:
                return 1
            elif sum == -3:
                return -1
        # Check the rows ...
        for col in range(self.boardSize):
            sum = 0
            for row in range(self.boardSize):
                sum += self.board[row][col]
            if sum == 3:
                return 1
            elif sum == -3:
                return -1

        # Check the diagonals ...
        sum1 = 0
        sum2 = 0
        for diag in range(self.boardSize):
            sum1 += self.board[diag][diag]
            sum2 += self.board[diag][self.boardSize - 1 - diag]
        if sum1 == 3 or sum2 == 3:
            return 1
        elif sum1 == -3 or sum2 == -3:
            return -1

        # Check for incomplete game ...
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                if self.board[row][col] == 0:
                    return -2

        # If we get here, it's a draw ...
        return 0

    def computerTurn(self):
        """ The computer chooses an unoccupied
            space at random. Returns a tuple
            (row, col) when chosen"""
        # To prevent infinite loops ....
        if self.checkWinStatus() != -2:
            return (-1, -1)
        played = False

        while played == False:
            row = random.randrange(self.boardSize)
            col = random.randrange(self.boardSize)
            if self.board[row][col] == 0:
                self.board[row][col] = -1
                played = True

        return (row, col)


def main():
    # Basic check that the game works ...
    # You can expand this if you like ...
    game = TicTacToeModel()

    game.playSpace(0, 0)
    (r, c) = game.computerTurn()
    print(game.board)
    print(game.checkWinStatus())


if __name__ == "__main__":
    main()
