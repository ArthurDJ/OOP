# Solution for the simple random maze search 1 problem

import random
import queue


def setupMaze():
    """ Setup an 8x8 max
        0 is  square we can move through, 1 is a rock"""
    return \
        [[0, 1, 0, 0, 1, 1, 0, 1], \
         [0, 1, 1, 0, 0, 1, 0, 1], \
         [0, 0, 0, 0, 0, 1, 0, 1], \
         [0, 0, 1, 0, 0, 1, 0, 1], \
         [1, 0, 1, 0, 0, 0, 0, 0], \
         [1, 0, 0, 0, 0, 1, 1, 0], \
         [0, 0, 1, 0, 0, 1, 0, 0], \
         [1, 1, 1, 1, 0, 0, 0, 0], \
         ]


def setupVis(n):
    return [[0 for i in range(n)] for j in range(n)]


def findPath(maze, location):
    """Find a way through the maze using simple random search"""
    path = queue.Queue()
    possibleDirections = ['N', 'S', 'E', 'W']
    rand = random.randint(0, 3)
    direction = possibleDirections[rand]
    while location != (7, 7):
        r, c = location
        if direction == 'N' and r - 1 != -1 and maze[r - 1][c] != 1:
            # path.append('North')
            path.put('North')
            r -= 1
            location = r, c
        elif direction == 'S' and r + 1 != 8 and maze[r + 1][c] != 1:
            # path.append('South')
            path.put('South')
            r += 1
            location = r, c
        elif direction == 'E' and c + 1 != 8 and maze[r][c + 1] != 1:
            # path.append('East')
            path.put('East')
            c += 1
            location = r, c
        elif direction == 'W' and c - 1 != -1 and maze[r][c - 1] != 1:
            # path.append('West')
            path.put('West')
            c -= 1
            location = r, c
        else:
            rand = random.randint(0, 3)
            direction = possibleDirections[rand]
    return path


def displayPath(path):
    """Takes a stack with all the directions we took ..."""
    while not path.empty():
        print(path.get())


def main():
    maze = setupMaze()  # maze is a 2D list
    Vis = setupVis(8)
    initialLocation = 0, 0  # 2-tuple to hold current location as (row, column)

    # Functions for you to implement ...
    # path should be a stack returned by findPath() ...

    path = findPath(maze, initialLocation)
    displayPath(path)


if __name__ == "__main__":
    main()
