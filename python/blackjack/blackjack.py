#!/usr/bin/python3

import random, time, turtle

#wn = turtle.Screen()
#wn.screensize(400, 600)
#wn.title("Blackjack")
#
# Pen Setup
#text_turtle = turtle.Pen("arrow", 0, False)
#text_turtle.penup()
#text_turtle.setpos(-240.00, 240.00)
#text_turtle.write("test",font=("Times New Roman", 24, "normal"))

def play_again():
    if input("Would you like to play again? y/n: ") == "y":
        blackjack()
    else:
        exit()

def blackjack():
    # cn = card number
    cn = []
    suits = ["Hearts","Diamonds","Clubs","Spades"]
    deck = []
    for i in range(1,14):
        cn.append(i)

    for i in suits:
        for j in cn:
            named_cards = ""
            temp_list = []
            if j == 1 or j > 10:
                if j == 1:
                    named_card = "Ace"
                elif j == 11:
                    named_card = "Jack"
                elif j == 12:
                    named_card = "Queen"
                elif j == 13:
                    named_card = "King"
                temp_list = [j,i,named_card]
            else:
                temp_list = [j,i]

            deck.append(temp_list)

    random.shuffle(deck)

    counter = 0
    player_bar = 0
    dealer_bar = 0

    while counter <= 52:
        user_input = input("Hit/Stay: ")
        if user_input == "h":
            if len(deck[counter]) == 3:
                #pc = player card
                pc = str(deck[counter][2]) + " of " + str(deck[counter][1])
            else:
                pc = str(deck[counter][0]) + " of " + str(deck[counter][1])
            player_bar += deck[counter][0]
            print("\nPlayer: " + pc)

            counter += 1

            if len(deck[counter]) == 3:
                #dc = dealer card
                dc = str(deck[counter][2]) + " of " + str(deck[counter][1])
            else:
                dc = str(deck[counter][0]) + " of " + str(deck[counter][1])
            dealer_bar += deck[counter][0]
            print("Dealer: " + dc + "\n")

            print("Player Score: " + str(player_bar) + "\n" + "Dealer Score: " 
                    + str(dealer_bar) + "\n")

            if player_bar > 21:
                print("Game Over. Dealer Wins")
                play_again()
            elif player_bar == 21:
                print("Perfect Score! Player Wins")
                play_again()
            elif dealer_bar > 21:
                print("Game Over. Player Wins")
                play_again()
            elif dealer_bar == 21:
                print("Dealer Wins")
                play_again()

            counter += 1

        elif user_input == "exit":
            exit()

        elif user_input == "s":
            print("Player stays at " + str(player_bar))
            #duplicate code. Find a way to streamline
            if len(deck[counter]) == 3:
                #dc = dealer card
                dc = str(deck[counter][2]) + " of " + str(deck[counter][1])
            else:
                dc = str(deck[counter][0]) + " of " + str(deck[counter][1])

            dealer_bar += deck[counter][0]
            print("Dealer: " + dc + "\n")

            if dealer_bar > 21:
                print("Game Over. Player Wins")
                play_again()
            counter += 1

            print("Player Score: " + str(player_bar) + "\n" + "Dealer Score: " + str(dealer_bar))

        else:
            print("Please enter either h/s/exit: ")

blackjack()
