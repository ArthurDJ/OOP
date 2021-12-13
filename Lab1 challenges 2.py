import math


def isPrime(n):
    if n <= 3:
        return ("prime" if (n > 1) else "not prime")
    if n % 6 != 1 and n % 6 != 5:
        return "not prime"

    for i in range(5, int(math.sqrt(n)), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return "not prime"
    return "prime"


n = 123457
print(isPrime(n))
