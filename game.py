# 21 Blackjack game
import random
import os
import time

"""CONSTANTS"""
# For now, Ace will be always be one
cardValues = {"Ace":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}
# Overall, suits are nothing but I'll include them for the aesthetic for later
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
BUSTED_TEXT_ART = "\n\t=======================\n\t‖       Busted!       ‖\n\t=======================\n"
DEALER_BUST_TEXT_ART = "\n\t=======================\n\t‖     Dealer bust!    ‖\n\t=======================\n"


""" FUNCTIONS: TOOLS """

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

""" FUNCTIONS: CARDS """
# Generates a random card. Value, Suit
def generateCard():
    return random.choice(list(cardValues.keys())), random.choice(suits)

# Uses generateCard() to deal 2 cards to each player and dealer. Initial Deal.
def dealCards(p, d):
    for i in range(2):
        p.append(generateCard())
        d.append(generateCard())

    displayCards(p, d)


# Returns the value of the hand
def cardTotal(hand):
    total = 0
    for i in hand:
        # gets the numerical value to the key of each card in the list of held cards and adds it to the total
        total += cardValues.get(i[0])

    return total


# Checks if player has busted. Will account for aces in future
def isBust(hand): # TODO: Ace exception
    if cardTotal(hand) > 21:
        return True
    else:
        return False



""" FUNCTIONS: DISPLAY """
# Prints the cards on the screen
def displayCards(p, d):
    clear()

    if isBust(p):
        print(BUSTED_TEXT_ART)

    print("Player has :")
    for i in p:
        print(i[0]+" of "+ i[1])
    print("Total: "+ str(cardTotal(p)))

    print("\nDealer has :")
    for i in d:
        print(i[0]+" of "+ i[1])
    print("Total: "+ str(cardTotal(d)))


def continueGame():
    input("\n\nPress Enter to continue...")
    menu()

def playerWin():
    # In future versions, this will do something with bets
    print("\n\nPlayer Win. Congrats!")
    continueGame()

def dealerBust():
    print(DEALER_BUST_TEXT_ART)
    playerWin()

def dealerWin():
    # In future versions, this will do something with bets
    print("\n\nDealer Win. Sorry!")
    continueGame()

def gameTie():
    print("\n\nTied.")
    continueGame()



""" FUNCTIONS: ACTIONS """
def actionHit(hand):
    hand.append(generateCard())



""" FUNCTIONS: ACTIONS - USER """
def userAction(hand, dHand):
    print("\nCommands: h = Hit\ts = Stand")
    userInput = input("Input:")

    if userInput == "h":
        actionHit(hand)
    elif userInput == "s":
        dealerAction(dHand, hand)
    else:
        print("Invalid Input")



""" FUNCTIONS: ACTIONS - DEALER """
def dealerAction(hand, phand):
    # Dealer must draw to 16, stand on 17
    while cardTotal(hand) <= 16:
        actionHit(hand)
        displayCards(phand, hand)

    dealerStand(hand, phand)


def dealerStand(dhand, phand):
    if cardTotal(dhand) > 21:
        dealerBust()
    elif cardTotal(phand) > cardTotal(dhand):
        playerWin()
    elif cardTotal(dhand) > cardTotal(phand):
        dealerWin()
    elif cardTotal(phand) == cardTotal(dhand):
        gameTie()


""" FUNCTIONS: MAIN """
def playGame():
    playerCards = []
    dealerCards = []

    dealCards(playerCards, dealerCards)

    while not isBust(playerCards):
        userAction(playerCards, dealerCards)
        displayCards(playerCards, dealerCards)


def menu():
    userInput = str()
    clear()
    print("Welcome to 21 Blackjack. Made by Kevin Geng.\n\n")

    while (userInput != "q"):
        userInput = str()
        print("Commands: n = New Game\tq = Quit")
        userInput = input("Input: ")

        if userInput == "n":
            playGame()


if __name__ == "__main__":
    menu()
