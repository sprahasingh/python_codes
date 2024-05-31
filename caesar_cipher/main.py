import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def caesar(str_text, int_shift, str_direction):
    for i in range(0, len(str_text)):
        index = alphabet.index(str_text[i])
        if str_direction == 'encode':
            index = (index + int_shift) % (len(alphabet))
        else:
            index = (index - int_shift) % (len(alphabet))
        str_text = str_text[:i] + alphabet[index] + str_text[i + 1:]
    print(f"The {str_direction}d text is {str_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to exit:\n").lower()
    if direction not in {'encode', 'decode', 'exit'}:
        print("Enter valid input")
        continue
    if direction == 'exit':
        print("GoodBye!")
        exit()
    text = input("Type your message:\n").lower()
    flag = False
    for letter in text:
        if letter not in alphabet:
            print("Enter valid input")
            flag = True
            break
    if flag:
        continue
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
