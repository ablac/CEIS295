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