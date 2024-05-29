import random
import clear
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']
card_dict = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'K': 10, 'Q':10, 'J': 10}
def generate_card():
    chosen_card = cards[random.randint(0,(len(cards)-1))]
    return chosen_card
def play_again(game_num,user_win,comp_win):
    while True:
        again = input("Do you want to play again? Enter 'y' to play again, 'n' to exit\n").lower()
        clear.clear_console()
        if again == 'y' :
            game(game_num,user_win,comp_win)
        elif again == 'n':
            print(f"Total games: {game_num} Your wins: {user_win}  Comp wins: {comp_win}")
            if user_win > comp_win :
                print("Congratulations! You Win")
            elif comp_win > user_win :
                print("Better Luck Next Time")
            else:
                print("Its a Draw :)")
            exit()
        else:
            print("Enter valid input")
            continue
def game(game_num,user_win,comp_win):
    print(f"Game number: {game_num} Your wins: {user_win}  Comp wins: {comp_win}")
    card_dict["A"] = 11
    comp_cards = [] 
    user_cards = []
    i = 1
    j = 1
    comp_cards.append(generate_card())
    comp_cards.append(generate_card())
    print(f"Comp cards are ['{comp_cards[0]}', 'X']")
    comp_sum = card_dict[comp_cards[0]] + card_dict[comp_cards[1]]
    if comp_sum == 22 :
        card_dict["A"] = 1
        comp_sum = 12
    user_cards.append(generate_card())
    user_cards.append(generate_card())
    print(f"Your cards are {user_cards}")
    user_sum = card_dict[user_cards[0]] + card_dict[user_cards[1]]
    if user_sum == 22 :
        card_dict["A"] = 1
        user_sum = 12   
    print(f"Your total sum is {user_sum}")
    if user_sum == 21 :
        print(f"Comp cards: {comp_cards}, Comp total: {comp_sum}")
        print(f"Your cards: {user_cards}, Your total: {user_sum}")
        if comp_sum == 21 :
            print("Push")
            print(f"Your wins: {user_win}\nComp wins: {comp_win}")
        else:
            print("BlackJack. You Win")
            user_win+=1
        print(f"Your wins: {user_win}\nComp wins: {comp_win}")
        game_num+=1
        play_again(game_num,user_win,comp_win)
    while user_sum < 21 :
        choice = input("Enter 'hit' to take an extra card, Enter 'stand' to stop taking cards\n").lower()
        if choice == 'hit' :
            i+=1
            user_cards.append(generate_card())
            if user_cards[i] == "A" and user_sum > 10 :
                card_dict["A"] = 1
            print(f"Your cards are {user_cards}")
            user_sum+=card_dict[user_cards[i]]
            print(f"Your total sum is {user_sum}")
        elif choice == 'stand':
            break
        else:
            print("Enter valid input")
            continue
        if user_sum > 21 :
            print("Bust(You)\nYou lose")
            comp_win+=1
            print(f"Your wins: {user_win}\nComp wins: {comp_win}")
            game_num+=1
            play_again(game_num,user_win,comp_win)

    while comp_sum <17 :
        j+=1
        comp_cards.append(generate_card())
        comp_sum+=card_dict[comp_cards[j]]
        if comp_sum > 21 :
            print(f"Comp cards: {comp_cards}, Comp total: {comp_sum}")
            print(f"Your cards: {user_cards}, Your total: {user_sum}")
            print("Bust(Comp)\nYou win")
            user_win+=1
            print(f"Your wins: {user_win}\nComp wins: {comp_win}")
            game_num+=1
            play_again(game_num,user_win,comp_win)
    print(f"Comp cards: {comp_cards}, Comp total: {comp_sum}")
    print(f"Your cards: {user_cards}, Your total: {user_sum}")
    if user_sum > comp_sum :
        print("You win")
        user_win+=1
        print(f"Your wins: {user_win}\nComp wins: {comp_win}")
    elif comp_sum > user_sum:
        print("You lose")
        comp_win+=1
        print(f"Your wins: {user_win}\nComp wins: {comp_win}")
    elif user_sum == comp_sum:
        print("Push")
        print(f"Your wins: {user_win}\nComp wins: {comp_win}")
    game_num+=1
    play_again(game_num,user_win,comp_win)
print("WELCOME TO BLACKJACK")
hit = input("Press ENTER to start")
game_num = 1
user_win = 0
comp_win = 0
game(game_num,user_win,comp_win)