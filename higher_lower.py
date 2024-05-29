from higher_lower_art import logo, vs
from higher_lower_data import data
import random

def game(level,a,b,score,prev) :
    def replay(level,a,b,score,prev) :
        while True:
            again = input("Enter '1' to play again, '0' to exit\n")
            if again == '1' :
                game(level,a,b,score,prev)
                break
            elif again == '0' :
                exit()
            else:
                print("Enter valid input")
                continue
    while True:
        print(f"Current level: {level}, Current score: {score}")
        if level == 1:
            a = random.choice(data)
        b = random.choice(data)
        while a == b or (b['name'] in prev):
            b = random.choice(data)
        print(f"\nCompare A: {a['name']}, {a['description']}, from {a['country']}")
        print(vs)
        print(f"Against B: {b['name']}, {b['description']}, from {b['country']}\n")
        while True:
            guess = input("Who has more followers? Type 'A' or 'B':\n").upper()
            if (guess == 'A' and a['follower_count'] > b['follower_count']) or (guess == 'B' and a['follower_count'] < b['follower_count']) :
                print("You Win")
                if a['follower_count'] < b['follower_count'] :
                    prev.append(a['name'])
                    a = b
                elif a['follower_count'] > b['follower_count'] :
                    prev.append(b['name'])
                if len(prev) == len(data)-1:
                    print("CONGRATULATIONS!! YOU WIN THE GAME!!")
                level+=1
                score+=1
                replay(level,a,b,score,prev)
                    
            elif (guess == 'A' and a['follower_count'] < b['follower_count']) or (guess == 'B' and a['follower_count'] > b['follower_count']) :
                print("You lose")
                prev=[]
                print(f"Final score: {score}")
                level = 1
                score = 0
                replay(level,a,b,score,prev)
            else:
                print("Enter valid input")
                continue
            break
prev = []
a = {}
b = {}
level = 1
score=0
print(logo)
game(level,a,b,score,prev)