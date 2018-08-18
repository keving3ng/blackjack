# 21 Blackjack game
import random

# For now, Ace will be always be one
cardValues = {"Ace":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}
# Overall, suits are nothing but I'll include them for the aesthetic for later
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

# Generates a random card. Value, Suit
def generateCard():
    return random.choice(list(cardValues.keys())), random.choice(suits)

# Uses generateCard() to deal 2 cards to each player and dealer. Initial Deal.
def dealCards(p, d):
    for i in range(2):
        p.append(generateCard())
        d.append(generateCard())

    displayCards(p, d)

# Checks if player has busted. Will account for aces in future
def isBust(hand): # TODO: Ace exception
    if cardTotal(hand) > 21:
        return True
    else:
        return False

# Returns the value of the hand
def cardTotal(hand):
    total = 0
    for i in hand:
        # gets the numerical value to the key of each card in the list of held cards and adds it to the total
        total += cardValues.get(i[0])

    return total

# Prints the cards on the screen
def displayCards(p, d):
    print("\nPlayer has :")
    for i in p:
        print(i[0]+" of "+ i[1])
    print("Total: "+ str(cardTotal(p)))

    print("\nDealer has :")
    for i in d:
        print(i[0]+" of "+ i[1])
    print("Total: "+ str(cardTotal(d)))

def actionHit(hand):
    hand.append(generateCard())
    return 0


def userAction(hand):
    print("\nCommands: h = Hit\ts = Stand")
    userInput = input("Input:")

    if userInput == "h":
        actionHit(hand)
    elif userInput == "s":
        print("stand")
    else:
        print("Invalid Input")

    if isBust(hand):
        print("\n\t=======================\n\t======= Busted! =======\n\t=======================\n")

def playGame():
    playerCards = []
    dealerCards = []

    userInput = str()

    while (userInput != "q"):
        print("\nCommands: n = New Game\tq = Quit")
        userInput = input("Input: ")

        if userInput == "n":
            dealCards(playerCards, dealerCards)

            while not isBust(playerCards):
                userAction(playerCards)
                displayCards(playerCards, dealerCards)


if __name__ == "__main__":
    playGame()


    # When this is integrated with the front end, there will be a start game button
