#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_last = number % 10
else:
    last_last = number % -10
print("Last digit of", number, "is", last_last, end=' ')
if last_last > 5:
    print("and is greater than 5")
elif last_last == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
