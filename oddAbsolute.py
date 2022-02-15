from lib2to3.pytree import NodePattern


def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
    try :
        in_num = int(in_num)
    except :
        print('Error, please enter a number')
        
    if in_num < 21 :
        print(str(abs(in_num-21)))
    else :
        print(str(abs(2 * (in_num-21))))
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateAbsolute()

