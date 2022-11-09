# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/8/2022

# Used to get current data and time
from time import strftime

class Call:
  def __init__(self, client_id=0, client_name="Unknown", client_phone="Unknown"):
    self.client_id = client_id
    self.client_name = client_name
    self.client_phone = client_phone
    self.call_date = strftime("%m/%d/%Y")
    self.call_time = strftime("%H:%M")

  # __STR__() method is automatically called when printing object
  def __str__(self):
    return str(self.client_id) + ", " + self.client_name + "\n\tPhone: " + self.client_phone + "\tDate/Time: " + self.call_date + " @ " + self.call_time