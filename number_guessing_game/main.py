import random
import art

print("Welcome to the Number Guessing Game!")


def replay():
    while True:
        again = input("Press '1' to play again, '0' to exit\n")
        if again == '1':
            play()
        elif again == '0':
            exit()
        else:
            print("Enter valid input")
            continue


def play():
    while True:
        print("I'm thinking of a number between 1 and 100.")
        number = random.randint(1, 100)
        attempts = 0
        while True:
            level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
            if level == 'easy':
                attempts = 10
                break
            elif level == 'hard':
                attempts = 5
                break
            else:
                print("Enter valid input")
                continue
        print(f"You have {attempts} attempts remaining to guess the number.")
        while True:
            attempts -= 1
            guess = int(input("Make a guess\n"))
            if guess < number:
                if number - guess <= 5:
                    print("Guess a little higher")
                else:
                    print("Your guess is too low")
            elif guess > number:
                if guess - number <= 5:
                    print("Guess a little lower")
                else:
                    print("Your guess is too high")
            else:
                print(f"You got it! The answer was {number}.")
                replay()
                break
            if attempts == 0:
                print(f"You've run out of guesses, you lose. The answer was {number}")
                replay()
                break
            else:
                print(f"You have {attempts} attempts remaining to guess the number.")
                continue


print(art.logo)
play()
