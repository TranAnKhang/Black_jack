from random import *
from time import *

def sum_of_2_cards(first_card, second_card): 
    sum_of_2_cards = first_card + second_card
    return sum_of_2_cards

def sum_of_3_cards(third_card):
    sum_of_3_cards = third_card + sum_of_2_cards(first_card, second_card) 
    return sum_of_3_cards

def sum_of_4_cards(final_card):
    sum_of_4_cards = sum_of_3_cards(third_card) + final_card
    return sum_of_4_cards

def first_card_conversion(first_card):
    if first_card == 1 or first_card == 11:
        first_card = "ace"
    elif first_card == 10:
        cards = ["jack","king","queen"]
        first_card = choice(cards)
    return first_card

def second_card_conversion(second_card):
    if second_card == 1 or second_card == 11:
        second_card = "ace"
    elif second_card == 10:
        cards = ["jack","king","queen"]
        second_card = choice(cards)
    return second_card
def third_card_conversion(third_card):
    if third_card == 1 or third_card == 11:
        third_card = "ace"
    elif third_card == 10:
        cards = ["jack","king","queen"]
        third_card = choice(cards)
    return third_card
def final_card_conversion(final_card):
    if final_card == 1 or final_card == 11:
        final_card = "ace"
    elif final_card == 10:
        cards = ["jack","king","queen"]
        final_card = choice(cards)
    return final_card

def check_bot_card(res):
    bot_card = randint(15,24)
    print("The bot had a sum of:", bot_card)
    sleep(1)
    if res > 21:
        if bot_card > 21:
            print("You both busted! Its a draw!")
        else:
            print("You busted! Better luck next time!")

    elif res <= 21:
        if res > bot_card:
            print("Congrats! You've won!!!")
        elif bot_card == res:
            print("You both had the same sum! Its a draw!")
        else: 
            if bot_card <= 21:
                print("The bot had a bigger sum! Better luck next time!")
            else:
                print("Congrats! You've won!!!")
print("WELCOME TO THE ROYAL CASINO!!!")
start = int(input("Enter 1 - start, 0 - End"))
while start != 0:
    decision = input("Would you like to play a game of blackjack? (yes/no)")
    if decision == "yes":
        print("Lets begin!")
        print("Shuffling ...")
        first_card = randint(1,11)
        second_card = randint(1,11)
        res = sum_of_2_cards(first_card, second_card)
        sleep(4)
        print("Here are your cards:")
        print("1st card:", first_card_conversion(first_card))
        print("2nd card:", second_card_conversion(second_card))
        draw_card = input("Would you like to draw another card? (yes/no)")
        if draw_card == "yes":
            sleep(2)
            third_card = randint(1,10)
            print("3rd card:", third_card_conversion(third_card))
            res = sum_of_3_cards(third_card)
            draw_another_card = input("Would you like to draw another card? (yes/no)")
            if draw_another_card == "yes":
                final_card = randint(1,10)
                res = sum_of_4_cards(final_card)
                print("4th card:", final_card_conversion(final_card))
                print("The total for your cards are:", sum_of_4_cards(final_card))
                check_bot_card(res)
            else: 
                print("The total for your cards are:", sum_of_3_cards(third_card))
                check_bot_card(res)
        else:
            print("The total for your cards are:", sum_of_2_cards(first_card, second_card))
            check_bot_card(res)
    else:
        print("Lets have a game of Rock Paper Scissor! (stop - end)")
        from Hi import *
        welcome()
        output()
        gameStart(playerChoice, computerChoice, score)
        playerChoice = ""
        while playerChoice != "stop":
            choice = ["rock", "paper", "scissors"]
            computerChoice = random.choice(choice)
            print("Ok let's play.")
            print("Score: %s" % score)
            playerChoice = input("Enter your choice here: ")
            if playerChoice.lower() == "r":
                playerChoice = "Rock"
            elif playerChoice.lower() == "p":
                playerChoice = "Paper"
            elif playerChoice.lower() == "s":
                playerChoice = "Scissors"
                playerChoice = playerChoice.lower()
            if (not playerChoice in choices) and playerChoice != "stop":
                print("invalid word")
                break
            if playerChoice != "stop":
                score = gameStart(playerChoice, computerChoice, score)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> " + "YOUR SCORE: {}".format(score))
                rounds()
            start = int(input("Enter 1 - start, 0 - End"))