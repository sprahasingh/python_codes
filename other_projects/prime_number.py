import math


def prime_checker(number):
    key = False
    if number <= 1 or number == 2 or number == 3:
        key = False
    else:
        for i in range(2, (int(math.sqrt(number)) + 1)):
            if number % i == 0:
                key = True
            if key:
                break
    if not key:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = 1
while True:
    n = int(input("Enter the number to check or 0 to exit\n"))
    if n == 0:
        exit()
    prime_checker(n)
