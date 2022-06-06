from gameCards import *
from gameSetup import *
from gameFunctions import *

playerTracker= 0    # variable to track the current player
win = 0             # variable to check if any player has won the game
parth.drawResource(200,currentResourcePile)

while win == 0:
    endTurn = 0
    while endTurn == 0:
        drawCounter = 0
        currentPlayer = playerList[playerTracker]       # Get current player's object from play list
        print("It's {}'s turn:".format(currentPlayer.name))
        print("**************************************")
        choice = getChoice()
        print("\n")

        if choice == 1:                                 # Chooses to trigger skill cards
            skillCards(currentPlayer)
        elif choice == 2:                               # Chooses to trigger Actionable Card                
            actionCard(currentPlayer, currentActionPile, discardedActionPile, drawCounter)
            
        elif choice == 3:                               # Chooses to view Resources hand
            currentPlayer.printResources()
            print("\n")
        elif choice == 4:
            currentPlayer.printHold()
        elif choice == 5:
            moreOptions()
            print("\n")
        elif choice == 9:

            if checkWin(currentPlayer):
                print("\n**************************************")
                print("Congrats!! {} wins the game".format(currentPlayer.name))
                print("**************************************")
                win = 1
            # if drawCounter == 0:
            #     print("It is compulsory to draw at least 1 card")  
            else:              
                currentPlayer.drawResource(3, currentResourcePile)
                print("\n\n\n**************************************")
                endTurn = 1

    playerTracker += 1
    playerTracker = playerTracker % 3
print("GAME OVER")
    
        
        