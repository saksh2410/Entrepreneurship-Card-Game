from dis import dis
from statistics import median


def getChoice():        # function to get users choice of action on their turn
    print("1. Buy Skill Cards")
    print("2. Buy Actionable Cards")
    print("3. View Resources in Hand")
    print("4. View Entire Hand")
    print("5. More Options")
    print("9. End Turn\n")
    print("************************")
    userChoice = int(input())

    if userChoice == 1 or userChoice == 2 or userChoice == 3 or userChoice == 9 or userChoice == 4 or userChoice == 5:
        return userChoice
    else:
        print("Please enter a valid choice")
        getChoice()

def skillCards(player):       # Function for user to trigger Skill Cards
    

    # defining cost and benefit of different skill levels
    generalCost = [500, 2000, 4000, 6000]
    specialCost = [1500, 3500,  4500, 7000]
    generalReduction = [0, 1, 3, 6, 9]
    specialReduction = [0, 2, 5, 8, 11]

    # unpacking level of expertise in each area
    research = player.skillLevel[0]
    marketing = player.skillLevel[1]
    design = player.skillLevel[2]
    technology = player.skillLevel[3]


    def addSkill(skill):        # function to add the skill level to player object
        
        if skill == 0:
            if generalCost[research] <= player.money:
                player.skillLevel[0] += 1
                player.skillReduction[0] = generalReduction[research + 1]
                print("\nCongrats, you upskilled RESEARCH to lvl {}".format(player.skillLevel[0]))
                print("You now get {}hrs off on RESEARCH actionable cards\n".format(player.skillReduction[0]))
                player.money -= generalCost[research]
                player.printMoney()
                player.printSkillReduction()
            else:
                print("\nNot enough money to upskill\n")
        elif skill== 1:
            if generalCost[marketing] <= player.money:
                player.skillLevel[1] += 1
                player.skillReduction[1] = generalReduction[marketing + 1]
                print("\nCongrats, you upskilled MARKETING to lvl {}".format(player.skillLevel[1]))
                print("You now get {}hrs off on MARKETING actionable cards\n".format(player.skillReduction[1]))
                player.money -= generalCost[marketing]
                player.printMoney()
                player.printSkillReduction()
            else:
                print("\nNot enough money to upskill\n")
        elif skill== 2:
            if specialCost[design] <= player.money:
                player.skillLevel[2] += 1
                player.skillReduction[2] = specialReduction[design + 1]
                print("\nCongrats, you upskilled DESIGN to lvl {}".format(player.skillLevel[2]))
                print("You now get {}hrs off on DESIGN actionable cards\n".format(player.skillReduction[2]))
                player.money -= specialCost[design]
                player.printMoney()
                player.printSkillReduction()
            else:
                print("\nNot enough money to upskill\n")
        elif skill== 3:
            if specialCost[technology] <= player.money:
                player.skillLevel[3] += 1
                player.skillReduction[3] = specialReduction[technology + 1]
                print("\nCongrats, you upskilled TECHNOLOGY to lvl {}\n".format(player.skillLevel[3]))
                print("You now get {}hrs off on TECHNOLOGY actionable cards\n".format(player.skillReduction[3]))
                player.money -= specialCost[technology] 
                player.printMoney()
                player.printSkillReduction()
            else:
                print("\nNot enough money to upskill\n")

    def confirmPurchase(skill, level):          # Function to confirm the purchase of a skill
        skillList = ["RESEARCH", "MARKETING", "DESIGN", "TECHNOLOGY"]
        print("\nAre you sure you want to purchase {} lvl {}".format(skillList[skill], level + 1))
        print("1. YES       2. NO")
        choice= int(input())

        if choice == 1:
            addSkill(skill)
        elif choice == 2:
            print("\n")
            skillCards(player)
        else:
            print("INVALID CHOICE")
            print("\n")
            skillCards(player)

    # displaying user current skill level and money

    player.printSkillLevel()
    player.printMoney()
    print("\n")

    # asking user which skill if any they want to upgrade
    print("************************")
    print("The Cost of Buying next level skill is:")
    print("1. Research (lvl {}): {}".format(research + 1, generalCost[research]))
    print("2. Marketing (lvl {}): {}".format(marketing + 1, generalCost[marketing]))
    print("3. Design (lvl {}): {}".format(design + 1, specialCost[design]))
    print("4. Technology (lvl {}): {}".format(technology + 1, specialCost[technology]))
    print("************************")
    print("\n5. View Skill Benefits")
    print("6. Back to Turn Menu")
    boughtSkill = int(input()) - 1  


    if boughtSkill== 0:
        confirmPurchase(0, research)
    elif boughtSkill== 1:
        confirmPurchase(1, marketing)
    elif boughtSkill== 2:
        confirmPurchase(2, design)
    elif boughtSkill== 3:
        confirmPurchase(3, technology)
    elif boughtSkill== 4:
        print("\nDiscount (in hrs) based on skill level is:   ")
        print("General Skill (Research and Marketing):  {}".format(generalReduction))
        print("Special Skill (Design and Technology):   {}\n\n".format(specialReduction))
    elif boughtSkill== 5:
        print("\n")
        return
    else:
        print("INVALID CHOICE\n")
        return



    return 0

