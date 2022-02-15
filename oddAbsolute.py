from lib2to3.pytree import NodePattern


def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
    try :
        in_num = int(in_num)
    except :
        print('Nope')
        
    if in_num < 21 :
        in_num = abs(21 - in_num)
        print(in_num)
    else :
        in_num = abs(in_num - 21)
        in_num = in_num * 2
        print(in_num)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateAbsolute()

