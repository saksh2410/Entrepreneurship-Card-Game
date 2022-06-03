def getChoice():        # function to get users choice of action on their turn
    print("1. Buy Skill Cards")
    print("2. Buy Actionable Cards")
    print("3. View Resources in Hand")
    print("4. View Entire Hand")
    print("9. End Turn\n")
    userChoice = int(input())

    if userChoice == 1 or userChoice == 2 or userChoice == 3 or userChoice == 9 or userChoice == 4:
        return userChoice
    else:
        print("Please enter a valid choice")
        getChoice()

def skillCards(player):       # Function for user to trigger Skill Cards
    player.printSkillLevel()
    print("\n")

    # definig cost of different skill levels
    generalCost = [500, 2000, 4000, 6000]
    specialCost = [1500, 3500,  4500, 7000]

    # unpacking level of expertise in each area
    research = player.skillLevel[0]
    marketing = player.skillLevel[1]
    design = player.skillLevel[2]
    technology = player.skillLevel[3]

    # asking user which skill if any they want to upgrade
    print("The Cost of Buying next level skill is:")
    print("1. Research (lvl {}): {}".format(research + 1, generalCost[research]))
    print("2. Marketing (lvl {}): {}".format(marketing + 1, generalCost[marketing]))
    print("3. Design (lvl {}): {}".format(design + 1, specialCost[design]))
    print("4. Technology (lvl {}): {}".format(technology + 1, specialCost[technology]))
    print("5. Back to Turn Menue")
    print("\n")
    boughtSkill = int(input())

    if boughtSkill== 1:
        if generalCost[research] <= player.money:
            player.skillLevel[0] += 1
            print("\nCongrats, you upskilled Research to lvl {}\n".format(player.skillLevel[0]))
            player.money -= generalCost[research]
        else:
            print("\nNot enough money to upskill\n")
    elif boughtSkill== 2:
        if generalCost[marketing] <= player.money:
            player.skillLevel[1] += 1
            print("\nCongrats, you upskilled Marketing to lvl {}\n".format(player.skillLevel[1]))
            player.money -= generalCost[marketing]
        else:
            print("\nNot enough money to upskill\n")
    elif boughtSkill== 3:
        if specialCost[design] <= player.money:
            player.skillLevel[2] += 1
            print("\nCongrats, you upskilled Design to lvl {}\n".format(player.skillLevel[2]))
            player.money -= generalCost[design]
        else:
            print("\nNot enough money to upskill\n")
    if boughtSkill== 4:
        if specialCost[technology] <= player.money:
            player.skillLevel[3] += 1
            player.money -= generalCost[technology]
        else:
            print("Not enough money to upskill")
    
    
generalSkillReduction = [0, 1, 3, 6, 9]
specialSkillReduction = [0, 2, 5, 8, 11]




def actionCardsv2(player, currentActionPile, discardedActionPile):   # Function for user to trigger Actionable Cards
    
    print("Top Opened Action Card:")
    print(discardedActionPile[-1])

    print("Do you want to buy it? y/n")
    actionCardChoice= int(input())

    def buyActionCard(drawnActionCard):
        player.time -= drawnActionCard[1]
        
        if drawnActionCard[0]=="research":
            player.actionCards[0]+=1

        elif drawnActionCard[0]=="marketing":
            player.actionCards[1]+=1

        elif drawnActionCard[0]=="design":
            player.actionCards[2]+=1

        elif drawnActionCard[0]=="technology":
            player.actionCards[3]+=1
        
        discardedActionPile.pop()
        print("You have bought {} action card ".format(drawnActionCard))

    def drawCard():
    
            drawnActionCard =currentActionPile.pop()
            discardedActionPile.append(drawnActionCard)
            print("The drawn Action card is {}".format(drawnActionCard))

    def buyActionCard():
        boughtCard = discardedActionPile.pop()
        print("You bought")

    if actionCardChoice== 'n' or actionCardChoice== 'N':
        drawCard()
    elif actionCardChoice== 'y' or actionCardChoice== 'Y':
        buyActionCard()


