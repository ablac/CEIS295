# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  10/29/2022

import os

def start():
  # User Menu
  print ("Insert 1 for TimeProcess")
  print ("Insert 2 for ArrayListActualSpeed")
  print ("Insert 3 for LinkedArrayListActualSpeed")
  print ("Insert C to clear console")
  print ("Insert E to exit")
  
  # Request Input
  select = input("Select Process: ")
  
  # Convert to uppercase
  select = select.upper()
  
  # Run Selected Process
  if select == "1":
    import TimeProcess.TimeProcess
  elif select == "2":
    import Project1.ArrayListActualSpeed
  elif select == "3":
    import Project2.LinkedArrayListActualSpeed

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
    
  