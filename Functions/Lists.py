# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/30/2022

class Node:
    def __init__(self, initial_data=None):
        self.data = initial_data
        self.next = None
class NodeP6:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None      
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        
    def get_first(self):
        if self.__head != None:
            return self.__head.data
        else:
            return None
        
    def get_last(self):
        if self.__tail != None:
            return self.__tail.data
        else:
            return None
        
    def get_at(self, index):
        if self.__head == None:
            return None
        else:
            temp = self.__head
            
            # "traverse" or step down the chain
            for i in range(0, index):
                if temp == None:
                    return None
                else:
                    temp = temp.next
                
            if temp == None:
                return None
            else:
                return temp.data

    def add_first(self, data):
        # create a new node using the data
        new_node = Node(data)
        
        # add it to the front of the list
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node    # new_node becomes the head
            
    def add_last(self, data):
        # create a new node using the data
        new_node = Node(data)
        
        # add it to the end of the list
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node     # new_node becomes the tail

    def add_at(self, index, data):
        # if index = 0, add to front
        if index == 0:
            self.add_first(data)
            return       # end the method
        
        # create a new node
        new_node = Node(data)
        
        # traverse the list to just before the index to add
        temp = self.__head 
        
        for i in range(index - 1):    # notice the -1
            if temp.next != None:     # make sure we do not run over the end
                temp = temp.next
                
        # insert the new node
        new_node.next = temp.next
        temp.next = new_node
   
    def remove_first(self):
        # Special case, empty list so nothing to remove
        if self.__head == None:
            return        # end the method
        
        # Special case, single node in the list
        if self.__head.next == None:
            self.__head == None 
            self.__tail == None 
            
        # remove the head node from the data
        self.__head = self.__head.next 
        
    def remove_last(self):
        # Special case, empty list so nothing to remove
        if self.__head == None:
            return        # end the method
        
        # Special case, single node in the list
        if self.__head.next == None:
            self.__head == None 
            self.__tail == None 
            return        # end the method
                  
        # traverse the list and find the SECOND to last node
        temp = self.__head 
        
        while temp.next.next != None: # notice .next.next to
            temp = temp.next          #  find second to last node
            
        # delete the last node
        temp.next = None
        
    def remove_at(self, index):
        # Special case, empty list so nothing to remove
        if self.__head == None:
            return        # end the method
        
        # Special case, single node in the list
        if self.__head.next == None:
            self.__head == None 
            self.__tail == None 
            return        # end the method
            
        # traverse the list and find the NODE BEFORE the index
        temp = self.__head 
        
        for i in range(index - 1):    # notice the -1
            if temp.next.next != None:  # make sure we do not run over the end
                temp = temp.next
                
        # delete the node at that index
        temp.next = temp.next.next
        
    def remove(self, data):
        # Special case, empty list so nothing to remove
        if self.__head == None:
            return None       # end the method

        # Create a variable for the return value
        result = None
          
        # Special case, head node has data
        if self.__head.data == data:
            result = self.__head.data
            if self.__head.next == None:  # single node only
                self.__head == None 
                self.__tail == None
            else:
                self.__head = self.__head.next   # use second node as head
 
            return result       # end the method
            
        # traverse the list and find the NODE BEFORE the index
        temp = self.__head 
        parent = None
        
        while temp.next is not None:
            parent = temp 
            temp = temp.next 
            if temp.data == data:
                result = temp.data
                parent.next = temp.next # delete the node by overwriting the parent's next
                break     # end the loop

        return result
		
    def search(self, data):
        if self.__head == None:
            return None
        
        # traverse the list and find the data if possible
        temp = self.__head
        
        while temp is not None:
            if temp.data == data:
                return temp.data
            else:
                temp = temp.next
        
        # If the above loop finishes without returning,
        # it means the search item was not found.
        return None
	
        
    def is_empty(self):
        # if the head is empty, then the list is empty
        return self.__head == None 
    
    def get_length(self):
        # create count variable
        count = 0
        
        # traverse the list and count the nodes
        temp = self.__head 
        
        while temp != None:
            count += 1
            temp = temp.next
            
        return count
                
    def get_list(self):
        # create output variable
        items = ""
        
        # start at the top
        temp = self.__head
        
        # append all the data
        while temp != None:
            items += str(temp.data) + " "
            temp = temp.next
            
        # return the output variable
        return items        
                
    def contains(self, data):
        # check each node and see if it matches the data
        # start at the top with the head node
        temp = self.__head
        
        # traverse the list
        while temp != None:
            if temp.data == data:
                return True    # return True if we find the data!
            else:
                temp = temp.next
            
        # if we go through every node and do not find the data, return false
        return False
    
    def clear_list(self):
        self.__head = None
        self.__tail = None

