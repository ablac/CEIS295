# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/14/2022

import sys

def Continue():
  print()
  answer = input("Continue (Y/n)? " or "y")
  if answer.lower() == "n":
    sys.exit()
  print()