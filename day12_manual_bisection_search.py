#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 13:04:21 2022

@author: ken
"""

import random

answer = random.choice(range(1, 100))
#test print
print(answer)

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
    
def inner():
    if mode == 'easy':
        attempts = 10
    else:
        attempts = 5
    
    while attempts > 0:
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess == answer:
            print("That's correct!")
            return
        elif guess > answer:
            print("Too high.")
            print("Guess again.")
            print("You have", attempts, "attempts remaining to guess the number.")
        else:
            print("Too low.")
            print("Guess again.")
            print("You have", attempts, "attempts remaining to guess the number.")
while inner():
    pass
