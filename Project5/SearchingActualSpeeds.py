# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/14/2022

from Functions.Sort import QuickSort
from Functions.Search import LinearSearch, BinarySearch
from Functions.Client import Client
from Functions.Default import Continue, TTime, Title
from datetime import date
import time, os, random  # Used to time code executions


def main():
  os.system('clear')
  # Variables
  name = "Keith V Swoger"  # Authors Name
  CSVFile = [
    'Data/Clients100.csv', 'Data/Clients1000.csv', 'Data/Clients10000.csv',
    'Data/Clients100000.csv'
  ]
  Searching = ['LinearSearch', 'BinarySearch']
  size = ['100', '1,000', '10,000', '100,000']

  # Defaults
  print_records = False
  answer = "N"
  search = 1000
  file = 0  # Selects which CSV File to openOpens 100 clients by default
  selection = 0  # Selects which search to use by default
  start_record = 100001
  #----------------------------
  #----------SETTINGS----------
  #----------------------------

  print(f"0 for {size[0]}\n1 for {size[1]}\n2 for {size[2]}\n3 for {size[3]}")
  file = int(
    (input(f"Select number of records to sort? (Default {size[file]}) ")
     or file))
  os.system('clear')

  print(f"0 for {Searching[0]}\n1 for {Searching[1]}")
  selection = int(
    (input(f"Select sort type? (Default {Searching[selection]}) ")
     or selection))
  os.system('clear')

  print("How many search's do you want to preform?")
  search = int((input(f"Number of searches? (Default {search}) ") or search))
  os.system('clear')

  answer = input(f"Display Records (N/y) (Default {answer})? " or answer)
  if answer.lower() == "y":
    print_records = True
  os.system('clear')

  # Display Name and Date in output
  print()
  print("Name:", name)
  print("Date :", date.today())
  print(f"Sorting file {size[file]}")
  print(f"Sorting type {Searching[selection]}")
  print(f"Display Records set to {print_records}")
  print()

  #----------------------------
  #--------PROGRAM START-------
  #----------------------------

  clients = []

  # Read records from CSV File.
  with open(CSVFile[file]) as infile:
    for line in infile:
      # Split the line based on the commas
      s = line.split(',')
      client_id = int(s[0])  # Convert to Int from String
      f_name = s[1]
      l_name = s[2]
      phone = s[3]
      email = s[4]

      # Create Client object
      clt = Client(client_id, f_name, l_name, phone, email)
      # Add the client object to list
      clients.append(clt)

  #----------------------------
  #---------SEARCHING_---------
  #----------------------------

  # Scenario Sorting Records from a datafile.
  num_records = len(clients)
  end_record = start_record + num_records
  S1 = f"-Scenario: Searching for {search} random records within {str(num_records)} records"
  
  Title(S1)

  Continue()

  # Must sort data before searching with Binary
  if selection == 1:
    QuickSort.sort(clients)
    print("Completed Quicksort of data.")
    Continue()

  start_time = time.time()

  #call the static search method in the class
  for i in range(search):
    client_id = random.randint(start_record, end_record)
    clt = Client(client_id)

    #Search Function
    if selection == 0:
      result = LinearSearch.search(clients, clt)
    elif selection == 1:
      result = BinarySearch.search(clients, clt)
    else:
      break

    if print_records == True:
      if result is None:
        print(clt, "was not found.")
      else:
        print(result)

  end_time = time.time()

  print(
    f"Seconds to search {search} random records: {TTime(start_time, end_time)} using {Searching[selection]} method"
  )

  Continue()


while True:
  main()
  os.system('clear')
  if input("Would you like to run another test? (Y/n)").strip().upper() == 'N':
    break