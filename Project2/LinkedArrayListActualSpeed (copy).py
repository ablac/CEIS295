# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  10/29/2022

from Project1.ArrayList import ArrayList
from Project1.Client import Client
from Project1.Quicksort import Quicksort
from datetime import date
import time     # Used to time code executions
import random   # Used to generate random numbers
import sys      # Used to Terminate application early

# Variables
name = "Keith V Swoger" # Authors Name
CSVFile = 'Project1/ClientData.csv' # Client Data.csv
smallest_id = 100001 # Client ID Starting Point
Records_Display = 1000 # How many records to display in random search
Records_Add = 1000 # How many records to add
Records_Remove = 1000 # How many records to remove
sort = True # Sort The Records?
print_records = True # Set to true to display all record updates, False to just display times.

NE2 = "n" # Letter to not continue, or to set settings to false anything else will continue.
S1 = "-Scenario: Printer Queue or Call Queue or Service Queue-" # Scenario 1 Name
S2 = "-Scenario: Customer Service Center-" # Scenario 2 Name
S3 = "-Scenario: Call Center-" # Scenario 3 Name

# Settings for the Scenarios
answer = input("Sort Records (Default True) (Y/n)? ") # Sort the results?
if answer.lower() == NE2:
  sort = False

answer = input("Display Records (Default True) (Y/n)? ") # Display the Records?
if answer.lower() == NE2:
  print_records = False

Records_Display= int(input("Number to Display (Default 1000)? ") or "1000") # How many to display?

Records_Add = int(input("Number to Add (Default 1000)? ") or "1000") # How many to Add?

Records_Remove = int(input("Number to Remove (Default 1000)? ") or "1000") # How many to remove?

# Display Program Information
print ()
print ("Name:", name)
print ("Date :", date.today())
print ("Display Records:", print_records)
print ("Sorted:", sort)
print ("Records to Add:", Records_Add)
print ("Records to Remove:", Records_Remove)
print ("Records to Display", Records_Display)

clients = []
def Continue():
  answer = input("Continue (Y/n)? " or "y")
  if answer.lower() == NE2:
    sys.exit()

Continue()
# Read records from Clientdata.csv
with open(CSVFile) as infile:
  for line in infile:
    # Split the line based on the commas
    s = line.split(',')
    client_id = int(s[0]) # Convert to Int from String
    f_name = s[1]
    l_name = s[2]
    phone = s[3]
    email = s[4]

    # Create Client object
    clt = Client(client_id, f_name, l_name, phone, email)
    # Add the client object to list
    clients.append(clt)

# Sort the clients list
if sort == True:
  Quicksort.sort(clients)
  
# How many client objects?
num_records = len(clients)

# create an arraylist object
my_array_list = ArrayList()

# Scenario 1: Scenario: Printer Queue or Call Queue or Service Queue
print ("-" * len(S1))
print(S1)
print ("-" * len(S1))

#how long does it take to add client records?
start_time = time.time()

for i in range(num_records):
  my_array_list.append(clients[i])

end_time = time.time()
total_time = end_time - start_time
print ("Seconds to add all", str(num_records),"records from file: {:.6f}".format(total_time))

#How long does it take to remove records from the front of the Array List
start_time = time.time()

for i in range(num_records):
  my_array_list.remove_at(0)

end_time = time.time()
total_time = end_time - start_time
print ("Seconds to remove all records from front: {:.6f}".format(total_time))

Continue()

#Scenario 2: Customer Service Center
print ("-" * len(S2))
print(S2)
print ("-" * len(S2))

for i in range(num_records):
  my_array_list.append(clients[i])

#how long does it take to randomly display records?
start_time = time.time()

for i in range(Records_Display):
  largest_id = smallest_id + num_records
  ran_number = random.randint(smallest_id, largest_id)
  if print_records == True:
    if sort == True:
      print ( my_array_list.search_sorted(Client(ran_number)))
    else:
      print ( my_array_list.search(Client(ran_number)))
  else:
     if sort == True:
       my_array_list.search_sorted(Client(ran_number))
     else:
       my_array_list.search(Client(ran_number))
end_time = time.time()
total_time = end_time - start_time
print ("Seconds to pick", str(Records_Display),"random records: {:.6f}".format(total_time))

Continue()
  
#Scenario 3: Call Center
print ("-" * len(S3))
print(S3)
print ("-" * len(S3))

#how long does it take to add records randomly, and randomly display and remove records?
start_time = time.time()
current_id = smallest_id + num_records + 1

for i in range(Records_Add):
  my_array_list.append(Client(current_id))
  current_id += 1
num_records = len(clients)

for i in range(Records_Display):
  largest_id = smallest_id + num_records
  ran_number = random.randint(smallest_id, largest_id)
  if print_records == True:
    if sort == True:
      print ( my_array_list.search_sorted(Client(ran_number)))
    else:
      print ( my_array_list.search(Client(ran_number)))

for i in range(Records_Remove):
  largest_id = smallest_id + num_records
  random_num = random.randint(smallest_id, largest_id)
  if print_records == True:
    if sort == True:
      print ( my_array_list.search_sorted(Client(ran_number)))
    else:
      print ( my_array_list.search(Client(ran_number)))

end_time = time.time()
total_time = end_time - start_time
print ("Seconds to add", str(Records_Add),"records, Display", str(Records_Display),"records, and Remove",str(Records_Remove),"Records: {:.6f}".format(total_time))