def actionCardsv3(player,currentActionPile,discardedActionPile):

    
    def buyActionCard(drawnActionCard):
        player.time -= drawnActionCard[1]
        
        if drawnActionCard[0]=="research":
            player.actionCards[0]+=1

        elif drawnActionCard[0]=="marketing":
            player.actionCards[1]+=1

        elif drawnActionCard[0]=="design":
            player.actionCards[2]+=1

        elif drawnActionCard[0]=="technology":
            player.actionCards[3]+=1
        
        discardedActionPile.pop()
        print("You have bought {} action card ".format(drawnActionCard))
        
    def cardDrawn():

            drawnActionCard=currentActionPile.pop()
            print("The drawn Action card is {}".format(drawnActionCard))
            discardedActionPile.append(drawnActionCard)

            print("1.Buy action card")
            print("2.Draw another Action card for 1000$")
            print("3.Pass")

            drawnChoice=1
            while drawnChoice==1:

                drawnChoiceNumber=int(input())

                if drawnChoiceNumber==1:
                    buyingComplete=0

                    while buyingComplete==0:
                        buyActionCard(discardedActionPile[-1])
                        print("Do you want to buy the next top card")
                        print("0.Yes")
                        print("1.No")
                        buyingComplete=int(input())
                        drawnChoiceNumber=0
                    return 0                        

                elif drawnChoiceNumber==2:
                    player.money -= 1000
                    cardDrawn()
                    drawnChoiceNumber=0
                    return 0
                
                elif drawnChoiceNumber==3:
                    drawnChoiceNumber=0
                    return 0
    print("Top Opened Action Card:")
    print(discardedActionPile[-1])

    print("1.Draw action card from pile")
    print("2.Buy opened Action card")
    

    actionCardChoice=int(input())

    if actionCardChoice==1:
        cardDrawn()
        return 0
            
    elif actionCardChoice==2:

        buyingComplete=0

        while buyingComplete==0:
            buyActionCard(discardedActionPile[-1])
            print("Do you want to buy the next top card")
            print("0.Yes")
            print("1.No")
            buyingComplete=int(input())
        return 0
    return 0


def actionCards(player,currentActionPile,discardedActionPile,counter):
    
    def buyActionCard(drawnActionCard):

        startingLetter=drawnActionCard[0][0]
        if startingLetter=='r':
            modifiedCost=drawnActionCard[1] - generalSkillReduction[player.skillCards[0]]
        elif startingLetter=='m':
            modifiedCost=drawnActionCard[1] - generalSkillReduction[player.skillCards[1]]
        elif startingLetter=='d':
            modifiedCost=drawnActionCard[1] - specialSkillReduction[player.skillCards[2]]
        elif startingLetter=='t':
            modifiedCost=drawnActionCard[1] - specialSkillReduction[player.skillCards[3]]



        player.time -= modifiedCost
        
        if drawnActionCard[0]=="research":
            player.actionCards[0]+=1

        elif drawnActionCard[0]=="marketing":
            player.actionCards[1]+=1

        elif drawnActionCard[0]=="design":
            player.actionCards[2]+=1

        elif drawnActionCard[0]=="technology":
            player.actionCards[3]+=1
        
        discardedActionPile.pop()
        print("You have bought {} action card ".format(drawnActionCard))
        
    def cardDrawn():

            drawnActionCard=currentActionPile.pop()
            print("The drawn Action card is {}".format(drawnActionCard))
            discardedActionPile.append(drawnActionCard)

            print("1.Buy action card")
            print("2.Draw another Action card for 1000$")
            print("3.Pass")

            drawnChoice=1
            while drawnChoice==1:

                drawnChoiceNumber=int(input())

                if drawnChoiceNumber==1:
                    buyingComplete=0

                    while buyingComplete==0:
                        buyActionCard(discardedActionPile[-1])
                        print("Do you want to buy the next top card {}".format(discardedActionPile[-1]))
                        print("0.Yes")
                        print("1.No")
                        buyingComplete=int(input())
                        drawnChoiceNumber=0
                        return 0

                elif drawnChoiceNumber==2:
                    player.money -= 1000
                    cardDrawn()
                    drawnChoiceNumber=0
                    return 0
                
                elif drawnChoiceNumber==3:
                    drawnChoiceNumber=0
                    return 0
    print("Top Opened Action Card:")
    print(discardedActionPile[-1])

    if counter ==1:

        print("1.Draw action card from pile")
        print("2.Buy opened Action card")

        actionCardChoice1=int(input())
    
    else:
        print("Do you want to buy topmost card")
        print("0.Yes")
        print("1.No")
        actionCardChoice2=int(input())

    if actionCardChoice1==1:
        cardDrawn()
        return 0
            
    elif actionCardChoice1==2 or actionCardChoice2==0:

        buyingComplete=0

        while buyingComplete==0 :
            buyActionCard(discardedActionPile[-1])
            print("Do you want to buy the next top card {}".format(discardedActionPile[-1]))
            print("0.Yes")
            print("1.No")
            buyingComplete=int(input())
        return 0

    elif actionCardChoice2==1:
        return 0

    actionCardChoice1=0
    counter+=1
    return 0