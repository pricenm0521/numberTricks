# numberTricks.py
# adapted from https://www.thoughtco.com/math-tricks-that-will-blow-your-mind-4154742

import random
def test():
    print("Hello from test")
    

def trick02(number = None):
    '''
    Think of a number.
    Multiply it by 3.
    Add 6.
    Divide this number by 3.
    Subtract the number from Step 1 from the answer in Step 4.
    The answer is 2.
    '''
    if number == None:
        number = random.randint(12345,54321)
    step1 = number
    number = step1 * 3
    number = number + 6
    number = number // 3
    number = number - step1
    print("Started with", step1, "ended with", number)

def trick03():
    '''
    Think of any three-digit number in which each of the digits is the same. Examples include 333, 666, 777, and 999.
    Add up the digits.
    Divide the three-digit number by the answer in Step 2.
    The answer is 37.
    '''
    
    number = 777
    digit1 = str(number)[0] # first digit of the number
    digit2 = str(number)[1] # second digit of the number
    digit3 = str(number)[2] # third digit of the number
    temp = int(digit1) + int(digit2) + int(digit3)
    final = number // temp
    print("Started with", number, "ended with", final)
    

    