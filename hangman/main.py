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
    print(f"Word to guess: {display}")
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display_count = sum(1 for char in display if char == guess)
            word_count = sum(1 for char in chosen_word if char == guess)
            if guess in display and display_count == word_count:
                print(f"{guess} is already guessed")
                key = 1
                break
            display[i] = guess
            key = 1
    if key == 0:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(art.stages[lives])
        print(f"You have {lives} lives left")
    else:
        key = 0

if lives > 0:
    print("Congratulations You Win")
else:
    print("Better Luck Next Time")
    print(f"The word was {chosen_word}")
