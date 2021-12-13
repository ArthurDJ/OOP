from tkinter.messagebox import showinfo


def AddDict(thedict, key_a, key_b, val):
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a: {key_b: val}})


def CheckEven(num):
    if num % 2:
        return False
    return True


def CheckUpper(str1, str2):
    return str1.upper() == str2.upper()


def CheckTypeStr(str):
    return type(str) is str


def ShowShop(dict):
    print("%9s%8s" % ("name", 'price'))
    for name in dict:
        print("%9s%8s" % (name, dict[name]['price']))


def CheckPoint(x1, y1, x2, y2):
    if x1 == x2 * 2 + 1 and y1 == y2 * 2 + 1:
        return True
    return False


def GuiWarning():
    title = 'warning'
    message = "You can't do this!"
    showinfo(title=title, message=message)

