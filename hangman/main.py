import random
import art
import words

print(art.logo)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
word_list = words.word_list
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
guessed_words = []
key = 0
lives = 6

while '_' in display and lives > 0:
    print(f"Word to guess: {display}")
    while True:
        guess = input("Guess a letter: ").lower()
        if guess not in alphabets:
            print("Enter valid input")
            continue
        else:
            break
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display_count = sum(1 for char in display if char == guess)
            # stores number of time guessed word is present in display word
            word_count = sum(1 for char in chosen_word if char == guess)
            # stores number of times the guessed word is present in chosen word
            if guess not in guessed_words:
                guessed_words.append(guess)
            if guess in display and display_count == word_count:
                print(f"{guess} is already guessed")
                key = 1
                break
            display[i] = guess
            key = 1
    if key == 0:
        if guess in guessed_words:
            print(f"{guess} is already guessed")
            continue
        else:
            guessed_words.append(guess)
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            print(art.stages[lives])
            print(f"You have {lives} lives left")
    else:
        key = 0

if lives > 0:
    print("Congratulations You Win!!")
else:
    print("Better Luck Next Time :)")
print(f"The word was '{chosen_word}'")
