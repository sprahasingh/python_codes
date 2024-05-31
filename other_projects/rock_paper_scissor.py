import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number, you lose!")
    exit()
computer_choice = random.randint(0, 2)
choices = [rock, paper, scissors]
print("Your choice:")
print(choices[user_choice])
print("Computer choice:")
print(choices[computer_choice])
if user_choice == computer_choice:
    print("It's a Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice > computer_choice :
    print("You win")
else:
    print("You lose")
