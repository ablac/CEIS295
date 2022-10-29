# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  10/29/2022

from ArrayList import ArrayList
from Client import Client
from Quicksort import Quicksort
from datetime import date

import time     # Used to time code executions
import random   # Used to generate random numbers
import sys      # Used to Terminate application early

# Variables
name = "Keith V Swoger" # Authors Name
CSVFile = 'ClientData.csv' # Client Data.csv
smallest_id = 100001 # Client ID Starting Point
Records_Display = 1000 # How many records to display in random search
Records_Add = 1000 # How many records to add
Records_Remove = 1000 # How many records to remove

# Display Name and Date in output

print ("Name:", name)
print ("Date :", date.today)

clients = []

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

# How many client objects?
num_records = len(clients)

# create an arraylist object
my_array_list = ArrayList()

# Scenario 1: Scenario: Printer Queue or Call Queue or Service Queue
section_title = "-Scenario: Printer Queue or Call Queue or Service Queue-"
print ("-" * len(section_title))
print(section_title)
print ("-" * len(section_title))

#how long does it take to add client records?
start_time = time.time()

for i in range(num_records):
  my_array_list.append(clients[i])

end_time = time.time()
total_time = end_time - start_time
print ("Seconds to add", str(num_records),"records: {:.6f}".format(total_time))

#How long does it take to remove records from the front of the Array List
start_time = time.time()

for i in range(num_records):
  my_array_list.remove_at(0)

end_time = time.time()
total_time = end_time - start_time
print ("Seconds to remove records from front: {:.6f}".format(total_time))

answer = input("Continue (y/n)? ")
if answer.lower() != "y":
  sys.exit()

#Scenario 2: Customer Service Center
section_title = "-Scenario: Customer Service Center-"
print ("-" * len(section_title))
print(section_title)
print ("-" * len(section_title))

for i in range(num_records):
  my_array_list.append(clients[i])

#how long does it take to randomly display records?
start_time = time.time()

for i in range(Records_Display):
  largest_id = smallest_id + num_records
  ran_number = random.randint(smallest_id, largest_id)
  print ( my_array_list.search(Client(ran_number)))

end_time = time.time()
total_time = end_time - start_time
print ("Seconds to pick", str(Records_Display),"random records: {:.6f}".format(total_time))

answer = input("Continue (y/n)? ")
if answer.lower() != "y":
  sys.exit()
  
#Scenario 3: Call Center
section_title = "Scenario: Call Center"
print ("-" * len(section_title))
print(section_title)
print ("-" * len(section_title))

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
  print ( my_array_list.search(Client(ran_number)))

for i in range(Records_Remove):
  largest_id = smallest_id + num_records
  random_num = random.randint(smallest_id, largest_id)
  print ( my_array_list.search(Client(ran_number)))

end_time = time.time()
total_time = end_time - start_time
print ("Seconds to add", str(Records_Add),"records, Display", str(Records_Display),"records, and Remove",str(Records_Remove),"Records: {:.6f}".format(total_time))