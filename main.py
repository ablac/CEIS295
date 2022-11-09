# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/8/2022

import os

def start():
  # User Menu
  print ("Insert 1 for ArrayListActualSpeed (Project 1)")
  print ("Insert 2 for LinkedArrayListActualSpeed (Project 2)")
  print ("Insert 3 for AutomatciCallDistributor (Project 3)")
  print ("Insert T for TimeProcess")
  print ("Insert M for MainForStack")
  print ("Insert C to clear console")
  print ("Insert E to exit")
  
  # Request Input
  select = input("Select Process: ")
  
  # Convert to uppercase
  select = select.upper()
  
  # Project Programs
  if select == "1":
    os.system('clear')
    import Project1.ArrayListActualSpeed
  elif select == "2":
    os.system('clear') 
    import Project2.LinkedArrayListActualSpeed
  elif select == "3":
    os.system('clear')
    import Project3.AutomatciCallDistributor

  # Extra Programs
  elif select == "T":
    os.system('clear') 
    import Extra.TimeProcess
  elif select == "M":
    os.system('clear') 
    import Extra.MainForStack
    
  # Clear Console.
  elif select == "C":
    os.system('clear')  
    start()
    
  # Exit Code
  elif select == "E":
    quit
    
  # Invalid Entry  
  else:
    print("Invalid Entry")
    start()

# Run Program. 
if __name__ == "__main__":
  start()
    
  