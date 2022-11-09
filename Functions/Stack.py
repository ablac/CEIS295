# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/8/2022

from Functions.LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.__length = 0
        self.__linked_list = LinkedList()
        
    def push(self, data):
        self.__linked_list.add_first(data)
        self.__length += 1    # increment length
        
    def pop(self):
        data = self.__linked_list.get_first()
        self.__linked_list.remove_first()
        if data != None:
            self.__length -= 1    # decrement length
        return data
        
    def peek(self):
        return self.__linked_list.get_first()

    def is_empty(self):
        # if the length is zero, then the stack is empty
        return self.__length == 0 
    
    def get_length(self):    
        return self.__length
                
    def get_stack(self):
        return self.__linked_list.get_list()
		
		