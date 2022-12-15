# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/14/2022

from Functions.Sort import BubbleSort, SelectionSort, InsertionSort, ShellSort, QuickSort, MergeSort
from Functions.Client import ClientP4 as Client
from Functions.Default import Continue, TTime, Title
from datetime import date
import time, os     # Used to time code executions

def main():
  os.system('clear')
  # Variables
  name = "Keith V Swoger" # Authors Name
  CSVFile = ['Data/Clients100.csv','Data/Clients1000.csv','Data/Clients10000.csv','Data/Clients100000.csv']
  file = 0 # Selects which CSV File to openOpens 100 clients by default
  Sorting = ['BubbleSort','SelectionSort','InsertionSort','ShellSort','QuickSort','MergeSort']
  size = ['100','1,000','10,000','100,000']
  print_records = False
  #----------------------------
  #----------SETTINGS----------
  #----------------------------
  
  print (f"0 for {size[0]}\n1 for {size[1]}\n2 for {size[2]}\n3 for {size[3]}")
  file = int((input(f"Select number of records to sort? (Default {size[0]}) ") or "0"))
  os.system('clear')
  
  print (f"0 for {Sorting[0]}\n1 for {Sorting[1]}\n2 for {Sorting[2]}\n3 for {Sorting[3]}\n4 for {Sorting[4]}\n5 for {Sorting[0]}")
  selection = int((input(f"Select sort type? (Default {Sorting[0]}) ") or "0"))
  os.system('clear')
  
  answer = input("Display Records (Default True) (y/N)? " or "N") 
  if answer.lower() == "y":
    print_records = True
  os.system('clear')
  
  # Display Name and Date in output
  print ()
  print ("Name:", name)
  print ("Date :", date.today())
  print (f"Sorting file {size[file]}")
  print (f"Sorting type {Sorting[selection]}")
  print (f"Display Records set to {print_records}")
  print ()
  
  #----------------------------
  #--------PROGRAM START-------
  #----------------------------
  
  clients = []
  
  # Read records from CSV File.
  with open(CSVFile[file]) as infile:
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
  
  #----------------------------
  #---------SORTING------------
  #----------------------------
      
  # Scenario Sorting Records from a datafile.
  num_records = len(clients)
  S1 = "-Scenario: Sorting " + str(num_records) + " Records"
  
  Title(S1)
  
  Continue()
  
  start_time = time.time()
  
  #call the static sort method in the class
  if selection == 0:
    BubbleSort.sort(clients)
  elif selection == 1:
    SelectionSort.sort(clients)
  elif selection == 2:
    InsertionSort.sort(clients)
  elif selection == 3:
    ShellSort.sort(clients)
  elif selection == 4:
    QuickSort.sort(clients)
  elif selection == 5:
    MergeSort.sort(clients)
  
  end_time =time.time()
  
  if print_records == True:  
    for clt in clients:
      print(clt)
      
  print(f"Seconds to sort {num_records} records: {TTime(start_time, end_time)} using {Sorting[selection]} sorting method")
  Continue()

while True:
  main()
  os.system('clear')
  if input("Would you like to run another test? (Y/N)" ).strip().upper() == 'N':
    break