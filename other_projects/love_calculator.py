print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n").upper()
name2 = input("What is their name?\n").upper()
name = name1 + name2
t = name.count("T")
r = name.count("R")
u = name.count("U")
e1 = name.count("E")
l = name.count("L")
o = name.count("O")
v = name.count("V")
e2 = name.count("E")
num1 = t + r + u + e1
num2 = l + o + v + e2
score = int(str(num1) + str(num2))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
