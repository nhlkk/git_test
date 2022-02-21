#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:30:15 2022

@author: ken
"""

bids = {}

def stage1():
    name = input("What is your name?: ")    
    bid = input("What is your bid?: $")
    bids[name] = bid
    
    # adding feedback
    print(f"{name} placed a bid of ${bid}.")
        
    x = input("Are there any other bidders? Type 'yes' or 'no'.: ")
    
    if x == 'yes':
        stage1()  
    elif x == 'no':
        winner = max(bids, key=bids.get)
        print(f"The winner is {winner} with a bid of ${bids[winner]}.")
    else:
        print("Invalid input. Try again.")
        stage1()
stage1()