import art
print(caesar_cipher_art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text,shift,direction):
    for i in range(0, len(text)):
        index = alphabet.index(text[i])
        if direction=='encode':
            index=(index+shift)%(len(alphabet))
        else:
            index=(index-shift)%(len(alphabet))
        text=text[:i] + alphabet[index] + text[i+1:]
    print(f"The {direction}d text is {text}")
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to exit:\n").lower()
    if direction not in {'encode', 'decode', 'exit'}:
        print("Enter valid input")
        continue
    if direction=='exit':
        print("GoodBye!")
        exit()
    text = input("Type your message:\n").lower()
    for letter in text:
        flag=False
        if letter not in alphabet:
            print("Enter valid input")
            flag=True
            break
    if flag:
        continue
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)