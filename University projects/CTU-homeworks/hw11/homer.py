"""
Homer's fridge
Course: B0B36ZAL
"""


class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration

def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
# openFridge(fridge)


"""
Task #1
"""
def maxExpirationDay(fridge):
    max = 0
    for food in fridge:
        if food.expiration > max:
            max = food.expiration
    return max

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(maxExpirationDay(fridge))
# The command should print 4


"""
Task #2
"""
def histogramOfExpirations(fridge):
    hg = []
    date = 0
    for i in range (maxExpirationDay(fridge) + 1):
        count = 0
        for food in fridge:
            if food.expiration == date:
                count += 1
        hg.append(count)
        date += 1
    return hg


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(histogramOfExpirations(fridge))
# The command should print [0, 2, 0, 1, 1]


"""
Task #3
"""
def cumulativeSum(histogram):
    cumsum = []
    s = 0
    for x in range(len(histogram)):
        s = s + histogram[x]
        cumsum.append(s)
    return cumsum

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(cumulativeSum([0, 2, 0, 1, 1]))
# The command should print [0, 2, 2, 3, 4]


"""
Task #4
"""
def sortFoodInFridge(fridge):
    a = cumulativeSum(histogramOfExpirations(fridge)).copy()
    fr = fridge.copy()
    for food in fridge:
        i = food.expiration
        a[i] = a[i] - 1
        fr[a[i]] = food
    return fr


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #5
"""
def reverseFridge(fridge):
    vystup = []
    fr = fridge.copy()
    for food in fridge:
        x = fr.pop()
        vystup.append(x)
    return vystup
        

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(reverseFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #6
"""
def eatFood(name, fridge):
    minexpdate = 500
    x = None
    fr = fridge.copy()
    for food in fridge:
        if name == food.name and minexpdate > food.expiration:
            x = food
            minexpdate = food.expiration
    if minexpdate != 500:
        fr.remove(x)
    return fr


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(
#     eatFood("donut",
#         [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#         Food("donut", 3), Food("donut", 1), Food("donut", 6)]
#     ))
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)
