import random
user_input = input("Enter comma-separated names:\n")
names = user_input.split(",")
names = [item.strip() for item in names]
size = len(names)
index = random.randint(0,size-1)
print(f"{names[index]} is going to buy the meal today!")