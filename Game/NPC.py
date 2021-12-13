import math
import random
import unittest

from sysconf import *
from TextUI import *
from items import *
from Bag import Bag


# 角色类：
class Npc:
    def __init__(self, Name=Name, Attack=Mon_Attack, Defend=Mon_Defend, HealthPoint=Mon_HealthPoint):
        self.Name = Name
        self.Attack = Attack
        self.Defend = Defend
        self.HealthPoint = HealthPoint

    def ShowName(self, TextUI):
        TextUI.printtoTextUI("Your name is %s." % self.Name)

    def ShowAttack(self, TextUI):
        TextUI.printtoTextUI("%s's Attack is %s." % (self.Name, self.Attack))

    def ShowDefend(self, TextUI):
        TextUI.printtoTextUI("%s's Defend is %s." % (self.Name, self.Defend))

    def ShowHealthPoint(self, TextUI):
        TextUI.printtoTextUI("%s's HealthPoint is %s." % (self.Name, self.HealthPoint))

    def GetName(self):
        return self.Name

    def GetAttack(self):
        return self.Attack

    def GetDefend(self):
        return self.Defend

    def GetHealthPoint(self):
        return self.HealthPoint


# 英雄类：
class Hero(Npc, Bag):
    def __init__(self, Level=Level, Experience=Experience):
        # 初始化父类
        Npc.__init__(self)
        Bag.__init__(self, isHero=True)
        self.Attack = Hero_Attack
        self.Defend = Hero_Defend
        self.HealthPoint = Hero_HealthPoint
        self.Level = Level
        self.Experience = Experience

    def ShowAttribute(self, TextUI):
        self.ShowName(TextUI)
        self.ShowHealthPoint(TextUI)
        self.ShowAttack(TextUI)
        self.ShowDefend(TextUI)

    def ShowLevel(self, TextUI=TextUI()):
        TextUI.printtoTextUI("%s's Level is %s." % (self.Name, self.Level))
        TextUI.printtoTextUI("%s need %s Experience to get to the next level." %
                             (self.Name, self.Level * LevelNeed - self.Experience))

    def GetLevel(self):
        return self.Level

    def GetExperience(self):
        return self.Experience

    def UseThing(self, Name, Number, TextUI=TextUI()):
        Number = int(Number)
        if Number < 0:
            TextUI.printtoTextUI("DO NOT DREAM~~~~")
        elif Name in self.Dict:
            if 0 < Number <= self.Dict[Name]['num']:
                useStr = ITEMS_DATA["itemEffect"][Name] + str(Number)
                # print(useStr)
                exec(useStr)
                self.Dict[Name]['num'] -= Number
                TextUI.pringUseThing(Name, Number)
            else:
                TextUI.printNotenough(Name)
        else:
            TextUI.printNoThing()


# 怪物类：
class Monster(Npc):
    def __init__(self, Gold=Gold, Level=Level):
        # 初始化父类
        Npc.__init__(self)
        self.Gold = Gold
        self.Level = Level
        strLevel = 'Level' + str(Level)
        self.Name = random.choice(MonsterName[strLevel])
        self.Attack = int(self.Attack * random.uniform(Level - 0.9, Level))
        self.Defend = int(self.Defend * random.uniform(Level - 0.9, Level))
        self.HealthPoint = int(self.HealthPoint * random.uniform(Level - 0.9, Level))


class TestHero(unittest.TestCase):
    def setUp(self):
        self.test = Hero()
        self.UI = TextUI()

    def test1(self):
        Name = "red"
        Num = 1
        self.test.Show(self.UI)
        self.test.ShowAttribute(self.UI)
        self.test.UseThing(Name, Num, self.UI)
        self.test.ShowAttribute(self.UI)
