print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n").upper()
name2 = input("What is their name?\n").upper()
name = name1 + name2
t_count = name.count("T")
r_count = name.count("R")
u_count = name.count("U")
e1_count = name.count("E")
l_count = name.count("L")
o_count = name.count("O")
v_count = name.count("V")
e2_count = name.count("E")
num1 = t_count + r_count + u_count + e1_count
num2 = l_count + o_count + v_count + e2_count
score = int(str(num1) + str(num2))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
