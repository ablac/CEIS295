# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  10/29/2022

class Client:
  def __init__(self, client_id=0, first_name="Unknown", last_name="Unknown", phone="Unknown", email="Unknown"):
    self.__client_id = client_id
    self.__first_name = first_name
    self.__last_name = last_name
    self.__phone = phone
    self.__email = email