def actionCard(player,currentActionPile,discardedActionPile,drawnCounter):      # Function to trigger action cards
    
    def modifiedActionCardCost(topCard):        # Function to return modified cost due to player skill

        startingLetter=topCard[0][0]
        if startingLetter=='R':
            modifiedCost=topCard[1] - player.skillReduction[0]
        elif startingLetter=='M':
            modifiedCost=topCard[1] - player.skillReduction[1]
        elif startingLetter=='D':
            modifiedCost=topCard[1] - player.skillReduction[2]
        elif startingLetter=='T':
            modifiedCost=topCard[1] - player.skillReduction[3]

        print("The modified cost for this action card is * {} hours *".format(modifiedCost))
        return modifiedCost

    def buyActionCard(topCard):

        modifiedCost=modifiedActionCardCost(topCard)  #this variable tells the price at which player is buying that card
        if player.time>=modifiedCost:
            player.time-=modifiedCost
            if topCard[0]=="Research":
                player.actionCards[0]+=1

            elif topCard[0]=="Marketing":
                player.actionCards[1]+=1

            elif topCard[0]=="Design":
                player.actionCards[2]+=1

            elif topCard[0]=="Technology":
                player.actionCards[3]+=1

            print("You have bought {}".format(topCard))
            discardedActionPile.pop()
        
        else:
            print("You do not have eenough resources to buy this card")
            
   
    def cardDrawn(drawnCounter):
        print("NOTE-The First card is free to draw. Every succesive card costs 1000$")
        if drawnCounter==0:
            drawnCard=currentActionPile.pop()
            discardedActionPile.append(drawnCard)
            drawnCounter=1
        elif drawnCounter>=1:
            if player.money>=1000:
                player.money-=1000
                drawnCard=currentActionPile.pop()
                discardedActionPile.append(drawnCard)
                drawnCounter+=1
            else:
                print("You dont have enough money to draw another card")
        return drawnCounter
            
    userRun=1       # Variable to hold whether the user is in action card menue or not
    
    while userRun==1:
        topCard=discardedActionPile[-1]
        print("\n\nTop opened Action card is :   {}".format(topCard))
        print("You have drawn {} cards in this chance".format(drawnCounter))
        modifiedActionCardCost(topCard)
        print("\n")
        
        print("1.Buy top Action Card")
        print("2.Draw Action Card from deck")
        print("3.Pass\n")
        

        playerFirstChoice=int(input())
        print("\n")

        if playerFirstChoice==1:
            buyActionCard(topCard)
        
        elif playerFirstChoice==2:
            drawnCounter=cardDrawn(drawnCounter)

        elif playerFirstChoice==3:
                userRun=0
            

    return 0


def checkWin(player):          # Function to check if the player has met the objectives required for winning

    if player.actionCards == player.MVP:
        return True
    else:
        return False

def moreOptions():

    print("1. View your skill discounts")
    print("2. View your MVP requirements")
