import random
import string


def even_list():
    listnum = []
    for i in range(1, 10):
        listnum.append(random.randint(1, 100))
    even_list1 = [i for i in listnum if i % 2 == 0]
    return even_list1


def random_str(num=10):
    liststr = []
    for i in range(1, num):
        str_len = random.randint(1, 7)
        liststr.append(''.join(random.sample(string.ascii_letters, str_len)))
    return liststr


def len_str():
    n = 3
    ans_list = [i for i in random_str() if len(i) <= n]
    return ans_list


# print(len_str())

def firstLetter_str():
    firstLetter = random.choice(string.ascii_letters)
    ans_list = [i for i in random_str(100) if i[0] == firstLetter]
    return ans_list


# print(firstLetter_str())

def firstLetter_str_plus():
    firstLetter = random.choice(string.ascii_letters)
    n = 3
    ans_list = [i for i in random_str(100) if (i[0] == firstLetter and len(i) <= n)]
    return ans_list


print(firstLetter_str_plus())