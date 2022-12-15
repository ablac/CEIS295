# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  10/29/2022

from Functions.Lists import ArrayList
from Functions.Client import Client
from Functions.Sort import QuickSort
from datetime import date
from Functions.Default import Continue, TTime, Title, Open
import time, random, os


def main():
  os.system('clear')
  # Variables
  name = "Keith V Swoger"  # Authors Name
  CSVFile = 'Data/P1_Clients.csv'  # Client Data.csv
  smallest_id = 100001  # Client ID Starting Point
  Records_Display = 1000  # How many records to display in random search
  Records_Add = 1000  # How many records to add
  Records_Remove = 1000  # How many records to remove
  sort = True  # Sort The Records?
  print_records = True  # Set to true to display all record updates, False to just display times.

  sec_title = [
    "Scenario: Printer Queue or Call Queue or Service Queue",
    "Scenario: Customer Service Center",
    "Scenario: Call Center"
  ]
  
  os.system('clear')
  # Settings for the Scenarios

  answer = input("Sort Records (Default True) (Y/n)? ")  # Sort the results?
  if answer.lower() == "N":
    sort = False
  os.system('clear')

  answer = input(
    "Display Records (Default True) (Y/n)? ")  # Display the Records?
  if answer.lower() == "N":
    print_records = False
  os.system('clear')

  Records_Display = int(input("Number to Display (Default 1000)? ")
                        or "1000")  # How many to display?
  os.system('clear')

  Records_Add = int(input("Number to Add (Default 1000)? ")
                    or "1000")  # How many to Add?
  os.system('clear')

  Records_Remove = int(input("Number to Remove (Default 1000)? ")
                       or "1000")  # How many to remove?
  os.system('clear')

  # Display Program Information
  print()
  print("Name:", name)
  print("Date :", date.today())
  print("Display Records:", print_records)
  print("Sorted:", sort)
  print("Records to Add:", Records_Add)
  print("Records to Remove:", Records_Remove)
  print("Records to Display", Records_Display)

  clients = []

  Continue()  
  ########################################## END SETTINGS
  
  # Read records from Clientdata.csv
  Open(CSVFile, clients, Client)

  # Sort the clients list
  if sort == True:
    QuickSort.sort(clients)

  # How many client objects?
  num_records = len(clients)

  # create an arraylist object
  my_array_list = ArrayList()

  # Scenario 1: Scenario: Printer Queue or Call Queue or Service Queue
  Title(sec_title[0])

  #how long does it take to add client records?
  start_time = time.time()

  for i in range(num_records):
    my_array_list.append(clients[i])

  end_time = time.time()
  print(
    f"Seconds to add all {num_records} records from file: {TTime(start_time, end_time)}"
  )

  #How long does it take to remove records from the front of the Array List
  start_time = time.time()

  for i in range(num_records):
    my_array_list.remove_at(0)

  end_time = time.time()
  print(
    f"Seconds to remove all records from front: {TTime(start_time, end_time)}")

  Continue()  ########################################## END SCENARIO 1

  #Scenario 2: Customer Service Center
  Title(sec_title[1])

  for i in range(num_records):
    my_array_list.append(clients[i])

  #how long does it take to randomly display records?
  start_time = time.time()

  for i in range(Records_Display):
    largest_id = smallest_id + num_records
    ran_number = random.randint(smallest_id, largest_id)
    if print_records == True:
      if sort == True:
        print(my_array_list.search_sorted(Client(ran_number)))
      else:
        print(my_array_list.search(Client(ran_number)))
    else:
      if sort == True:
        my_array_list.search_sorted(Client(ran_number))
      else:
        my_array_list.search(Client(ran_number))
  end_time = time.time()
  print(
    f"Seconds to pick {Records_Display} random records: {TTime(start_time, end_time)}"
  )

  Continue()  ########################################## END SCENARIO 2

  #Scenario 3: Call Center
  Title(sec_title[2])

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
        print(my_array_list.search_sorted(Client(ran_number)))
      else:
        print(my_array_list.search(Client(ran_number)))
    else:
      if sort == True:
        my_array_list.search_sorted(Client(ran_number))
      else:
        my_array_list.search(Client(ran_number))

  for i in range(Records_Remove):
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)

    if print_records == True:
      print(my_array_list.remove(Client(random_num)))
    else:
      my_array_list.remove(Client(random_num))

  end_time = time.time()
  print(
    "Seconds to add {Records_Add} records, Display {Records_Display} records, and Remove {Records_Remove} Records: {TTime(start_time, end_time)}"
  )
  Continue()


while True:
  main()
  os.system('clear')
  if input("Would you like to run another test? (Y/n)").strip().upper() == 'N':
    break