import random

print("Heads or Tails")
start = input("Press enter to start\n")
num = random.randint(0, 1)
if num == 1:
    print("You got Heads")
else:
    print("You got Tails")
