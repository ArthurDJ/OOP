import math

def print_num(n):
    a = 0;
    while a <= n:
        print(a, end=" ")
        a += 2


def print_str():
    str = input("plz enter a string:\n")
    for char in str:
        print(char, end="\n")


def print_str_rev():
    str = input("plz enter a string:\n")
    # print(str[::-1])
    List_str = list(str)
    List_str.reverse()

    for char in List_str:
        print(char, end="\n")


def fib(n):
    if n >= 0:
        f = (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5)
        return int(f)
    else:
        pass


# print_num(20)
# print_str_rev()
print(fib(5))