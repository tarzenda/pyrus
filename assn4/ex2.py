def intro():
    print ("This program is made to compare numbers.")
    x = input("what is x? ")
    y = input("what is y? ")
    compare(x,y)

def compare(x,y):
    if x<y:
        print (x, "is less than", y)
    elif x>y:
        print (x, "is greater than", y)
    else:
        print (x, "and", y, "are equal")
