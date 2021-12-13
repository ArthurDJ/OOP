from random import randint, choice
from enum import Enum
from sysconf import *
import unittest


class MapBlock(Enum):
    Empty = 0,
    Block = 1,
    Start = 2,


class WallDirection(Enum):
    Left = 0,
    Up = 1,
    Right = 2,
    Down = 3,


class Map:
    def __init__(self, width=11, height=11):
        self.startX, self.startY = None, None
        self.devilX, self.devilY = None, None
        self.width = width
        self.height = height
        self.map = [[0 for _ in range(self.height)] for _ in range(self.width)]
        self.doRandomPrim()
        if SHOW_MAP:
            self.showMap()

    def resetMap(self, value):
        for x in range(self.width):
            for y in range(self.height):
                self.setMap(x, y, value)

    def setMap(self, x, y, value):
        try:
            if value == MapBlock.Empty:
                self.map[x][y] = 0
            elif value == MapBlock.Block:
                self.map[x][y] = 1
            elif value == MapBlock.Start:
                self.map[x][y] = 2
        except:
            print("x : %d, y : %d, value : %s" % (x, y, value.name))

    def isVisited(self, x, y):
        return self.map[x][y] != 1

    def showMap(self):
        for row in self.map:
            s = ''
            for entry in row:
                if entry == 0:
                    s += ' 0'
                elif entry == 1:
                    s += ' #'
                elif entry == 2:
                    s += ' X'
            print(s)

    # find unvisited adjacent entries of four possible entris
    # then add random one of them to checklist and mark it as visited
    def checkAdjacentPos(self, x, y, width, height, checklist):
        directions = []
        if x > 0:
            if not self.isVisited(2 * (x - 1) + 1, 2 * y + 1):
                directions.append(WallDirection.Left)

        if y > 0:
            if not self.isVisited(2 * x + 1, 2 * (y - 1) + 1):
                directions.append(WallDirection.Up)

        if x < width - 1:
            if not self.isVisited(2 * (x + 1) + 1, 2 * y + 1):
                directions.append(WallDirection.Right)

        if y < height - 1:
            if not self.isVisited(2 * x + 1, 2 * (y + 1) + 1):
                directions.append(WallDirection.Down)

        if len(directions):
            direction = choice(directions)
            # print("(%d, %d) => %s" % (x, y, str(direction)))
            if direction == WallDirection.Left:
                self.setMap(2 * (x - 1) + 1, 2 * y + 1, MapBlock.Empty)
                self.setMap(2 * x, 2 * y + 1, MapBlock.Empty)
                checklist.append((x - 1, y))
            elif direction == WallDirection.Up:
                self.setMap(2 * x + 1, 2 * (y - 1) + 1, MapBlock.Empty)
                self.setMap(2 * x + 1, 2 * y, MapBlock.Empty)
                checklist.append((x, y - 1))
            elif direction == WallDirection.Right:
                self.setMap(2 * (x + 1) + 1, 2 * y + 1, MapBlock.Empty)
                self.setMap(2 * x + 2, 2 * y + 1, MapBlock.Empty)
                checklist.append((x + 1, y))
            elif direction == WallDirection.Down:
                self.setMap(2 * x + 1, 2 * (y + 1) + 1, MapBlock.Empty)
                self.setMap(2 * x + 1, 2 * y + 2, MapBlock.Empty)
                checklist.append((x, y + 1))
            return True
        else:
            # if not find any unvisited adjacent entry
            return False

    # random prim algorithm
    def randomPrim(self, width, height):
        self.startX, self.startY = randint(0, width - 1), randint(0, height - 1)
        self.devilX, self.devilY = randint(0, width - 1), randint(0, height - 1)
        # print("start(%d, %d)" % (self.startX, self.startY))
        # self.setMap(self.startX, self.startY, MapBlock.Start)
        self.setMap(2 * self.startX + 1, 2 * self.startY + 1, MapBlock.Start)
        checklist = list()
        checklist.append((self.startX, self.startY))
        while len(checklist):
            # select a random entry from checklist
            entry = choice(checklist)
            if not self.checkAdjacentPos(entry[0], entry[1], width, height, checklist):
                # the entry has no unvisited adjacent entry, so remove it from checklist
                checklist.remove(entry)

    # set all entries of map to wall
    def doRandomPrim(self):
        self.resetMap(MapBlock.Block)
        self.randomPrim((self.width - 1) // 2, (self.height - 1) // 2)


class TestMap(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Map(Width, Height)

    def test1(self):
        self.test.showMap()
