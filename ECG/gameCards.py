# File containing all game cards
from heapq import merge
from itertools import repeat
import random

# Resource Cards

time = []
time.extend(repeat(1,27))
time.extend(repeat(2,22))
time.extend(repeat(4,11))

money = []
money.extend(repeat(500,25))
money.extend(repeat(1000,20))
money.extend(repeat(1500,15))

resourcePile = time +  money


# Actionable Cards 

# General Skills (research and marketing):  7hr*3  +  9hr* 6  +  13hr*4
generalHourCost = [7, 9, 13]            # Hour cost of general skill cards
generalCardQuantity = [3, 6, 4]         # Quantities of general skill cards

researchActionCards = []
researchActionCards.extend(repeat(("Research", generalHourCost[0]), generalCardQuantity[0]))
researchActionCards.extend(repeat(("Research", generalHourCost[1]), generalCardQuantity[1]))
researchActionCards.extend(repeat(("Research", generalHourCost[2]), generalCardQuantity[2]))

marketingActionCards = []
marketingActionCards.extend(repeat(("Marketing", generalHourCost[0]), generalCardQuantity[0]))
marketingActionCards.extend(repeat(("Marketing", generalHourCost[1]), generalCardQuantity[1]))
marketingActionCards.extend(repeat(("Marketing", generalHourCost[2]), generalCardQuantity[2]))


# Specialized Skills (design and technology):   9hr*3  +  11hr* 6  +  15hr*4
specializedHourCost = [9, 11, 15]          # Hour cost of special skill cards
specializedCardQuantity = [3, 6, 4]        # Quantities of special skill cards

technologyActionCards = []
technologyActionCards.extend(repeat(("Technology", specializedHourCost[0]), specializedCardQuantity[0]))
technologyActionCards.extend(repeat(("Technology", specializedHourCost[1]), specializedCardQuantity[1]))
technologyActionCards.extend(repeat(("Technology", specializedHourCost[2]), specializedCardQuantity[2]))

designActionCards = []
designActionCards.extend(repeat(("Design", specializedHourCost[0]), specializedCardQuantity[0]))
designActionCards.extend(repeat(("Design", specializedHourCost[1]), specializedCardQuantity[1]))
designActionCards.extend(repeat(("Design", specializedHourCost[2]), specializedCardQuantity[2]))


actionCardPile = researchActionCards + marketingActionCards + technologyActionCards + designActionCards

# create a random Resources pile and Actionable Cards pile
def addResources(resourcePile):
    resources = resourcePile.copy()
    random.shuffle(resources)
    random.shuffle(resources)
    return resources

currentResourcePile = []
currentResourcePile.extend(addResources(resourcePile))
currentResourcePile.extend(addResources(resourcePile))
currentResourcePile.extend(addResources(resourcePile))

currentActionPile = actionCardPile.copy()
random.shuffle(currentActionPile)
random.shuffle(currentActionPile)
discardedActionPile = []
discardedActionPile.append(currentActionPile.pop())     # Adding 1st card to the discard pile

# Skill Cards costs and benefits

# generalSkillCost = [0, 500, 2000, 4000, 6000]
# generalSkillReduction = [0, 1, 3, 6, 9]

# specialSkillCost = [0, 1500, 3500, 4500, 7000]
# specialSkillReduction = [0, 2, 5, 8, 11]


# Service Cards
serviceCards = ["Research", "Marketing", "Design", "Technology"]

# MVP Cards (r,m,d,t)
MVPCards=[[3,2,3,2],[3,2,2,3],[2,3,3,2],[2,3,2,3],[3,2,3,2],[3,2,2,3],[2,3,3,2],[2,3,2,3]]


# Chance Cards

neutral = "Better luck next time"
chanceCards= {
1: neutral,
2: neutral,
3: neutral,
4: neutral,
5: neutral,
6: neutral,
7: neutral,
8: neutral,
9: "Exchange your personality card with someone",
10: "Exchange your personality card with someone",
11: "The entrepreneur choose another entrepreneur to loose half their resource cards randomly",
12: "The entreprenur can choose any one player and one resource and everytime that entrepreneur spends that resource, the entrepreneur who has played this card will get it for the next 2 rounds",
13: "The entreprenur can choose any one player and one resource and everytime that entrepreneur spends that resource, the entrepreneur who has played this card will get it for the next 2 rounds",
14: "The entreprenur can choose 2 different entrepreneurs to receive no resources for one round.",
15: "The entrepreneur can change any one functional requirement of an MVP card of any entrepreneur including themselves by 1 point.",
16: "The entrepreneur can change any one functional requirement of an MVP card of any entrepreneur including herself by 1 point.",
17: "The entreperneur gets a free service card at random",
18: "The entrepreneur can steal any skill card (Level 4 not allowed) from another entrepreneur.",
19: "The entrepreneur can steal any skill card (Level 4 not allowed) from another entrepreneur.",
20: "Just say NO",
21: "Just say NO",
22: "Just say NO",
23: "An entrepreneur can discard any one actionable card of any other entrepreneur",
24: "An entrepreneur can discard any one actionable card of any other entrepreneur"}

chanceCardKeys = list(chanceCards.keys())
random.shuffle(chanceCardKeys)
random.shuffle(chanceCardKeys)



