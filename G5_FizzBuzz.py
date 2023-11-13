import time
i = 1

def checkFizzBuzz(x, i):    
    if (i % 15 == 0):
        if (x == "Fizz Buzz"):
            return True
        else:
            return False
    elif (i % 5 == 0): 
        if (x == "Buzz"):
            return True
        else:
            return False
    elif (i % 3 == 0): 
        if (x == "Fizz"):
            return True
        else:
            return False
    elif (i == int(x)):
        return True
    else: return False

while(True):
    start =time.time()
    x = input("Next: ")
    if (time.time() - start > 5):
        print("Too slow!")
        break
    if not checkFizzBuzz(x,i):
        print("Wrong answer idot!")
        break
    i+=1
