from lib2to3.pytree import NodePattern


def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
     
    if in_num < 21 :
        in_num = str(abs(in_num-21))
        print(in_num)
    else :
        in_num = str(abs(2 * (in_num-21)))
        print(in_num)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateAbsolute()

