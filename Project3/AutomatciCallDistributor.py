# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/8/2022

from Functions.Queue import Queue
from Functions.Call import Call
from datetime import date
import time     # Used to pause the application
import random   # Used to generate random number

name = "Keith V Swoger"           # Authors Name
CSVFile = 'Data/P3_Calls.csv'     # Client Data.csv
call_number = 0                   # Number of calls waiting
sleeptime = 2                     # Time for the application to sleep
seconds = 20                      # Number of times to run the simulation
dashes = 45                       # Number of - to display between simulated calls
rand = 4                          # Number to set to generate random numbers to Higher number = Higher Queue

# Create lists
calls = []

print ()
print ("Name:", name)
print ("Date :", date.today())

with open (CSVFile) as infile:
  for line in infile:
    # Splie the line based on commas
    s = line.split(',')
    client_id = int(s[0])
    client_name = s[1]
    client_phone = s[2]

    # create call object based on data from line
    a_call = Call(client_id, client_name, client_phone)

    # Add Call object to list
    calls.append(a_call)

# Queue object for our calls
calls_waiting = Queue()

# User settings input prompts.
sleeptime = int(input(f"How long between simulated seconds? (Default {sleeptime}) ") or f"{sleeptime}")
seconds = int(input(f"How many seconds do you want to simulate? (Default {seconds}) ") or f"{seconds}")
answer = int(input(f"Random number max, higher = larger queue (Default {rand}) ") or f"{rand}")
if answer < 3:
  print (f"Must be greater then 3 defaulting to {rand}")
else:
  rand = answer

print(f"Running simulation {seconds} times with spacing of {sleeptime} seconds and a random number maxing out at {rand}")
print ("-" * dashes)

# Run the simulation for the given number of times
for i in range(seconds):
  print ("-" * dashes)
  # Pause the application for time designated
  time.sleep(sleeptime) 
  random_event = random.randint(1,rand)
  
  # Nothing happens when Rand = 3
  if random_event == 1:
    print("Nothing happened during this time.")
    print ("\t Number of calls waiting in queue", calls_waiting.get_length())
    
  # Send next caller in Queue to a service rep 
  elif random_event == 2:
    print ("Call sent to representative for service")
    if calls_waiting.get_length() > 0:
      print("Caller information: ")
      print(calls_waiting.dequeue())
    else:
      print ("The call waiting queue is empty.")
    print ("\t Number of calls waiting in queue", calls_waiting.get_length())
  
  # Add Random Caller to Queue
  else:
    print("Call Received. Caller added to queue.")
    calls_waiting.enqueue ( calls[call_number] )
    # Setup the next call
    call_number =+ 1
    print ("\tNumber of calls waiting in Queue", calls_waiting.get_length())

print("\n The Automatic Call Distributor simulation has completed.")
    