# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/22/2022


class Client:

  def __init__(self,
               client_id=0,
               first_name="Unknown",
               last_name="Unknown",
               phone="Unknown",
               email="Unknown"):
    self.__client_id = client_id
    self.__first_name = first_name
    self.__last_name = last_name
    self.__phone = phone
    self.__email = email

  #classes that compare object, must implement __eq__ Method and __lt__ method
  #__lt__ = Less Than and must return a Boolean
  #__le__ = Less Than or Equal to and must return a Boolean
  #__eq__ = equals to and must return a boolean
  def __lt__(self, other):
    return self.__client_id < other.__client_id

  def __le__(self, other):
    return self.__client_id <= other.__client_id

  def __eq__(self, other):
    return self.__client_id == other.__client_id

  #__str__() method, automatically called when printing object
  def __str__(self):
    return str(
      self.__client_id) + ", " + self.__last_name + ", " + self.__first_name

  #getters and setters
  def get_client_id(self):
    return self.__client_id

  def set_client_id(self, client_id):
    self.__client_id = client_id

  def get_first_name(self):
    return self.__first_name

  def set_first_name(self, first_name):
    self.__first_name = first_name

  def get_last_name(self):
    return self.__last_name

  def set_last_name(self, last_name):
    self.__last_name = last_name

  def get_phone(self):
    return self.__phone

  def set_phone(self, phone):
    self.__phone = phone

  def get_email(self):
    return self.__email

  def set_email(self, email):
    self.__email = email


# Client P4
class ClientP4(Client):

  def __lt__(self, other):
    this_full_name = self._Client__last_name + " " + self._Client__first_name
    other_full_name = other._Client__last_name + " " + other._Client__first_name
    return this_full_name < other_full_name

  def __le__(self, other):
    this_full_name = self._Client__last_name + " " + self._Client__first_name
    other_full_name = other._Client__last_name + " " + other._Client__first_name
    return this_full_name <= other_full_name

  #__str__() method, automatically called when printing object
  def __str__(self):
    return self._Client__last_name + ", " + self._Client__first_name


# Client P6
class ClientP6(Client):

  def __str__(self):
    return "[" + str(self._Client__client_id) + "]"
