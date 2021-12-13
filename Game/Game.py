from Room import *
from Map import *
from role import *

"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game.  Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, create an instance of this class and call the "play"
    method.

    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game.  It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage
"""


class Game:

    def __init__(self):
        """
        Initialises the game
        """
        self.textUI = TextUI()
        self.Hero = Hero()
        self.Map = Map(Width, Height)
        self.room = [[Room(description="Here is H = %s, W = %s" % (x, y))
                      for x in range(HEIGHT)] for y in range(WIDTH)]
        self.HeroX, self.HeroY = self.Map.startX, self.Map.startY
        self.DevilX, self.DevilY = self.Map.startX, self.Map.startY
        self.DevilX, self.DevilY = self.Map.devilX, self.Map.devilY
        # self.currentRoom = self.room[self.HeroX][self.HeroY]
        self.createRooms()

    def setName(self):
        """
        get Hero Name and set
        :return: None
        """
        self.textUI.printtoTextUI("At first, Hero, Tell me Your Name?")
        Name, sword = self.textUI.getCommand()
        self.Hero.Name = Name

    def createRooms(self):
        """
            Sets up all room assets
        :return: None
        """
        self.room[self.DevilX][self.DevilY].Monster.append(Monster(Gold=1000, Level=30))
        for x in range(WIDTH):
            for y in range(HEIGHT):
                rate = randint(1, Shop_Rate)
                if rate == 1:
                    self.room[x][y].isShop = True
                map_x = x * 2 + 1
                map_y = y * 2 + 1
                for i in range(4):
                    next_map_x = map_x + dirsx[i]
                    next_map_y = map_y + dirsy[i]
                    if self.checkRooms(next_map_x, next_map_y):
                        self.room[x][y].setExit(dir[i], self.room[x + dirsx[i]][y + dirsy[i]])
                        # print("nowx = %s, nowy =  %s.\nnextx = %s, nexty = %s." %
                        #       (x, y, x + dirsx[i], y + dirsy[i]))
        self.currentRoom = self.room[self.HeroX][self.HeroY]

    def checkRooms(self, x, y):
        """
        Judge the validity of room coordinates
        :param x: the line of Room in Map
        :param y: the line of Room in Map
        :return:the validity of room coordinates
        """
        if Width >= x >= 0 == self.Map.map[x][y] and 0 <= y <= Height:
            return True
        return False

    def play(self):
        """
            The main play loop
        :return: None
        """
        self.printWelcome()
        self.setName()
        self.showCommandWords()
        finished = False
        while not finished:
            command = self.textUI.getCommand()  # Returns a 2-tuple
            finished = self.processCommand(command)

        print("Thank you for playing!")

    def printWelcome(self):
        """
            Displays a welcome message
        :return:
        """
        self.textUI.printtoTextUI("You come to the devil's castle alone.")
        self.textUI.printtoTextUI("The princess was locked in the attic somewhere.")
        self.textUI.printtoTextUI("Take the sword in your hand, defeat the monster.")
        self.textUI.printtoTextUI("Defeat the devil and save the princess.")
        self.textUI.printtoTextUI("")

    def showCommandWords(self):
        """
            Show a list of available commands
        :return: None
        """
        self.textUI.printtoTextUI(f'Your command words are: {CommandWords}')

    def processCommand(self, command):
        """
            Process a command from the TextUI
        :param command: a 2-tuple of the form (commandWord, secondWord)
        :return: True if the game has been quit, False otherwise
        """
        commandWord, secondWord = command
        if commandWord is not None:
            commandWord = commandWord.upper()

        wantToQuit = False
        if commandWord == "HELP":
            self.doPrintHelp()
        elif commandWord == "GO":
            self.doGoCommand(secondWord)
        elif commandWord == "USE":
            self.doUseCommand()
        elif commandWord == "QUIT":
            wantToQuit = True
        elif commandWord == "LIST":
            self.doListCommand()
        elif commandWord == "PICK":
            self.doPickCommand(self.room[self.HeroX][self.HeroY])
        elif commandWord == "THROW":
            self.doThrowCommand(self.room[self.HeroX][self.HeroY])
        elif commandWord == "HERO":
            self.doHeroCommand()
        elif commandWord == "FIGHT":
            self.doFightCommand(self.room[self.HeroX][self.HeroY])
        elif commandWord == "BUY":
            self.doBuyCommand(self.room[self.HeroX][self.HeroY])
        else:
            # Unknown command ...
            self.textUI.printtoTextUI("Don't know what you mean")

        return wantToQuit

    def doBuyCommand(self, Room):
        if Room.isShop:
            ShowShop(Shop_Dict)
            self.textUI.printtoTextUI("Please input the item and quantity you want to buy.")
            Name, Number = self.textUI.getCommand()
            if Name in Shop_Dict:
                if Number is None:
                    self.textUI.printtoTextUI("Please input quantity you want to buy.")
                    Number, sword = self.textUI.getCommand()
                Number = int(Number)
                Sum_Price = Shop_Dict[Name]['price'] * Number
                print(Sum_Price)
                w = Number * Shop_Dict[Name]['weight']
                if Number >= 0:
                    if self.Hero.Gold >= Sum_Price and self.Hero.Weight + w <= self.Hero.MaxWeight:
                        # self.textUI.printGetThing(Name, Number)
                        self.Hero.Gold -= Sum_Price
                        self.Hero.AddThing(Name, Number, self.textUI)
                    elif self.Hero.Gold < Sum_Price:
                        self.textUI.printNotenough("Gold")
                    elif self.Hero.Weight + w > self.Hero.MaxWeight:
                        self.textUI.printOutWeight()
                else:
                    self.textUI.printDream()
            else:
                self.textUI.printtoTextUI("There is no this item.")
        else:
            self.textUI.printtoTextUI("There is no shop here, you can't buy things.")

    def doFightCommand(self, Room):
        MonsterNum = len(Room.Monster)
        if MonsterNum == 0:
            self.textUI.printtoTextUI("There is safe.")
        else:
            Room.showMonster()
            self.textUI.printtoTextUI("Which monster do you want to fight (enter number)?")
            Number, sword = self.textUI.getCommand()
            Number = int(Number)
            if 0 < Number <= len(Room.Monster):
                BattleSettlement(self.Hero, Room.Monster[Number - 1], self.textUI)
                if Room.Monster[Number - 1].Name == 'devil':
                    self.doWin()
                del Room.Monster[Number - 1]
            else:
                self.textUI.printtoTextUI("No this Monster.")

    def doPrintHelp(self):
        """
            Display some useful help text
        :return: None
        """
        self.showCommandWords()
 
    def doPickCommand(self, Room):
        """
            Pick things in room
        :param Room: which room you pick things
        :return: None
        """
        Room.Show(self.textUI)
        self.textUI.printtoTextUI("Please input what and how much you want pick.")
        Name, Number = self.textUI.getCommand()
        if Name in Room.Dict or Name.upper() == "GOLD":
            if Number is None:
                self.textUI.printtoTextUI("Please input how much you want pick.")
                Number, sword = self.textUI.getCommand()
            self.Hero.Pick(Name, Number, Room, self.textUI)
        else:
            self.textUI.printNoThing()

    def doThrowCommand(self, Room):
        """
        Throw things in to room
        :param Room: Which room you throw things
        :return: None
        """
        self.Hero.Show(self.textUI)
        self.textUI.printtoTextUI("Please input what and how much you want throw.")

        Name, Number = self.textUI.getCommand()
        if Name in self.Hero.Dict or CheckUpper(Name, 'gold'):
            if Number is None:
                self.textUI.printtoTextUI("Please input how much you want throw.")
                Number, word = self.textUI.getCommand()

            self.Hero.ThrowThing(Name, Number, Room, self.textUI)
        else:
            self.textUI.printNoThing()

    def doGoCommand(self, secondWord):
        """
            Performs the GO command
        :param secondWord: the direction the player wishes to travel in
        :return: None
        """
        if secondWord is None:
            # Missing second word ...
            self.textUI.printtoTextUI("Go where?")
            return

        nextRoom = self.currentRoom.getExit(secondWord)
        if nextRoom is None:
            self.textUI.printtoTextUI("There is no door!")
        else:
            for i in range(4):
                if secondWord == dir[i]:
                    self.HeroX += dirsx[i]
                    self.HeroY += dirsy[i]
                    # print("HeroX: %s, HeroY: %s." % (self.HeroX, self.HeroY))
            self.currentRoom = nextRoom
            self.textUI.printtoTextUI(self.currentRoom.getLongDescription())
            if self.currentRoom.isShop:
                self.textUI.printtoTextUI("You can buy things in the store")

    def doListCommand(self):
        self.Hero.Show(self.textUI)

    def doHeroCommand(self):
        self.Hero.ShowAttribute(self.textUI)
        self.Hero.ShowLevel(self.textUI)

    def doUseCommand(self):
        self.Hero.Show(self.textUI)
        self.textUI.printtoTextUI("Please input what and how much you want use.")
        Name, Number = self.textUI.getCommand()
        if Name in self.Hero.Dict:
            if Number is None:
                self.textUI.printtoTextUI("Please input how much you want use.")
                Number, word = self.textUI.getCommand()
            self.Hero.UseThing(Name, Number, self.textUI)
            LevelUp(self.Hero)
        else:
            self.textUI.printNoThing()

    def doWin(self):
        self.textUI.printtoTextUI("")
        self.textUI.printtoTextUI("You beat the devil!!!")
        self.textUI.printtoTextUI("You save the princess!!!")
        self.textUI.printtoTextUI("Thank you for your contribution!!!")
        exit()


def main():
    # try:
    game = Game()
    game.play()


# except Exception as e:
#     print(e.args)


# class TestGame(unittest.TestCase):
#     def setUp(self):
#         self.test = Game()
#
#     def test1(self):
#         self.test.processCommand(("LIST", None))


if __name__ == "__main__":
    main()
