# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:37:47 2021

@author: Kumar
"""

import random
number=random.randint(1,10)
for i in range(1,4):
    guess=int(input("Guess a number between 1 to 10 :: "))
    if(guess==number):
        print("You won the game......")
        break
    else:
        if(i==3):
            print("Better luck next time ....:)")
        else:
            print("You have",3-i,"chances remaining....")