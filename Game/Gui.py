import tkinter as tk
from tkinter import *
from tkinter import TOP, BOTH, X, N, LEFT, RIGHT, BOTTOM, CENTER, DISABLED, NORMAL
from tkinter.messagebox import showinfo

from PIL import ImageTk, Image
from os import path
from Game import *
from sysconf import *
from logger import *


class GUI:
    def __init__(self, root):
        self.logger = logger_config(log_path='log.txt', logging_name='Game')
        self.game = Game()
        self.frame = tk.Frame(root)
        self.frame.grid()

        menubar = tk.Menu()
        menubar.add_command(label='Quit', command=root.destroy)
        menubar.add_command(label='About', command=lambda: self.showabout())
        menubar.add_command(label='Help', command=lambda: self.showHelp())
        root.config(menu=menubar)

        self.imgDict = {}
        self.SetMapframe()
        self.SetHeroframe()
        self.SetFunction()
        self.top = tk.Toplevel()
        self.top.destroy()
        self.SetName()

    def showHelp(self):
        message = '''
                The left is the map of the game, 
                and the right is the attribute of the hero
                Use the left direction to change the hero's position.
                Use the action on the right to interact.
                '''
        title = "Help"
        showinfo(title=title, message=message)

    def showabout(self):
        message = '''
        You come to the devil's castle alone.
        The princess was locked in the attic somewhere.
        Take the sword in your hand, defeat the monster.
        Defeat the devil and save the princess.
        '''
        title = "About Game"
        showinfo(title=title, message=message)

    def SetMapframe(self):
        self.Mapframe = tk.Frame(self.frame, width=Width * MapSize, height=Height * MapSize)
        self.Mapframe.grid(row=0, column=0)
        self.Map = self.game.Map
        self.MapLabel = [[tk.Label(self.Mapframe) for _ in range(self.Map.width)] for _ in range(self.Map.height)]
        self.RefreshMapframe()

    def SetHeroframe(self):
        self.rightframe = tk.Frame(self.frame)
        self.rightframe.grid(row=0, column=1, sticky='ns', padx=10)

        self.Heroframe = tk.Frame(self.rightframe)
        self.Heroframe.grid(row=0, column=0, sticky='w')
        name = 'Head0' + str(randint(1, 5))
        self.Head = tk.Label(self.Heroframe, image=self.GetImg(name=name, resize=100))
        self.Head.grid(row=0, column=0)
        self.RefreshHeroframe()
        self.Bagframe = tk.Frame(self.rightframe)
        self.Bagframe.grid(row=1, column=0, pady=10)
        self.RefreshBagframe()

    def RefreshBagframe(self):

        LabelSize = 30

        redJeweltext = "X " + str(self.game.Hero.Dict['redJewel']['num'])
        self.redJewelLabel = tk.Label(self.Bagframe, text=redJeweltext, compound='left',
                                      image=self.GetImg(name='redJewel', resize=LabelSize))
        self.redJewelLabel.grid(row=1, column=0, sticky='w')
        self.redJewelLButton = tk.Button(self.Bagframe, text='use', command=lambda: self.UseredJewel())
        self.redJewelLButton.grid(row=1, column=1, padx=15)
        if not self.game.Hero.Dict['redJewel']['num']:
            self.redJewelLButton.configure(state=DISABLED)

        blueJeweltext = "X " + str(self.game.Hero.Dict['blueJewel']['num'])
        self.blueJewelLabel = tk.Label(self.Bagframe, text=blueJeweltext, compound='left',
                                       image=self.GetImg(name='blueJewel', resize=LabelSize))
        self.blueJewelLabel.grid(row=2, column=0, sticky='w')
        self.blueJewelButton = tk.Button(self.Bagframe, text='use', command=lambda: self.UseblueJewel())
        self.blueJewelButton.grid(row=2, column=1, padx=15)
        if not self.game.Hero.Dict['blueJewel']['num']:
            self.blueJewelButton.configure(state=DISABLED)

        redPotiontext = "X " + str(self.game.Hero.Dict['redPotion']['num'])
        self.redPotionLabel = tk.Label(self.Bagframe, text=redPotiontext, compound='left',
                                       image=self.GetImg(name='redPotion', resize=LabelSize))
        self.redPotionLabel.grid(row=3, column=0, sticky='w')
        self.redPotionButton = tk.Button(self.Bagframe, text='use', command=lambda: self.UseredPotion())
        self.redPotionButton.grid(row=3, column=1, padx=15)
        if not self.game.Hero.Dict['redPotion']['num']:
            self.redPotionButton.configure(state=DISABLED)

        expPotiontext = "X " + str(self.game.Hero.Dict['expPotion']['num'])
        self.expPotionLabel = tk.Label(self.Bagframe, text=expPotiontext, compound='left',
                                       image=self.GetImg(name='expPotion', resize=LabelSize))
        self.expPotionLabel.grid(row=4, column=0, sticky='w')
        self.expPotionButton = tk.Button(self.Bagframe, text='use',
                                         command=lambda: self.UseexpPotion())
        self.expPotionButton.grid(row=4, column=1, padx=15)
        if not self.game.Hero.Dict['expPotion']['num']:
            self.expPotionButton.configure(state=DISABLED)

        Goldtext = "Gold X " + str(self.game.Hero.Gold)
        self.GoldLabel = tk.Label(self.Bagframe, text=Goldtext, compound='left', ). \
            grid(row=5, column=0, sticky='w')

        Weighttext = "Weight : " + str(self.game.Hero.GetTotalWeight())
        self.WeightLabel = tk.Label(self.Bagframe, text=Weighttext, compound='left', ). \
            grid(row=6, column=0, sticky='w')

    def UseexpPotion(self):
        self.game.Hero.UseThing('expPotion', 1)
        self.logger.info('use 1 expPotion')
        Up = LevelUp(self.game.Hero)
        if Up:
            showinfo(message='You have upgraded!You became stronger!')
            self.logger.info('Level up')
        self.top.destroy()
        self.RefreshHeroframe()
        self.RefreshBagframe()

    def UseredPotion(self):
        self.game.Hero.UseThing('redPotion', 1)
        self.logger.info('use 1 redPotion')
        self.top.destroy()
        self.RefreshHeroframe()
        self.RefreshBagframe()

    def UseblueJewel(self):
        self.game.Hero.UseThing('blueJewel', 1)
        self.logger.info('use 1 blueJewel')
        self.top.destroy()
        self.RefreshHeroframe()
        self.RefreshBagframe()

    def UseredJewel(self):
        self.game.Hero.UseThing('redJewel', 1)
        self.logger.info('use 1 redJewel')
        self.top.destroy()
        self.RefreshHeroframe()
        self.RefreshBagframe()

    def RefreshHeroframe(self):
        Nametext = "Name : " + str(self.game.Hero.GetName())
        self.NameLabel = tk.Label(self.Heroframe, text=Nametext)
        self.NameLabel.grid(row=1, sticky='w')

        Attacktext = "Attack : " + str(self.game.Hero.GetAttack())
        self.AttackLabel = tk.Label(self.Heroframe, text=Attacktext)
        self.AttackLabel.grid(row=2, sticky='w')

        Defendtext = "Defend : " + str(self.game.Hero.GetDefend())
        self.DefendLabel = tk.Label(self.Heroframe, text=Defendtext)
        self.DefendLabel.grid(row=3, sticky='w')

        HPtext = "HP : " + str(self.game.Hero.GetHealthPoint())
        self.HPLabel = tk.Label(self.Heroframe, text=HPtext)
        self.HPLabel.grid(row=4, sticky='w')

        Leveltext = "Level : " + str(self.game.Hero.GetLevel())
        self.LevelLabel = tk.Label(self.Heroframe, text=Leveltext)
        self.LevelLabel.grid(row=5, sticky='w')

        Exptext = "Exp : " + str(self.game.Hero.GetExperience())
        self.ExpLabel = tk.Label(self.Heroframe, text=Exptext)
        self.ExpLabel.grid(row=6, sticky='w')

    def SetName(self):
        self.top = tk.Toplevel()
        l = tk.Label(self.top, text="At first, Hero, Tell me Your Name?", width=50, height=5)
        l.grid(padx=4, pady=4)
        self.text1 = tk.Entry(self.top)
        self.text1.grid(padx=5, pady=5)
        self.bo1 = tk.Button(self.top, text='ok', width=20, command=lambda: self.ChangeName(self.text1.get()))
        self.bo1.grid(padx=7, pady=7)

    def ChangeName(self, name):
        try:
            self.game.Hero.Name = name
            showinfo(message='Name success')
            self.top.destroy()
            self.RefreshHeroframe()
            self.logger.info(f'Set name as {name}')
        except:
            self.logger.error(f"ChangeName Error!")

    def GoNorth(self):
        self.doGoCommand('north')
        self.top.destroy()

    def GoSouth(self):
        self.doGoCommand('south')
        self.top.destroy()

    def GoWest(self):
        self.doGoCommand('west')
        self.top.destroy()

    def GoEast(self):
        self.doGoCommand('east')
        self.top.destroy()

    def SetFunction(self):
        self.Functionframe = tk.Frame(self.frame, width=Width * MapSize + 100, height=100)
        self.Functionframe.grid(row=1, column=0, columnspan=2, pady=10)

        self.Functionframe.rowconfigure(0, pad=20)
        self.Functionframe.rowconfigure(1, pad=20)

        for i in range(7):
            self.Functionframe.columnconfigure(i, pad=20)

        w_Size = 8
        h_Size = 3
        self.NorthButton = tk.Button(self.Functionframe, width=w_Size, height=h_Size,
                                     text='north', command=lambda: self.GoNorth())
        self.NorthButton.grid(row=0, column=1)
        self.SouthButton = tk.Button(self.Functionframe, width=w_Size, height=h_Size,
                                     text='south', command=lambda: self.GoSouth())
        self.SouthButton.grid(row=1, column=1)
        self.WestButton = tk.Button(self.Functionframe, width=w_Size, height=h_Size,
                                    text='west', command=lambda: self.GoWest())
        self.WestButton.grid(row=1, column=0)
        self.EastButton = tk.Button(self.Functionframe, width=w_Size, height=h_Size,
                                    text='east', command=lambda: self.GoEast())
        self.EastButton.grid(row=1, column=2)

        Label = tk.Label(self.Functionframe, width=w_Size, height=h_Size)
        Label.grid(row=0, column=4)

        self.pickButton = tk.Button(self.Functionframe, text='pick', width=w_Size, height=h_Size,
                                    command=lambda: self.doPick())
        self.pickButton.grid(row=0, column=5)
        self.buyButton = tk.Button(self.Functionframe, text='shop', width=w_Size, height=h_Size,
                                   command=lambda: self.doBuy())
        self.buyButton.grid(row=1, column=5)

        if not self.game.room[self.game.HeroX][self.game.HeroY].isShop:
            self.buyButton.configure(state=DISABLED)

        self.throwButton = tk.Button(self.Functionframe, text='throw', width=w_Size, height=h_Size,
                                     command=lambda: self.doThrow())
        self.throwButton.grid(row=1, column=6)
        self.fightButton = tk.Button(self.Functionframe, text='fight', width=w_Size, height=h_Size,
                                     command=lambda: self.doFight())
        self.fightButton.grid(row=0, column=6)
        MonsterNum = len(self.game.room[self.game.HeroX][self.game.HeroY].Monster)
        if not MonsterNum:
            self.fightButton.configure(state=DISABLED)

    def doThrow(self):
        Room = self.game.room[self.game.HeroX][self.game.HeroY]
        self.top.destroy()
        self.top = tk.Toplevel()
        self.top.title(Room.description)
        t1 = tk.Frame(self.top, width=400, height=200)
        t1.grid(row=0, column=0)
        t1.rowconfigure(0, pad=40)
        t1.rowconfigure(1, pad=40)
        t1.rowconfigure(2, pad=40)
        t1.rowconfigure(3, pad=40)

        LabelSize = 30
        redJeweltext = "X " + str(Room.Dict['redJewel']['num'])
        self.ThrowredJewelLabel = tk.Label(t1, text=redJeweltext, compound='left',
                                           image=self.GetImg(name='redJewel', resize=LabelSize))
        self.ThrowredJewelLabel.grid(row=0, column=0, sticky='w')
        self.ThrowredJewelLButton = tk.Button(t1, text='Throw',
                                              command=lambda: self.Throw('redJewel', Room))
        self.ThrowredJewelLButton.grid(row=1, column=0, padx=15)
        if not self.game.Hero.Dict['redJewel']['num']:
            self.ThrowredJewelLButton.configure(state=DISABLED)

        blueJeweltext = "X " + str(Room.Dict['blueJewel']['num'])
        self.ThrowblueJewelLabel = tk.Label(t1, text=blueJeweltext, compound='left',
                                            image=self.GetImg(name='blueJewel', resize=LabelSize))
        self.ThrowblueJewelLabel.grid(row=0, column=1, sticky='w')
        self.ThrowblueJewelButton = tk.Button(t1, text='Throw',
                                              command=lambda: self.Throw('blueJewel', Room))
        self.ThrowblueJewelButton.grid(row=1, column=1, padx=15)
        if not self.game.Hero.Dict['blueJewel']['num']:
            self.ThrowblueJewelButton.configure(state=DISABLED)

        redPotiontext = "X " + str(Room.Dict['redPotion']['num'])
        self.ThrowredPotionLabel = tk.Label(t1, text=redPotiontext, compound='left',
                                            image=self.GetImg(name='redPotion', resize=LabelSize))
        self.ThrowredPotionLabel.grid(row=0, column=2, sticky='w')
        self.ThrowredPotionButton = tk.Button(t1, text='Throw',
                                              command=lambda: self.Throw('redPotion', Room))
        self.ThrowredPotionButton.grid(row=1, column=2, padx=15)
        if not self.game.Hero.Dict['redPotion']['num']:
            self.ThrowredPotionButton.configure(state=DISABLED)

        expPotiontext = "X " + str(Room.Dict['expPotion']['num'])
        self.ThrowexpPotionLabel = tk.Label(t1, text=expPotiontext, compound='left',
                                            image=self.GetImg(name='expPotion', resize=LabelSize))
        self.ThrowexpPotionLabel.grid(row=0, column=3, sticky='w')
        self.ThrowexpPotionButton = tk.Button(t1, text='Throw',
                                              command=lambda: self.Throw('expPotion', Room))
        self.ThrowexpPotionButton.grid(row=1, column=3, padx=15)
        if not self.game.Hero.Dict['expPotion']['num']:
            self.ThrowexpPotionButton.configure(state=DISABLED)

        Weighttext = "Weight : " + str(self.game.Hero.GetTotalWeight())
        self.WeightLabel = tk.Label(t1, text=Weighttext, compound='left', ). \
            grid(row=0, column=4)

        MaxWeighttext = "MaxWeight : " + str(MaxWeight)
        self.WeightLabel = tk.Label(t1, text=MaxWeighttext, compound='left', ). \
            grid(row=1, column=4)

    def doFight(self):
        Room = self.game.room[self.game.HeroX][self.game.HeroY]
        if not len(Room.Monster):
            showinfo(message="There is safe.")
            self.top.destroy()
            return
        self.top.destroy()
        self.top = tk.Toplevel()
        self.top.title(Room.description)
        t1 = tk.Frame(self.top, width=800, height=200)
        t1.grid(row=0, column=0)
        for i in range(7):
            t1.columnconfigure(i, pad=40)
        text = "Name"
        self.FightNameLabel = tk.Label(t1, text=text).grid(row=0, column=1)
        text = "Level"
        self.FightLevelLabel = tk.Label(t1, text=text).grid(row=0, column=2)
        text = "Attack"
        self.FightAttackLabel = tk.Label(t1, text=text).grid(row=0, column=3)
        text = "Defend"
        self.FightDefendLabel = tk.Label(t1, text=text).grid(row=0, column=4)
        text = "HP"
        self.FightHPLabel = tk.Label(t1, text=text).grid(row=0, column=5)

        row = 1
        for M in Room.Monster:
            img = randint(4, 30)
            name = str(img).rjust(2, '0') + '.png'
            self.FightImg = tk.Label(t1, image=self.GetImg(name=name, resize=40, Temp=False)). \
                grid(row=row, column=0)
            text = M.Name
            self.FightNameLabel = tk.Label(t1, text=text).grid(row=row, column=1)
            text = str(M.Level)
            self.FightLevelLabel = tk.Label(t1, text=text).grid(row=row, column=2)
            text = str(M.Attack)
            self.FightAttackLabel = tk.Label(t1, text=text).grid(row=row, column=3)
            text = str(M.Defend)
            self.FightDefendLabel = tk.Label(t1, text=text).grid(row=row, column=4)
            text = str(M.HealthPoint)
            self.FightHPLabel = tk.Label(t1, text=text).grid(row=row, column=5)
            text = 'Fight'
            self.FightButton = tk.Button(t1, text=text, command=lambda: self.Fight(Room, M)). \
                grid(row=row, column=6)
            row += 1

    def Fight(self, Room, Monster):
        State = Fight(self.game.Hero, Monster, TextUI)
        if State == -1:
            self.doLose(Monster.Name)
        else:
            self.game.Hero.HealthPoint -= State
            Gold_get = Monster.Gold * random.randint(1, Monster.Level)
            self.game.Hero.Gold += Gold_get
            Exp_Get = Monster.Level * MonsterExp
            self.game.Hero.Experience += Exp_Get
            LevelUp(self.game.Hero)
            if Monster.Name == 'devil':
                self.doEnd()
                self.logger.info("Win Game")
            else:
                title = "Win"
                message = ("You Lose %s HP in Battle with %s." % (State, Monster.Name))
                message += ("\nYou Get %s Gold." % Gold_get)
                message += ("\nYou Get %s Experience." % Exp_Get)
                showinfo(title=title, message=message)
                self.logger.info(message)
            for i in range(len(Room.Monster)):
                if Room.Monster[i] == Monster:
                    del Room.Monster[i]
                    break

        self.RefreshHeroframe()
        self.RefreshBagframe()
        self.doFight()

    def doLose(self, Name):
        title = "Lose"
        message = "You Dead in Battle with %s!" % Name
        message = message + '\nGame Over!'
        showinfo(title=title, message=message)
        self.logger.info(f'Game Over!')
        self.frame.destroy()

    def doEnd(self):
        try:
            title = "Win"
            message = """        You beat the devil!!!
            You save the princess!!!
            Thank you for your contribution!!!"""
            showinfo(title=title, message=message)
        except:
            self.logger.error(f"doEnd  error!")

    def Throw(self, name, Room):
        try:
            self.game.Hero.ThrowThing(name, 1, Room)
            self.RefreshBagframe()
            self.doThrow()
            self.logger.info(f'Throw {name} to {Room.description}')
        except:
            self.logger.critical(f'Throw {name} to {Room.description} critical')

    def doPick(self):
        Room = self.game.room[self.game.HeroX][self.game.HeroY]
        self.top.destroy()
        self.top = tk.Toplevel()
        self.top.title(Room.description)
        t1 = tk.Frame(self.top, width=400, height=200)
        t1.grid(row=0, column=0)
        t1.rowconfigure(0, pad=40)
        t1.rowconfigure(1, pad=40)
        t1.rowconfigure(2, pad=40)
        t1.rowconfigure(3, pad=40)

        Goldnum = Room.Gold
        if Goldnum:
            title = 'event'
            message = 'You got ' + str(Goldnum) + ' gold.'
            self.game.Hero.Pick('Gold', Goldnum, Room)
            self.RefreshBagframe()
            # showinfo(title=title, message=message)

        LabelSize = 30
        redJeweltext = "X " + str(Room.Dict['redJewel']['num'])
        self.PickredJewelLabel = tk.Label(t1, text=redJeweltext, compound='left',
                                          image=self.GetImg(name='redJewel', resize=LabelSize))
        self.PickredJewelLabel.grid(row=0, column=0, sticky='w')
        self.PickredJewelLButton = tk.Button(t1, text='pick', command=lambda: self.PickredJewel(Room))
        self.PickredJewelLButton.grid(row=1, column=0, padx=15)
        if not Room.Dict['redJewel']['num']:
            self.PickredJewelLButton.configure(state=DISABLED)

        blueJeweltext = "X " + str(Room.Dict['blueJewel']['num'])
        self.PickblueJewelLabel = tk.Label(t1, text=blueJeweltext, compound='left',
                                           image=self.GetImg(name='blueJewel', resize=LabelSize))
        self.PickblueJewelLabel.grid(row=0, column=1, sticky='w')
        self.PickblueJewelButton = tk.Button(t1, text='pick', command=lambda: self.PickblueJewel(Room))
        self.PickblueJewelButton.grid(row=1, column=1, padx=15)
        if not Room.Dict['blueJewel']['num']:
            self.PickblueJewelButton.configure(state=DISABLED)

        redPotiontext = "X " + str(Room.Dict['redPotion']['num'])
        self.PickredPotionLabel = tk.Label(t1, text=redPotiontext, compound='left',
                                           image=self.GetImg(name='redPotion', resize=LabelSize))
        self.PickredPotionLabel.grid(row=0, column=2, sticky='w')
        self.PickredPotionButton = tk.Button(t1, text='pick', command=lambda: self.PickredPotion(Room))
        self.PickredPotionButton.grid(row=1, column=2, padx=15)
        if not Room.Dict['redPotion']['num']:
            self.PickredPotionButton.configure(state=DISABLED)

        expPotiontext = "X " + str(Room.Dict['expPotion']['num'])
        self.PickexpPotionLabel = tk.Label(t1, text=expPotiontext, compound='left',
                                           image=self.GetImg(name='expPotion', resize=LabelSize))
        self.PickexpPotionLabel.grid(row=0, column=3, sticky='w')
        self.PickexpPotionButton = tk.Button(t1, text='pick', command=lambda: self.PickexpPotion(Room))
        self.PickexpPotionButton.grid(row=1, column=3, padx=15)
        if not Room.Dict['expPotion']['num']:
            self.PickexpPotionButton.configure(state=DISABLED)

        Weighttext = "Weight : " + str(self.game.Hero.GetTotalWeight())
        self.WeightLabel = tk.Label(t1, text=Weighttext, compound='left', ). \
            grid(row=0, column=4)

        MaxWeighttext = "MaxWeight : " + str(MaxWeight)
        self.WeightLabel = tk.Label(t1, text=MaxWeighttext, compound='left', ). \
            grid(row=1, column=4)

    def PickredJewel(self, Room):
        nRoom = self.game.room[self.game.HeroX][self.game.HeroY]
        if nRoom.description == Room.description:
            Pick = self.game.Hero.Pick('redJewel', 1, Room)
            self.logger.info(f"Pick redJewel {Room.description}")
            self.RefreshBagframe()
            self.doPick()
            if not Pick:
                GuiWarning()
        else:
            GuiWarning()

    def PickblueJewel(self, Room):
        nRoom = self.game.room[self.game.HeroX][self.game.HeroY]
        if nRoom.description == Room.description:
            Pick = self.game.Hero.Pick('blueJewel', 1, Room)
            self.logger.info(f"Pick blueJewel {Room.description}")
            self.RefreshBagframe()
            self.doPick()
            if not Pick:
                GuiWarning()
        else:
            GuiWarning()

    def PickredPotion(self, Room):
        nRoom = self.game.room[self.game.HeroX][self.game.HeroY]
        if nRoom.description == Room.description:
            Pick = self.game.Hero.Pick('redPotion', 1, Room)
            self.logger.info(f"Pick redPotion {Room.description}")
            self.RefreshBagframe()
            self.doPick()
            if not Pick:
                GuiWarning()
        else:
            GuiWarning()

    def PickexpPotion(self, Room):
        nRoom = self.game.room[self.game.HeroX][self.game.HeroY]
        if nRoom.description == Room.description:
            Pick = self.game.Hero.Pick('expPotion', 1, Room)
            if not Pick:
                GuiWarning()
            self.logger.info(f"Pick expPotion {Room.description}")
            self.RefreshBagframe()
            self.doPick()
        else:
            GuiWarning()

    def doGoCommand(self, secondWord):
        nextRoom = self.game.currentRoom.getExit(secondWord)
        if nextRoom:
            for i in range(4):
                if secondWord == dir[i]:
                    self.game.HeroX += dirsx[i]
                    self.game.HeroY += dirsy[i]
                    # print("HeroX: %s, HeroY: %s." % (self.HeroX, self.HeroY))
            self.game.currentRoom = nextRoom
            self.RefreshMapframe()

    def RefreshMapframe(self):
        for w in range(self.Map.width):
            for h in range(self.Map.height):
                if CheckPoint(w, h, self.game.HeroX, self.game.HeroY):
                    # print(h, '\n', w)
                    # print(self.game.HeroX, '\n', self.game.HeroY)
                    self.MapLabel[w][h] = tk.Label(self.Mapframe, image=self.GetImg(name='Hero01', resize=MapSize))

                elif self.Map.map[w][h] == 1:
                    self.MapLabel[w][h] = tk.Label(self.Mapframe, image=self.GetImg(name='wall', resize=MapSize))
                else:
                    if CheckEven(h + w):
                        name = 'room0' + str((h * 2 + w) % 3 + 1)
                        self.MapLabel[w][h] = tk.Label(self.Mapframe, image=self.GetImg(name=name, resize=MapSize))
                    else:
                        self.MapLabel[w][h] = tk.Label(self.Mapframe, image=self.GetImg(name='road', resize=MapSize))

                self.MapLabel[w][h].grid(row=w, column=h, padx=0, pady=0)

    def GetImg(self, name, resize=0, Temp=True):
        try:
            if Temp:
                Path = f'{path.dirname(__file__)}/images/{ImageDict[name]}'
            else:
                Path = f'{path.dirname(__file__)}/images/{name}'
            if Path in self.imgDict and self.imgDict[Path]:
                return self.imgDict[Path]
            Img = Image.open(Path)
            if resize:
                Img = Img.resize((resize, resize), Image.ANTIALIAS)
            Img = ImageTk.PhotoImage(Img)
            self.imgDict[Path] = Img
            return Img
        except:
            self.logger.critical(f"GetImg {name} critical!")

    def doBuy(self):
        self.top.destroy()
        if self.game.room[self.game.HeroX][self.game.HeroY].isShop:
            Room = self.game.room[self.game.HeroX][self.game.HeroY]
            self.top.destroy()
            self.top = tk.Toplevel()
            self.top.title(Room.description)
            t1 = tk.Frame(self.top, width=400, height=200)
            t1.grid(row=0, column=0)

            for i in range(4):
                t1.rowconfigure(i, pad=20)
            for i in range(5):
                t1.columnconfigure(i, pad=30)

            LabelSize = 30
            self.BuyredJewelLabel = tk.Label(t1, image=self.GetImg(name='redJewel', resize=LabelSize))
            self.BuyredJewelLabel.grid(row=0, column=0)
            Pircetext = str(Shop_Dict['redJewel']['price']) + 'g'
            self.PirceredJewelLabel = tk.Label(t1, text=Pircetext)
            self.PirceredJewelLabel.grid(row=1, column=0)
            self.BuyredJewelLButton = tk.Button(t1, text='Buy', command=lambda: self.Buy('redJewel'))
            self.BuyredJewelLButton.grid(row=2, column=0)
            self.SellredJewelLButton = tk.Button(t1, text='Sell', command=lambda: self.Sell('redJewel'))
            self.SellredJewelLButton.grid(row=3, column=0)
            if self.game.Hero.Gold < Shop_Dict['redJewel']['price'] or \
                    self.game.Hero.GetTotalWeight() + Shop_Dict['redJewel']['weight'] > self.game.Hero.MaxWeight:
                self.BuyredJewelLButton.configure(state=DISABLED)
            if not self.game.Hero.Dict['redJewel']['num']:
                self.SellredJewelLButton.configure(state=DISABLED)

            self.BuyblueJewelLabel = tk.Label(t1, image=self.GetImg(name='blueJewel', resize=LabelSize))
            self.BuyblueJewelLabel.grid(row=0, column=1)
            Pircetext = str(Shop_Dict['blueJewel']['price']) + 'g'
            self.PirceblueJewelLabel = tk.Label(t1, text=Pircetext)
            self.PirceblueJewelLabel.grid(row=1, column=1)
            self.BuyblueJewelButton = tk.Button(t1, text='Buy', command=lambda: self.Buy('blueJewel'))
            self.BuyblueJewelButton.grid(row=2, column=1)
            self.SellblueJewelButton = tk.Button(t1, text='Sell', command=lambda: self.Sell('blueJewel'))
            self.SellblueJewelButton.grid(row=3, column=1)
            if self.game.Hero.Gold < Shop_Dict['blueJewel']['price'] or \
                    self.game.Hero.GetTotalWeight() + Shop_Dict['blueJewel']['weight'] > self.game.Hero.MaxWeight:
                self.BuyblueJewelButton.configure(state=DISABLED)
            if not self.game.Hero.Dict['blueJewel']['num']:
                self.SellblueJewelButton.configure(state=DISABLED)

            self.BuyredPotionLabel = tk.Label(t1, image=self.GetImg(name='redPotion', resize=LabelSize))
            self.BuyredPotionLabel.grid(row=0, column=2)
            Pircetext = str(Shop_Dict['redPotion']['price']) + 'g'
            self.PirceredPotionLabel = tk.Label(t1, text=Pircetext)
            self.PirceredPotionLabel.grid(row=1, column=2)
            self.BuyredPotionButton = tk.Button(t1, text='Buy', command=lambda: self.Buy('redPotion'))
            self.BuyredPotionButton.grid(row=2, column=2)
            self.SellredPotionButton = tk.Button(t1, text='Sell', command=lambda: self.Sell('redPotion'))
            self.SellredPotionButton.grid(row=3, column=2)
            if self.game.Hero.Gold < Shop_Dict['redPotion']['price'] or \
                    self.game.Hero.GetTotalWeight() + Shop_Dict['redPotion']['weight'] > self.game.Hero.MaxWeight:
                self.BuyredPotionButton.configure(state=DISABLED)
            if not self.game.Hero.Dict['redPotion']['num']:
                self.SellredPotionButton.configure(state=DISABLED)

            self.BuyexpPotionLabel = tk.Label(t1, image=self.GetImg(name='expPotion', resize=LabelSize))
            self.BuyexpPotionLabel.grid(row=0, column=3)
            Pircetext = str(Shop_Dict['expPotion']['price']) + 'g'
            self.PirceexpPotionLabel = tk.Label(t1, text=Pircetext)
            self.PirceexpPotionLabel.grid(row=1, column=3)
            self.BuyexpPotionButton = tk.Button(t1, text='Buy', command=lambda: self.Buy('expPotion'))
            self.BuyexpPotionButton.grid(row=2, column=3)
            self.SellexpPotionButton = tk.Button(t1, text='Sell', command=lambda: self.Sell('expPotion'))
            self.SellexpPotionButton.grid(row=3, column=3)

            if self.game.Hero.Gold < Shop_Dict['expPotion']['price'] or \
                    self.game.Hero.GetTotalWeight() + Shop_Dict['expPotion']['weight'] > self.game.Hero.MaxWeight:
                self.BuyexpPotionButton.configure(state=DISABLED)
            if not self.game.Hero.Dict['expPotion']['num']:
                self.SellexpPotionButton.configure(state=DISABLED)

            Goldtext = "Gold : " + str(self.game.Hero.Gold)
            self.GoldLabel = tk.Label(t1, text=Goldtext, compound='left', ). \
                grid(row=0, column=4)
            Weighttext = "Weight : " + str(self.game.Hero.GetTotalWeight())
            self.WeightLabel = tk.Label(t1, text=Weighttext, compound='left', ). \
                grid(row=1, column=4)

            MaxWeighttext = "MaxWeight : " + str(MaxWeight)
            self.WeightLabel = tk.Label(t1, text=MaxWeighttext, compound='left', ). \
                grid(row=2, column=4)

    def Sell(self, name):
        try:
            self.game.Hero.Gold += Shop_Dict[name]['price']
            self.game.Hero.Dict[name]['num'] -= 1
            self.game.Hero.Weight = self.game.Hero.GetTotalWeight()
            self.RefreshBagframe()
            self.doBuy()
            self.logger.info(f"Sell {name}")
        except:
            self.logger.critical(f"Sell {name} critical!")

    def Buy(self, name):
        try:
            self.game.Hero.Gold -= Shop_Dict[name]['price']
            self.game.Hero.AddThing(name, 1)
            self.game.Hero.Weight = self.game.Hero.GetTotalWeight()
            self.RefreshBagframe()
            self.doBuy()
            self.logger.info(f"Buy {name}")
        except:
            self.logger.critical(f"Buy {name} critical!")


