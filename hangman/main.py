import random
import art
import words

print(art.logo)
word_list = words.word_list
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
key = 0
lives = 6

while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            if guess in display:
                print(f"{guess} is already guessed")
            display[i] = guess
            key = 1
    if key == 0:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(art.stages[lives])
        print(f"You have {lives} lives left")
    else:
        key = 0
    print(display)

if lives > 0:
    print("Congratulations You Win")
else:
    print("Better Luck Next Time")
    print(f"The word was {chosen_word}")
