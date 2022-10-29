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
name = "Keith V Swoger"
CSVFile = 'ClientData.csv'

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

# Scenario 1: Printer Queue, Call Queue, or Service Queue (line)
section_title = "-Scenario: Printer Queue-"
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