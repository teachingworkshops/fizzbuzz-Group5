import time
i = 1

def checkFizzBuzz(x, i): 
    try:
        x = int(x)
        if (x < 1 or i < 1):
            return False 
        
        if (i == x):
            return True
        else: return False
    except (ValueError): 
        if (i % 15 == 0):
            if (x.lower() == "fizz buzz" or x.lower() == "fizzbuzz"):
                return True
            else:
                return False
        elif (i % 5 == 0): 
            if (x.lower() == "buzz"):
                return True
            else:
                return False
        elif (i % 3 == 0): 
            if (x.lower() == "fizz"):
                return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
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
