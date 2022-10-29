class Quicksort:
    @classmethod
    def sort(cls, list):
        num_records = len(list)
        cls.quicksort(list, 0, num_records-1)
        
    @classmethod
    def quicksort(cls, list, start_index, end_index):
        # Only attempt to sort the list segment if there are
        # at least 2 elements
        if end_index <= start_index:
            return
              
        # Partition the list segment
        high = cls.partition(list, start_index, end_index)
    
        # Recursively sort the left segment
        cls.quicksort(list, start_index, high)
    
        # Recursively sort the right segment
        cls.quicksort(list, high + 1, end_index)
    
    @classmethod
    def partition(cls, numbers, start_index, end_index):
        # Select the middle value as the pivot.
        midpoint = start_index + (end_index - start_index) // 2
        pivot = numbers[midpoint]
       
        # "low" and "high" start at the ends of the list segment
        # and move towards each other.
        low = start_index
        high = end_index
       
        done = False
        while not done:
            # Increment low while numbers[low] < pivot
            while numbers[low] < pivot:
                low = low + 1
          
            # Decrement high while pivot < numbers[high]
            while pivot < numbers[high]:
                high = high - 1
          
            # If low and high have crossed each other, the loop
            # is done. If not, the elements are swapped, low is
            # incremented and high is decremented.
            if low >= high:
                done = True
            else:
                temp = numbers[low]
                numbers[low] = numbers[high]
                numbers[high] = temp
                low = low + 1
                high = high - 1
       
        # "high" is the last index in the left segment.
        return high