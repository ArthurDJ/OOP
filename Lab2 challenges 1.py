# Allow the user to enter a number. Use an if statement to display whether
# the number is negative, equal to zero or positive.
def num():
    n = int(input('Plz enter a number: '))
    if n < 0:
        print('Negative number')
    elif n == 0:
        print('Equal to zero')
    else:
        print('Positive number')
    return


# The range() function can be used to create a sequence of numbers (see
# the code examples for this). Allow the user to enter a number and then
# iterate over the range to determine whether the number the user entered
# is present in the sequence.
import random


def range_num():
    n = int(input('Plz enter a number: '))
    start = n - 100
    end = n + 100
    step = random.randint(1, 10)
    rand = range(start, end, step)
    # print(step, end="\n")
    for i in rand:
        # print(i, end="\n")
        if i == n:
            print("Congratulations!" + str(n) + " is in range!")
            return
    print("What a pity~~~")
    return


# range_num()


# An arithmetic series of numbers is defined by an initial value
# and a common difference. For example, if the starting value is 2 and
# the common difference is 5, the arithmetic sequence would begin 2, 5, 8, 11, 14 …
# Allow the user to enter values for the initial value and common difference.
# Write code to determine the sum of the first 10 elements in the
# arithmetic sequence.
def Sum_of_Elements():
    starting_num = int(input("Plz enter starting value: "))
    common_difference = int(input("Plz enter common difference: "))
    number_of_terms = 10
    ans = ((starting_num * 2 + common_difference * (number_of_terms - 1)) * number_of_terms) / 2
    print(ans)
    return
    # return ans


# Sum_of_Elements()

# Write code to simulate the simple children’s game “Fuzz Buzz”. The rules
# are simple; start counting upwards from 1 in single increments. If the
# number is divisible by 5, display “Fuzz”. if the number is divisible by 6,
# display “Buzz”. If the number is divisible by both, display “Fuzz Buzz”.
# Otherwise just display the number. Play the game from 1 through to 50
# inclusive

def Fuzz_Buzz():
    for i in range(1, 50):
        if i % 30 == 0:
            print("Fuzz Buzz", end='\n')
        elif i % 5 == 0:
            print("Fuzz", end='\n')
        elif i % 6 == 0:
            print("Buzz", end='\n')
        else:
            print(i, end='\n')
    return

Fuzz_Buzz()
