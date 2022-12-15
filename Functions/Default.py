# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/14/2022

import sys
from Functions.Client import Client

def Continue():
  print()
  answer = input("Continue (Y/n)? " or "y")
  if answer.lower() == "n":
    sys.exit()
  print()


def TTime(Start, End):
  Total_Time = End - Start
  return round(Total_Time, 6)

def Title(text):
  print("-" * len(text))
  print(text)
  print("-" * len(text))

def Open(file, clients):
  with open(file) as infile:
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
  return clients