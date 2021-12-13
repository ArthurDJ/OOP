import copy

from sysconf import *
from TextUI import *
from items import *
from tool import *
import unittest


# 背包类
class Bag:
    def __init__(self, Dict=Dict, Gold=Gold, MaxWeight=MaxWeight, isHero=False):
        self.Dict = copy.deepcopy(Dict)
        self.Gold = Gold
        self.Weight = 0
        self.MaxWeight = MaxWeight
        self.isHero = isHero

    def GetTotalWeight(self):
        """
        Calculate the total weight in the backpack
        :return:Total weight in backpack
        """
        w = 0
        for key in self.Dict.keys():
            w += self.Dict[key]['num'] * self.Dict[key]['weight']
        return w

    def ThrowThing(self, Name, Number, Room, TextUI=TextUI()):
        Number = int(Number)
        # Thing in your bag
        if Number < 0:
            TextUI.printDream()
        elif CheckUpper(Name, "gold"):
            if Number <= self.Gold:
                self.Gold -= Number
                Room.Gold += Number
                self.Show(TextUI)
            else:
                TextUI.printNotenough(Name)
        elif Name in self.Dict:
            NowNumber = self.Dict[Name]['num']
            if NowNumber >= Number:
                self.Dict[Name]['num'] -= Number
                Room.Dict[Name]['num'] += Number
                TextUI.printThrowThing(Name, Number)
                self.Show(TextUI)
            else:
                TextUI.printNotenough(Name)
        else:
            TextUI.printtoTextUI("You don't have %s." % Name)

    def Pick(self, Name, Number, Room, TextUI=TextUI()):
        Number = int(Number)
        if Number < 0:
            TextUI.printDream()

        elif CheckUpper(Name, "gold"):
            if 0 <= Number <= Room.Gold:
                TextUI.printtoTextUI("You get %s Gold." % Number)
                self.Gold += Number
                Room.Gold -= Number
            else:
                TextUI.printNotenough(Name)
        elif Name in Room.Dict and Room.Dict[Name]['num'] >= Number:
            w = Number * Room.Dict[Name]['weight']
            self.Weight = self.GetTotalWeight()
            if self.Weight + w > self.MaxWeight:
                TextUI.printOutWeight()
            else:
                self.AddThing(Name, Number, TextUI)
                Room.Dict[Name]['num'] = Room.Dict[Name]['num'] - Number
                return True
        else:
            TextUI.printNoThing()

    def AddThing(self, Name, Number, TextUI=TextUI()):
        if Name in self.Dict:
            TextUI.printGetThing(Name, Number)
            # print(self.Dict[Name]['num'])
            self.Dict[Name]['num'] = Number + self.Dict[Name]['num']
            # print(self.Dict[Name]['num'])
            self.Show(TextUI)
        elif Name in ITEMS_DATA["items"]:
            TextUI.printGetThing(Name, Number)
            self.Dict[Name] = ITEMS_DATA["items"][Name]
            self.Dict[Name]['num'] = Number
            self.Show(TextUI)
        else:
            TextUI.printNoThing()

    def Show(self, TextUI):
        if not self.isHero:
            TextUI.printtoTextUI("Things in Room:")
        else:
            TextUI.printtoTextUI("Here is Your Bag:")
        TextUI.printtoTextUI("%9s%12s%10s" % ("Name", "Number", "Weight"))
        TextUI.printtoTextUI("-" * 50)
        for name in self.Dict:
            if self.Dict[name]['num'] != 0:
                TextUI.printtoTextUI(text="%12s%7s%10s" % (
                    name, self.Dict[name]['num'], self.Dict[name]['num'] * self.Dict[name]['weight']))
        if self.Gold != 0 or self.isHero:
            TextUI.printtoTextUI("%9s%10s" % ("Gold", self.Gold))
        if self.isHero:
            TextUI.printtoTextUI("Total Weight is %s.\nMax Weight is %s." %
                                 (self.GetTotalWeight(), self.MaxWeight))

    def Arrange(self):
        for k in self.Dict:
            if k['num'] == 0:
                self.Dict.pop(k)


class TestBag(unittest.TestCase):
    def setUp(self):
        self.test = Bag(isHero=True)
        self.UI = TextUI()

    def tearDown(self):
        self.test.Dict.clear()

    def test1(self):
        Name = 'blueJewel'
        bag = Bag()
        Num = 1
        self.test.Pick(Name=Name, Number=Num, Room=bag, TextUI=self.UI)

    def test2(self):
        Name = 'blueJewel'
        bag = Bag()
        Num = 1
        self.test.ThrowThing(Name=Name, Number=Num, Room=bag, TextUI=self.UI)
