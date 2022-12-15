z# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/1/2022

from Functions.Lists import LinkedList
from Functions.Client import Client
from datetime import date
from Functions.Default import Continue, TTime, Title
import time, random, os

def main():
  os.system('clear')
  # Variables
  name = "Keith V Swoger" # Authors Name
  CSVFile = 'Data/P2_Clients.csv' # Client Data.csv
  smallest_id = 100001 # Client ID Starting Point
  Records_Display = 1000 # How many records to display in random search
  Records_Add = 1000 # How many records to add
  Records_Remove = 1000 # How many records to remove
  print_records = True # Set to true to display all record updates, False to just display times.

  S1 = "-Scenario: Printer Queue or Call Queue or Service Queue-" # Scenario 1 Name
  S2 = "-Scenario: Customer Service Center-" # Scenario 2 Name
  S3 = "-Scenario: Call Center-" # Scenario 3 Name
  os.system('clear')
  #----------------------------
  #-------------MENU-----------
  #----------------------------
  # Settings for the Scenarios
  
  answer = input("Display Records (Default True) (Y/n)? ") # Display the Records?
  if answer.lower() == "N":
    print_records = False
  os.system('clear')
  
  Records_Display= int(input(f"Number to Display (Default {Records_Display})? ") or f"{Records_Display}") # How many to display?
  os.system('clear')
  
  Records_Add = int(input(f"Number to Add (Default {Records_Add})? ") or f"{Records_Add}") # How many to Add?
  os.system('clear')
  
  Records_Remove = int(input(f"Number to Remove (Default {Records_Remove})? ") or f"{Records_Remove}") # How many to remove?
  os.system('clear')
  
  # Display Program Information
  print ()
  print ("Name:", name)
  print ("Date :", date.today())
  print ("Display Records:", print_records)
  print ("Records to Add:", Records_Add)
  print ("Records to Remove:", Records_Remove)
  print ("Records to Display", Records_Display)
  #----------------------------
  #--------PROGRAM START-------
  #----------------------------
  # Ask user if they would like to continue, or stop.
  
  def Add_List():
    for i in range(num_records):
      my_linked_list.add_last(clients[i])
    
  clients = []
  
  Continue() ########################################## END SETTINGS MENU
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
  
  # create an Linkedlist object
  my_linked_list = LinkedList()
  
  # Scenario 1: Scenario: Printer Queue or Call Queue or Service Queue
  Title(S1)
  
  # how long does it take to add client records?
  start_time = time.time()
  
  Add_List()
  
  end_time = time.time()
  print (f"Seconds to add all {num_records},records from file: {TTime(start_time, end_time)}")
  
  # How long does it take to remove records from the front of the Linked List
  start_time = time.time()
  
  for i in range(num_records):
    my_linked_list.remove_first()
  
  end_time = time.time()
  print (f"Seconds to remove all records from front: {TTime(start_time, end_time)}")
  
  Continue() ########################################## END SCENARIO 1
  
  # Scenario 2: Customer Service Center
  Title(S2)
  
  # Add clinets to linked List
  Add_List()
  
  # how long does it take to randomly display records?
  start_time = time.time()
  
  for i in range(Records_Display):
    largest_id = smallest_id + num_records
    ran_number = random.randint(smallest_id, largest_id)
    if print_records == True:
      print ( my_linked_list.search(Client(ran_number)))
    else:
      my_linked_list.search(Client(ran_number))
  
  end_time = time.time()
  print (f"Seconds to pick {Records_Display} random records: {TTime(start_time, end_time)}")
  
  Continue() ########################################## END SCENARIO 2
    
  # Scenario 3: Call Center
  Title(S3)
  
  # how long does it take to add records randomly, and randomly display and remove records?
  start_time = time.time()
  current_id = smallest_id + num_records + 1
  
  for i in range(Records_Add):
    my_linked_list.add_last(Client(current_id))
    current_id += 1
  
  num_records = len(clients)
  
  # Display Random Records 
  for i in range(Records_Display):
    largest_id = smallest_id + num_records
    ran_number = random.randint(smallest_id, largest_id)
    if print_records == True:
      print ( my_linked_list.search(Client(ran_number)))
    else:
      my_linked_list.search(Client(ran_number))
  
  # Remove Random Records
  for i in range(Records_Remove):
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    if print_records == True:
      print ( my_linked_list.remove(Client(random_num)))
    else:
      my_linked_list.remove(Client(random_num))
  
  # Calculate Time
  end_time = time.time()
  print (f"Seconds to add {Records_Add} records, Display {Records_Display} records, and remove {Records_Remove} records: {TTime(start_time, end_time)}")
  Continue()

while True:
  main()
  os.system('clear')
  if input("Would you like to run another test? (Y/N)" ).strip().upper() == 'N':
    break