import random

def d6():
    result = random.randint(1,6)
    if result == 6:
        result = 6 + random.randint(1,6)
    print("The result is: " + str(result))
