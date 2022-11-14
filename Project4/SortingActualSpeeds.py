# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/14/2022

from Functions.Sort import *
from Functions.ClientP4 import Client
from datetime import date
import time     # Used to time code executions
import sys      # Used to Terminate application early
import os

def main():
  # Variables
  name = "Keith V Swoger" # Authors Name
  CSVFile = ['Data/P4_Clients100.csv','Data/P4_Clients1000.csv','Data/P4_Clients10000.csv','Data/P4_Clients100000.csv']
  file = 0 # Selects which CSV File to openOpens 100 clients by default
  Sorting = ['BubbleSort','SelectionSort','InsertionSort','ShellSort','QuickSort','MergeSort']
  size = ['100','1,000','10,000','100,000']
  print_records = True
  #----------------------------
  #----------SETTINGS----------
  #----------------------------
  
  print ("0 for 100\n1 for 1000\n2 for 10,000\n3 for 100,000")
  file = int((input("Select number of records to sort? (Default 100) ") or "0"))
  os.system('clear')
  
  print ("0 for BubbleSort\n1 for SelectionSort\n2 for InsertionSort\n3 for ShellSort\n4 for QuickSort\n5 for MergeSort")
  selection = int((input("Select sort type? (Default BubbleSort) ") or "0"))
  os.system('clear')
  
  answer = input("Display Records (Default True) (y/N)? " or "N") 
  if answer.lower() == "Y":
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
  #----------FUNCTIONS---------
  #----------------------------
  
  def Continue():
    print ()
    answer = input("Continue (Y/n)? " or "Y")
    print ()
    if answer.lower() == "N":
      sys.exit()
  
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
  #---------BUBBLESORT---------
  #----------------------------
      
  # Scenario Sorting Records from a datafile.
  num_records = len(clients)
  S1 = "-Scenario: Sorting " + str(num_records) + " Records"
  print ("-" * len(S1))
  print(S1)
  print ("-" * len(S1))
  
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
  total_time = end_time - start_time
  
  if print_records == True:  
    for clt in clients:
      print(clt)
      
  print(f"Seconds to sort {num_records} records: {total_time} using {Sorting[selection]} sorting method")
  
  Continue()
  os.system('clear')

while True:
  main()
  if input("Would you like to run another test? (Y/N)" ).strip().upper() == 'N':
    break