##Leap Year checker

def leapcheck(year):
        if year > 0 and year <= 9999:
            if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
                print('The year', year, 'is a leap year')
            else:
                print('The year', year, 'is not a leap year.')        
        else:
            print('The year you entered is outside of the range 1-9999')
        

print    ("      Cliff's Leap Year Checker        ")
while True:
    print('---------------------------------------')
    print('Please enter year in this format - YYYY')
    try:
        yearentered = int(input())
        leapcheck(yearentered)
    except ValueError:
        print("That's not an integer and you're screwing up my program") 
