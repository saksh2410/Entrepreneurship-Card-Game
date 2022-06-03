from gameCards import *
from gameSetup import *
from gameFunctions import *

playerTracker= 0
endTurn= 0
drawCounter = 1
while endTurn == 0:
    currentPlayer = playerList[playerTracker]       # Get current player's object from play list
    print("It's {}'s turn:".format(currentPlayer.name))
    print("************************")
    choice = getChoice()
    print("\n")

    if choice == 1:                                 # Chooses to trigger skill cards
        skillCards(currentPlayer)
    elif choice == 2:                               # Chooses to trigger actionable cards
        actionCards(currentPlayer, currentActionPile, discardedActionPile, drawCounter)
    elif choice == 3:                               # Chooses to view Resources hand
        currentPlayer.printResources()
    elif choice == 4:
        currentPlayer.printHold()
    elif choice == 9:
        endTurn =12
        