from random import *

def is_valid(ch):
    return ch.isdigit() and 0 <= int(ch) <= 100

def chek(c, ch, cu):
    if cu:
        if int(c) > ch:
            print('Wrong! Your number is too large')
        elif int(c) >= 0:
            print('Wrong! Your number is too small')
        else:
            print('Wrong! You entered an incorrect value')
    
ch = randint(0, 100)
cu = 0
c = -1
print('Welcome to "Guessing Game"')
print('you need to guess the number 0 to 100')
print('after each attempt to guess the program')
print('your number will speak more or less')
print('Good luck!')
while(int(c) != ch):
    chek(c, ch, cu)
    cu += 1
    print('Attempt №'+ str(cu) +'. Enter the number:')
    c = input()
    if is_valid(c) == False:
        c = -1
print('Hooray! You guessed the number with '+ str(cu) + ' attempts!') 
print('And if you knew binary search, you would guess with 7 attempts!') 