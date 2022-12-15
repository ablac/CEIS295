# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  12/01/2022

import time, random, os
from datetime import date
from Functions.Client import ClientP6 as Client
from Functions.Search import BinarySearchTree as BST
from Functions.Default import Continue, TTime, Title, Open


def main():
  os.system('clear')
  # Settings
  name = "Keith V Swoger"  # Authors Name
  CSVFile = 'Data/P6_Clients.csv'
  sec_title = [
    "Scenario 1: Printer Queue/Call Queue/Service Queue",
    "Scenario 2: Customer Service Center",
    "Scenario 3: Add/Remove/Delete Random Records"
  ]
  smallest_id = 100001
  rec_disp = 1000
  rec_add = 1000
  rec_del = 1000
  print_records = False

  print("How many records do you want to Display?")
  rec_disp = int((input(f"Number of records to display? (Default {rec_disp}) ")
                  or rec_disp))
  os.system('clear')

  print("How many records do you want to Add?")
  rec_add = int((input(f"Number of records to Add? (Default {rec_add}) ")
                 or rec_add))
  os.system('clear')

  print("How many records do you want to Delete?")
  rec_del = int((input(f"Number of records to Delete? (Default {rec_del}) ")
                 or rec_del))
  os.system('clear')

  answer = input(f"Display Records (N/y) (Default {print_records})? "
                 or "N")
  if answer.lower() == "y":
    print_records = True
  os.system('clear')

  # Display Authors Name and Date
  print()
  print("Name:", name)
  print("Date :", date.today())
  print("Records to Display:", rec_disp)
  print("Records to Add:", rec_add)
  print("Records to Delete:", rec_del)
  print("Print Records:", print_records)

  # Create a List
  clients = []

  # Open, Read, and Assign CSV File
  Open(CSVFile, clients, Client)
  
  # Count Records
  num_records = len(clients)

  # Create the binary search tree to test real world speeds.
  my_bst = BST()

  Continue()

  # -------------------------------------------------- #
  # Scenario 1: Printer Queue/Call Queue/Service Queue #
  # -------------------------------------------------- #

  Title(sec_title[0])

  # How long does it take to add client records to BST
  start_time = time.time()

  for i in range(num_records):
    my_bst.insert(clients[i])

  end_time = time.time()
  print(f"Seconds to add records: {TTime(start_time, end_time)}")

  # How long does it take to remove the smallest records of the BST
  start_time = time.time()

  for i in range(num_records):
    my_bst.remove_minimum()

  end_time = time.time()
  print(f"Seconds to remove records: {TTime(start_time, end_time)}")

  Continue()

  # ----------------------------------- #
  # Scenario 2: Customer Service Center #
  # ----------------------------------- #

  Title(sec_title[1])

  # Add clients to BinarySearchTree
  for i in range(num_records):
    my_bst.insert(clients[i])

  # How long to randomly display 1000 Client records
  start_time = time.time()

  largest_id = smallest_id + num_records
  for i in range(rec_disp):
    random_num = random.randint(smallest_id, largest_id)
    if print_records == True:
      print(my_bst.search(Client(random_num)))
    else:
      my_bst.search(Client(random_num))

  end_time = time.time()
  print(
    f"Seconds to display {rec_disp} random records: {TTime(start_time, end_time)}"
  )

  for i in range(num_records):
    my_bst.remove_minimum()

  Continue()

  # --------------------------------------------- #
  # Scenario 3: Add/Display/Delete Random Records #
  # --------------------------------------------- #

  Title(sec_title[2])

  # Add clients to BinarySearchTree
  for i in range(num_records):
    my_bst.insert(clients[i])

  start_time = time.time()

  # How long to add more clients.
  current_id = smallest_id + num_records + 1
  for i in range(rec_add):
    my_bst.insert(Client(current_id))
    current_id += 1

  # How long to display random records
  for i in range(rec_disp):
    random_num = random.randint(smallest_id, current_id)
    if print_records == True:
      print(my_bst.search(Client(random_num)))
    else:
      my_bst.search(Client(random_num))

  # How long to remove random records
  largest_id = current_id
  for i in range(rec_del):
    random_num = random.randint(smallest_id, largest_id)
    my_bst.remove(Client(random_num))
    largest_id -= 1

  end_time = time.time()
  print(f"Seconds to add {rec_add} records, display {rec_disp} records")
  print(f"and delete {rec_del} records: {TTime(start_time, end_time)}")

  Continue()


while True:
  main()
  os.system('clear')
  if input("Would you like to run another test? (Y/n)").strip().upper() == 'N':
    break