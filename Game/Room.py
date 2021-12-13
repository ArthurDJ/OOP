from Bag import *
from NPC import *
import random
import unittest

"""
    Create a room described "description". Initially, it has
    no exits. 'description' is something like 'kitchen' or
    'an open court yard'
"""


class Room(Bag):

    def __init__(self, description=None, isShop=False):
        """
            Constructor method
        :param description: text description for this room
        """
        Bag.__init__(self, MaxWeight=1000000000000)
        self.description = description
        self.exits = {}  # Dictionary
        self.Monster = []
        self.setMonster()
        self.isShop = isShop

    def setMonster(self):
        MonsterNum = random.randint(3, 5)
        # print(MonsterNum)
        for _ in range(MonsterNum):
            MonsterLevel = random.randint(1, 3)
            self.Monster.append(Monster(Level=MonsterLevel))

    def showMonster(self):
        if self.Monster:
            print("%2s%8s%8s%8s%5s" % ("No", "Name", "Attack", "Defend", "HP"))
            Num = 1
            for M in self.Monster:
                print("%2s%8s%8s%8s%5s" % (Num, M.Name, M.Attack, M.Defend, M.HealthPoint))
                Num += 1

    def setExitbyDirection(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room)
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def setExit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            Convert numbers(Axis) to directions
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def getShortDescription(self):
        """
            Fetch a short text description
        :return: text description
        """
        return self.description

    def getLongDescription(self):
        """
            Fetch a longer description including available exits
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.getExits()} '

    def getExits(self):
        """
            Fetch all available exits as a list
        :return: list of all available exits
        """
        allExits = self.exits.keys()
        return list(allExits)

    def getExit(self, direction):
        """
            Fetch an exit in a specified direction
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Room(description=None)

    def test1(self):
        self.test.showMonster()
