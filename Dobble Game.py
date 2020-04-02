# -*- coding: utf-8 -*-
"""
This is the code for Dobble game implemented through Python.This game is generalised for one player only.
Rules:-
In this game you will get a score of +1 for each correct answer and a score of -1 for each incorrect answer.

Don't exceed the number of symbols beyond 25 as it can result in error.You can use error handling to prevent that too.
@author: Kapil Bansal
"""

import string
import random
player_name=input("Enter Your Name\n")
n=int(input("Enter the number of symbols you want"))
score=0 #Current score of the player
symbols=[]
card1=[0]*n #It will act as the first card of symbols
card2=[0]*n #It will act as the other card of symbols
while(1):
    symbols=list(string.ascii_letters) #Our main list of symbols
    pos1=random.randint(0,n-1) #Position of common symbol in card1
    pos2=random.randint(0,n-1) #Position of common symbol in card2
    same=random.choice(symbols) #It will be the symbol common in both cards
    symbols.remove(same)
    #Entering common symbol in both cards
    if(pos1==pos2):
        card1[pos1]=same
        card2[pos1]=same
    else:
        card1[pos1]=same
        card1[pos2]=random.choice(symbols)
        #As we add a symbol in card it is removed from the original list of symbols to prevent duplicacy.
        symbols.remove(card1[pos2])
        card2[pos2]=same
        card2[pos1]=random.choice(symbols)
        symbols.remove(card2[pos1])
    #Adding remaining symbols in the cards
    for i in range(n):
        if(i!=pos1 and i!=pos2):
            alpha1=random.choice(symbols)
            symbols.remove(alpha1)
            alpha2=random.choice(symbols)
            symbols.remove(alpha2)
            card1[i]=alpha1
            card2[i]=alpha2
    print(card1,"\n",card2)
    t=input("SPOT THE SIMILARITY ")
    if t==same:
        print("You Guessed it right")
        score=score+1
    else:
        print("Better luck next time")
        score=score-1
    print("Your current score is",score)
    c=input("Want to continue the game?? Press 1 for Yes\n")
    if c!='1':
        print("Thanks ",player_name," for playing")
        print("Your Scores are",score)
        break
