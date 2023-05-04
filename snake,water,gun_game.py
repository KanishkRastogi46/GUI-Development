# a program for both snake, water, gun & rock, paper, scissor #

import random

def player(a,b):
    if a=='s' and b=='w':
        win= a
    elif a=='s' and b=='g':
        win= b
    elif a=='w' and b=='g':
        win= a
    elif a=='w' and b=='s':
        win= b
    elif a=='g' and b=='s':
        win= a
    elif a=='g' and b=='w':
        win= b
    elif a==b:
        win= None
    

    if win==a:
        champion= "Computer"
    elif win==None:
        champion= "Tied"
    else:
        champion= "You"

    return champion



print("computer's turn first it will chose any random option")
rand_opt = random.randint(1,3)
if rand_opt==1:
    comp= 's'
elif rand_opt==2:
    comp= 'w'
else:
    comp= 'g'

you = input("Your turn select from Snake(s),Water(w),Gun(g):")
print("Computer chose:",comp)

winner = player(comp, you)
if winner=='Computer' or winner=='You':
    print("WINNER:", winner)
else:
    print("Match tied")