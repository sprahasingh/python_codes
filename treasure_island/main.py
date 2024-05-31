import art

print(art.logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroads. Do you want to go left or right?")
direction = input("Type 'left' or 'right': ").lower()
if direction == "left":
    print(
        "You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type "
        "'swim' to swim across."
    )
    lake = input("Type 'wait' or 'swim': ").lower()
    if lake == "wait":
        print(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. "
            "Which colour do you choose?"
        )
        door = input("Type 'red', 'yellow' or 'blue': ").lower()
        if door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
