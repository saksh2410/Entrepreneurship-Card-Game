import random
def intinput():                     # Function to get integer input
    while 1:
        try:
            userChoice = int(input("Please choose an option:    "))
            break
        except ValueError:
            print("Enter a valid choice")
            continue
    return userChoice


def getChoice():        # function to get users choice of action on their turn
    print("1. Buy Skill Cards")
    print("2. Buy Actionable Cards")
    print("3. View Resources in Hand")
    print("4. View Entire Hand")
    print("5. Chance Cards")
    print("9. End Turn\n")
    print("************************")
    
    userChoice = intinput()

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
                player.money -= generalCost[design]
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
    if research == 4:
        print("Research is maxed at lvl 4")
    else:
        print("1. Research (lvl {}): {}".format(research + 1, generalCost[research]))
    if marketing == 4:
        print("Marketing is maxed at lvl 4")
    else:
        print("2. Marketing (lvl {}): {}".format(marketing + 1, generalCost[marketing]))
    if design == 4:
        print("Design is maxed at lvl 4")
    else:
        print("3. Design (lvl {}): {}".format(design + 1, specialCost[design]))
    if technology == 4:
        print("Marketing is maxed at lvl 4")
    else:
        print("4. Technology (lvl {}): {}".format(technology + 1, specialCost[technology]))
    print("************************")

    print("\n5. View Skill Benefits")
    print("6. Back to Turn Menu")
    boughtSkill = int(input()) - 1  


    if boughtSkill== 0 and research !=4:
        confirmPurchase(0, research)
    elif boughtSkill== 1 and marketing !=4:
        confirmPurchase(1, marketing)
    elif boughtSkill== 2 and design !=4:
        confirmPurchase(2, design)
    elif boughtSkill== 3 and technology !=4:
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


def actionCards(player,currentActionPile,discardedActionPile,drawnCounter):

    def modifiedActionCardCost(currentTopActionCard): #dont know if working

        startingLetter=currentTopActionCard[0][0]
        if startingLetter=='R':
            modifiedCost=currentTopActionCard[1] - player.skillReduction[0]
        elif startingLetter=='M':
            modifiedCost=currentTopActionCard[1] - player.skillReduction[1]
        elif startingLetter=='D':
            modifiedCost=currentTopActionCard[1] - player.skillReduction[2]
        elif startingLetter=='T':
            modifiedCost=currentTopActionCard[1] - player.skillReduction[3]

        
        return modifiedCost

    def buyActionCard(currentTopAcionCard):

        modifiedCostBuy=modifiedActionCardCost(currentTopActionCard)  #this variable tells the price at which player is buying that card
        if player.time>=modifiedCostBuy:
            print("Are you sure you want to buy this action card")
            print("1.Yes       2.No")
            confirmationBuyActionCard=int(input())
            if confirmationBuyActionCard==1:

                player.time-=modifiedCostBuy
                if currentTopActionCard[0]=="Research":
                    player.actionCards[0]+=1

                elif currentTopActionCard[0]=="Marketing":
                    player.actionCards[1]+=1

                elif currentTopActionCard[0]=="Design":
                    player.actionCards[2]+=1

                elif currentTopActionCard[0]=="Technology":
                    player.actionCards[3]+=1

                print("You have bought {}".format(currentTopAcionCard))
                discardedActionPile.pop()
            elif confirmationBuyActionCard==2:
                print("Tansanction Cancelled")
        
        else:
            print("You do not have enough resources to buy this card")
            
   
    def cardDrawn(drawnCounter):
        print("NOTE-The First card is free to draw. Every succesive card costs 1000$\n")
        if drawnCounter==0:
            drawnCard=currentActionPile.pop()
            discardedActionPile.append(drawnCard)
            drawnCounter=1
            print("The Drawn Card is {}\n".format(drawnCard))
        elif drawnCounter>=1:
            if player.money>=1000:
                print("Are you sure you want to draw new action card worth 1000$")
                print("1.Yes          2.No")
                confirmationDrawCard=int(input())
                if confirmationDrawCard==1:
                    player.money-=1000
                    drawnCard=currentActionPile.pop()
                    discardedActionPile.append(drawnCard)
                    drawnCounter+=1
                    print("The Drawn Card is {}\n".format(drawnCard))
                elif confirmationDrawCard==2:
                    print("Transaction Cancelled")
            else:
                print("You dont have enough money to draw another card")
            
        
        return drawnCounter
            
    userRun=1
    
    while userRun==1:
        if len(currentActionPile)==0:  #this code is for reshufffling when current actionpile is over
            print("The action card pile is over and is being reshuffled")
            copyDiscardedActionPile=discardedActionPile.copy()
            currentActionPile=copyDiscardedActionPile[:-1]
            discardedActionPile=[discardedActionPile.pop()]
            random.shuffle(currentActionPile)
            random.shuffle(currentActionPile)
        print("****************************************************************")
        print("You have drawn {} cards in this chance".format(drawnCounter))
        if len(discardedActionPile)==0 :
            print("You cannot purchase action cards before drawing as no action cards left in the pile\n\n")
            print("1.Draw Action Card from deck")
            print("2.Pass\n")
            

        elif len(discardedActionPile)>0:
            currentTopActionCard=discardedActionPile[-1]
            print("\n\nTop opened Action card is :   {}".format(currentTopActionCard))
            modifiedCost=modifiedActionCardCost(currentTopActionCard)
            print("The modified cost for this action card is ** {} hours **\n\n".format(modifiedCost))

            print("1.Draw Action Card from deck")
            print("2.Pass")
            print("3.Buy top Opened Action Card")

        playerFirstChoice=int(input()) #have to make a check that user doesnt enter 3 even if first menu is showed
        print("\n")
                
        
        if playerFirstChoice==1 :
            drawnCounter=cardDrawn(drawnCounter)

        elif playerFirstChoice==2 :
            userRun=0
        
        elif playerFirstChoice==3 :
            buyActionCard(currentTopActionCard)
        
        else:
            print("Invalid Number please try again")
            

      
    return drawnCounter


def checkWin(player):          # Function to check if the player has met the objectives required for winning
    if player.actionCards == player.MVP:
        return True
    else:
        return False

def chanceCard(player, chanceCards, keys):
    def buyChanceCards(player, chanceCards, keys):
        if len(keys) !=0 :
            if player.money >= 2000:
                print("Are you sure you want to buy a chance card for $2000")
                print("1. YES       2. NO")
                confirmation = intinput()
                if confirmation == 1:
                    key = keys.pop()
                    player.chanceKeys.append(key)
                    print(chanceCards[key])
                else:
                    chanceCards(player, chanceCards, keys)
            else:
                print("insufficient funds")
                return
        else:
            print("The chance card pile is exhausted")
    
    def viewChanceCards(player):
        print("Your chance cards are:")
        player.printChance()

    print("1. Buy a chance Card")
    print("2. View / Play your chance cards")
    print("3. Go Back\n")

    userChoice = intinput()

    if userChoice == 1:
        buyChanceCards(player, chanceCards, keys)
    if userChoice == 2:
        viewChanceCards(player)
