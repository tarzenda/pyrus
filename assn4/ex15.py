import random

def d6(may_explode):
    result = random.randint(1,6)
    if may_explode == True:
        result = 6 + random.randint(1,6)
        print("The result is: " + str(result))