def main():
    win = tk.Tk()  # Create a window
    win.title("DJ Gui Game")  # Set window title
    w = str(int(Width * MapSize * 3 / 2) - 50)
    h = str((Height + 1) * MapSize + 180)
    size = w + "x" + h
    win.geometry(size)  # Set window size
    win.resizable(False, False)  # Both x and y dimensions ...

    # Create the GUI as a Frame
    # and attach it to the window ...
    myApp = GUI(win)

    # Call the GUI mainloop ...
    win.mainloop()


def test():
    win = tk.Tk()  # Create a window
    win.title("DJ Gui Game")  # Set window title
    w = str(int(Width * MapSize * 3 / 2) - 50)
    h = str((Height + 1) * MapSize + 180)
    size = w + "x" + h
    win.geometry(size)  # Set window size
    win.resizable(False, False)  # Both x and y dimensions ...

    # Create the GUI as a Frame
    # and attach it to the window ...
    myApp = GUI(win)
    myApp.GoEast()
    myApp.GoWest()
    myApp.UseexpPotion()
    myApp.UseexpPotion()
    myApp.UseexpPotion()
    myApp.Throw('blueJewel', myApp.game.currentRoom)

    # Call the GUI mainloop ...
    win.mainloop()


if __name__ == "__main__":
    # test()
    main()
