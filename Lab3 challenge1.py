import random


# Create a random number generator function that takes two parameters
# e.g. genRandom(minVal, maxVal) , and then returns an output value
# between those two values inclusive

def genRandom(minVal, maxVal):
    return random.randint(minVal, maxVal)


# Create a function to generate a lottery ticket. A lottery ticket can be
# conveniently represented using a list of 6 integer numbers with values
# between 1 and 50 inclusive. The function should return the list. Numeric
# values in a list can be sorted into ascending order using
# list.sort(reverse=??) where list is the list you want sorted a
# keyword argument reverse is used (value True or False) to specify
# whether you want ascending or descending order. There should be no
# duplicate values in your list.

def generate_a_lottery_ticket():
    lottery_ticket = []
    while len(lottery_ticket) < 6:
        num = random.randint(1, 10)
        if num not in lottery_ticket:
            lottery_ticket.append(num)
    lottery_ticket.sort()
    return lottery_ticket


# print(generate_a_lottery_ticket())


# Create a function to check whether we have won the lottery. This function
# should take the lottery ticket list previously created as one parameter, and
# a list of the 6 winning numbers as the other argument. If 2 numbers match
# return a win of £1. If 3 numbers match, the function should return a win of
# £10, if 4 numbers match, return a win of £50, 5 number a win of £500 and
# 6 numbers £1,000,000.

def check_won(lottery=[]):
    list1 = generate_a_lottery_ticket()
    lottery = generate_a_lottery_ticket()
    # ans = [i for i in list1 if i in lottery]
    # num = len(ans)
    num = len(set(list1) & set(lottery))
    print(num)
    if num == 2:
        return 1
    elif num == 3:
        return 10
    elif num == 4:
        return 50
    elif num == 5:
        return 500
    elif num == 6:
        return 1000000
    else:
        return 0


print(check_won())
