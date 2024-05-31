import random
import clear
import art
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']
card_dict = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'K': 10, 'Q':10, 'J': 10}
def deal_card():
    return random.choice(cards)
def play_again(game_num,user_win,comp_win):
    while True:
        again = input("Do you want to play again? Enter '1' to play again, '0' to exit\n").lower()
        clear.clear_console()
        if again == '1' :
            game(game_num,user_win,comp_win)
        elif again == '0':
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
    for _ in range(2) :
        comp_cards.append(deal_card())
        user_cards.append(deal_card())
    print(f"Comp cards are ['{comp_cards[0]}', 'X']")
    comp_score = card_dict[comp_cards[0]] + card_dict[comp_cards[1]]
    if comp_score == 22 :
        card_dict["A"] = 1
        comp_score = 12
    print(f"Your cards are {user_cards}")   
    user_score = card_dict[user_cards[0]] + card_dict[user_cards[1]]
    if user_score == 22 :
        card_dict["A"] = 1
        user_score = 12   
    print(f"Your score is {user_score}")
    if user_score == 21 :
        if comp_score == 21 :
            print(f"Comp final hand: {comp_cards}, Comp final score: {comp_score}")
            print(f"Your final hand: {user_cards}, Your final score: {user_score}")
            print("Push")
        else:
            print("BlackJack. You Win")
            user_win+=1
        print(f"Your wins: {user_win}\nComp wins: {comp_win}")
        game_num+=1
        play_again(game_num,user_win,comp_win)
    while user_score < 21 :
        choice = input("Enter '1' to take an extra card, Enter '0' to stop taking cards\n").lower()
        if choice == '1' :
            i+=1
            user_cards.append(deal_card())
            if user_cards[i] == "A" and user_score > 10 :
                card_dict["A"] = 1
            print(f"Your cards are {user_cards}")
            user_score+=card_dict[user_cards[i]]
            print(f"Your score is {user_score}")
        elif choice == '0':
            break
        else:
            print("Enter valid input")
            continue
        if user_score > 21 :
            print("Bust (You)\nYou lose")
            comp_win+=1
            print(f"Your wins: {user_win}\nComp wins: {comp_win}")
            game_num+=1
            play_again(game_num,user_win,comp_win)

    while comp_score <17 :
        j+=1
        comp_cards.append(deal_card())
        comp_score+=card_dict[comp_cards[j]]
        if comp_score > 21 :
            print(f"Comp final hand: {comp_cards}, Comp final score: {comp_score}")
            print(f"Your final hand: {user_cards}, Your final score: {user_score}")
            print("Bust (Comp)\nYou win")
            user_win+=1
            print(f"Your wins: {user_win}\nComp wins: {comp_win}")
            game_num+=1
            play_again(game_num,user_win,comp_win)
    print(f"Comp final hand: {comp_cards}, Comp final score: {comp_score}")
    print(f"Your final hand: {user_cards}, Your final score: {user_score}")
    if user_score > comp_score :
        print("You win")
        user_win+=1
        print(f"Your wins: {user_win}\nComp wins: {comp_win}")
    elif comp_score > user_score:
        print("You lose")
        comp_win+=1
        print(f"Your wins: {user_win}\nComp wins: {comp_win}")
    elif user_score == comp_score:
        print("Push")
        print(f"Your wins: {user_win}\nComp wins: {comp_win}")
    game_num+=1
    play_again(game_num,user_win,comp_win)
print(blackjack_art.logo)
print("WELCOME TO BLACKJACK")
hit = input("Press ENTER to start")
game_num = 1
user_win = 0
comp_win = 0
game(game_num,user_win,comp_win)