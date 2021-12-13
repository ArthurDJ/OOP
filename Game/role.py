import math
import random
from NPC import *
from sysconf import *


# 和怪物战斗
def Fight(Hero: object, Monster: object, TextUI):
    """
        Hero Fight with Monster.
    :param Hero: get a Hero object
    :param Monster: get a Monster object
    :param TextUI: Displays text to the console
    :return: the HP Hero lost or lose
    """
    # 怪物对英雄攻击
    Hurt_Hero = Monster.Attack - Hero.Defend
    # 英雄对怪物攻击
    Hurt_Monster = Hero.Attack - Monster.Defend
    # 英雄无法对怪物破防或战斗结束英雄死亡
    if Hurt_Monster <= 0 or Monster.HealthPoint <= Hurt_Hero * math.ceil(Monster.HealthPoint / Hurt_Monster):
        return -1
    # 英雄无法被破防且可以破怪物防御,战斗结束，直接获得金币
    elif Hurt_Hero <= 0 < Hurt_Monster:
        return 0
    # 掉血胜利
    else:
        return Monster.HealthPoint - (Hurt_Hero * math.ceil(Monster.HealthPoint / Hurt_Monster))


# 判定升级
def LevelUp(Hero):
    """
    Check Hero Level up or not
    and give Hero some Attributes
    :param Hero:
    :return:
    """
    Up = False
    while Hero.Experience >= Hero.Level * LevelNeed:
        Hero.Experience -= Hero.Level * LevelNeed
        Hero.Level += 1
        Hero.Attack += Hero.Level * 10
        Hero.Defend += Hero.Level * 10
        Hero.HealthPoint += Hero.Level * LevelNeed
        print("You have risen 1 level.")
        Up = True
    return Up


def BattleSettlement(Hero, Monster, TextUI=TextUI()):
    State = Fight(Hero, Monster, TextUI)
    if State == -1:
        TextUI.printtoTextUI("You Dead in Battle with %s!" % Monster.Name)
        TextUI.printtoTextUI("Game Over!")
        exit()
    else:
        Hero.HealthPoint -= State
        Gold_get = Monster.Gold * random.randint(1, Monster.Level)
        Hero.Gold += Gold_get
        Exp_Get = Monster.Level * MonsterExp
        Hero.Experience += Exp_Get
        TextUI.printtoTextUI("You Lose %s HP in Battle with %s." % (State, Monster.Name))
        TextUI.printtoTextUI("You Get %s Gold." % Gold_get)
        TextUI.printtoTextUI("You Get %s Experience." % Exp_Get)
        LevelUp(Hero)

