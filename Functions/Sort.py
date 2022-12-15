# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  11/14/2022


class BubbleSort:

  @staticmethod
  def sort(list):
    num_records = len(list)
    for i in range(num_records - 1):
      for j in range(num_records - i - 1):
        if list[j] > list[j + 1]:
          # flip them!
          temp = list[j]
          list[j] = list[j + 1]
          list[j + 1] = temp


class SelectionSort:

  @staticmethod
  def sort(list):
    num_records = len(list)
    for i in range(num_records - 1):

      # Find index of smallest remaining element
      index_smallest = i
      for j in range(i + 1, num_records):

        if list[j] < list[index_smallest]:
          index_smallest = j

      # Swap list[i] and list[index_smallest]
      temp = list[i]
      list[i] = list[index_smallest]
      list[index_smallest] = temp


class InsertionSort:

  @staticmethod
  def sort(list):
    num_records = len(list)
    for i in range(1, num_records):
      j = i

      # Insert list[i] into sorted part
      # stopping once list[i] in correct position
      while j > 0 and list[j] < list[j - 1]:
        # Swap numbers[j] and numbers[j - 1]
        temp = list[j]
        list[j] = list[j - 1]
        list[j - 1] = temp
        j -= 1


class ShellSort:

  @staticmethod
  def sort(list):
    num_records = len(list)

    # keep cutting the gap size in half as an integer -- using //
    gap = num_records // 2
    while gap > 0:
      for i in range(gap, num_records):
        temp = list[i]
        j = i

        while j >= gap and temp < list[j - gap]:
          list[j] = list[j - gap]
          j -= gap

        list[j] = temp

      # cut gap in half as an integer -- using //
      gap = gap // 2


class QuickSort:

  @classmethod
  def sort(cls, list):
    num_records = len(list)
    cls.quicksort(list, 0, num_records - 1)

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


class MergeSort:

  @classmethod
  def sort(cls, list):
    num_records = len(list)
    # Initial call to merge_sort
    cls.merge_sort(list, 0, num_records - 1)

  @classmethod
  def merge_sort(cls, list, i, k):
    j = 0

    if i < k:
      j = (i + k) // 2  # Find the midpoint in the partition

      # Recursively sort left and right partitions
      cls.merge_sort(list, i, j)
      cls.merge_sort(list, j + 1, k)

      # Merge left and right partition in sorted order
      cls.merge(list, i, j, k)

  @classmethod
  def merge(cls, list, i, j, k):
    merged_size = k - i + 1  # Size of merged partition
    merged_list = [0] * merged_size  # Dynamically allocates temporary array
    # for merged list
    merge_pos = 0  # Position to insert merged number
    left_pos = i  # Initialize left partition position
    right_pos = j + 1  # Initialize right partition position

    # Add smallest element from left or right partition to merged list
    while left_pos <= j and right_pos <= k:
      if list[left_pos] <= list[right_pos]:
        merged_list[merge_pos] = list[left_pos]
        left_pos += 1
      else:
        merged_list[merge_pos] = list[right_pos]
        right_pos += 1
      merge_pos = merge_pos + 1

    # If left partition is not empty, add remaining elements to merged list
    while left_pos <= j:
      merged_list[merge_pos] = list[left_pos]
      left_pos += 1
      merge_pos += 1

    # If right partition is not empty, add remaining elements to merged list
    while right_pos <= k:
      merged_list[merge_pos] = list[right_pos]
      right_pos = right_pos + 1
      merge_pos = merge_pos + 1

    # Copy merge number back to list
    for merge_pos in range(merged_size):
      list[i + merge_pos] = merged_list[merge_pos]