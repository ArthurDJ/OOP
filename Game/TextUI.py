"""
    A simple text based User Interface (UI) for the
    Adventure World game
"""


class TextUI:

    def __init__(self):
        # Nothing to do ...

        pass

    def getCommand(self):
        """
            Fetches a command from the console
        :return: a 2-tuple of the form (commandWord, secondWord)
        """
        word1 = None
        word2 = None
        print('> ', end='')
        inputLine = input()
        if inputLine != "":
            allWords = inputLine.split()
            word1 = allWords[0]
            if len(allWords) > 1:
                word2 = allWords[1]
            else:
                word2 = None
            # Just ignore any other words
        return word1, word2

    def printtoTextUI(self, text):
        """
            Displays text to the console
        :rtype: object
        :param text: Text to be displayed
        :return: None
        """
        print(text)

    def printGetThing(self, Name, Number):
        print("You get %s %s." % (Number, Name))

    def printNoThing(self):
        print("There is no such thing.")

    def printOutWeight(self):
        print("You don't have enough space in your backpack.")

    def printThrowThing(self, Name, Number):
        print("You throw %s %s." % (Number, Name))

    def printNotenough(self, Name):
        print("Don't have so much %s." % Name)

    def printDream(self):
        print("DO NOT DREAM~~~~")

    def pringUseThing(self, Name, Number):
        print("You use %s %s." % (Number, Name))
