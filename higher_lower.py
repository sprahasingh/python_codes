from higher_lower_art import logo, vs
from higher_lower_data import data
import random

def replay(level,a,b,score) :
    while True:
        again = input("Enter '1' to play again, '0' to exit\n")
        if again == '1' :
            game(level,a,b,score)
            break
        elif again == '0' :
            exit()
        else:
            print("Enter valid input")
            continue

def game(level,a,b,score) :
    while True:
        print(f"Current level: {level}, Current score: {score}")
        if level == 1:
            num_a = random.randint(0,49)
            a = data[num_a]
        num_b = random.randint(0,49)
        b = data[num_b]
        print(f"\nCompare A: {a['name']}, {a['description']}, from {a['country']}")
        print(vs)
        print(f"Against B: {b['name']}, {b['description']}, from {b['country']}\n")
        while True:
            guess = input("Who has more followers? Type 'A' or 'B':\n")
            if (guess == 'A' and a['follower_count'] > b['follower_count']) or (guess == 'B' and a['follower_count'] < b['follower_count']) :
                print("You Win")
                if a['follower_count'] < b['follower_count'] :
                    a = b
                level+=1
                score+=1
                replay(level,a,b,score)
            elif (guess == 'A' and a['follower_count'] < b['follower_count']) or (guess == 'B' and a['follower_count'] > b['follower_count']) :
                print("You lose")
                print(f"Final score: {score}")
                level = 1
                score = 0
                replay(level,a,b,score)
            else:
                print("Enter valid input")
                continue
            break
a = {}
b = {}
level = 1
score=0
print(logo)
game(level,a,b,score)