class ArrayList:
    def __init__(self, size=10):
        self.__array = [None] * size
        self.__capacity = size
        self.__length = 0
        
    def get(self, index):
        if index < self.__length:
            return self.__array[index]
        else:
            return None
        
    def append(self, new_item):
        # resize() if the array is full
        if self.__capacity == self.__length:
            self.resize(self.__length * 2)

        # Insert the new item at index equal to self.__length
        self.__array[self.__length] = new_item

        # Increment the array's length
        self.__length = self.__length + 1
        
    def remove_at(self, index):
        # create a reference for the item
        item = None
        
        # Make sure the index is valid for the current array
        if index >= 0 and index < self.__length:
            # get the item
            item = self.__array[index]
            
            # Shift items from the given index up to the
            # end of the array.
            for i in range(index, self.__length-1):
                self.__array[i] = self.__array[i+1]

            # Update the array's length
            self.__length = self.__length - 1
            
        return item
            
    def resize(self, new_allocation_size):
        # Create a new array with the indicated size
        new_array = [None] * new_allocation_size

        # Copy items in current array into the new array
        for i in range(self.__length):
            new_array[i] = self.__array[i]

        # Assign the array data member with the new array
        self.__array = new_array

        # Update the allocation size
        self.__capacity = new_allocation_size
            
    def is_empty(self):
        # if the length is zero, return true
        return self.__length == 0
        
    def get_length(self):
        # return the current number of objects in the arraylist
        return self.__length

    def get_capacity(self):
        # return the current capacity of the internal array
        return self.__capacity
    
    def get_array(self):
        # return the internal array
        return self.__array
           
# additional ArrayList functions
    def insert_after(self, index, new_item):
        # resize() if the array is full
        if self.allocation_size == self.__length:
            self.resize(self.__length * 2)

        # Shift all the array items to the right,
        # starting from the last item and moving down to
        # the item just past the given index.
        for i in reversed(range(index+1, self.__length+1)):
            self.__array[i] = self.__array[i-1]
            
        # Insert the new item at the index just past the
        # given index.
        self.__array[index+1] = new_item
        
        # Update the array's length
        self.__length = self.__length + 1
        

    def search(self, item):
        # Iterate through the entire array
        for i in range(self.__length):
            # If the current item matches the search
            # item, return the current index immediately.
            if self.__array[i] == item:
                return self.__array[i]
                
        # If the above loop finishes without returning,
        # it means the search item was not found.
        return None
    
    def search_sorted(self, item):
        list = self.__array
        n = self.__length      # n is the number of records in the list  
        first = 0
        last = n - 1
        middle = 0
        
        # keep looking until we find the client or the first and last are flipped
        while first <= last:
            middle = int( (first + last) / 2 )
            if list[middle] == item:
                return list[middle]
            else:
                # move the end of list based on the middle number
                if item < list[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
                    
        # if we get this far, we did not find the record
        return None
    
    def remove(self, item):
        # create a reference for the item
        result = None
        
        # Iterate through the entire array
        for i in range(self.__length):
            # If the current item matches the search
            # item, return the current index immediately.
            if self.__array[i] == item:
                result = self.__array[i]
                
        # return the item if found, otherwise, return nothing (None)
        return result
        
    def clear_list(self):
        # clear the internal array using a default size
        size = 10
        self.__array = [None] * size
        
        # set capacity to default size and number of items to zero
        self.__capacity = size
        self.__length = 0
      
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
    
class Queue:
    def __init__(self):
        self.__length = 0
        self.__linked_list = LinkedList()
        
    def enqueue(self, data):
        self.__linked_list.add_last(data)
        self.__length += 1    # increment length
        
    def dequeue(self):
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
                
    def get_queue(self):
        return self.__linked_list.get_list()