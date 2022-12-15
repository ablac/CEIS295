# Name: Keith V Swoger
# School : DeVry University
# Course: CEIS 295
# Date:  10/29/2022

from Functions.Lists import Stack

# create the Stack and add some items
num_stack = Stack()

# test the add method
num_stack.push(99)  # Add 99 - 99
num_stack.push(44)  # Add 44 - 44 99
num_stack.push(42)  # Add 42 - 42 44 99
num_stack.push(66)  # Add 66 - 66 42 44 99
num_stack.push(17)  # Add 17 - 17 42 44 99 66
num_stack.push(23)  # Add 23 - 23 42 44 99 66 17
num_stack.push(13)  # Add 13 - 13 42 44 23 99 66 17

# show the current stack
print("Current stack after adding items:", num_stack.get_stack())

# test the get methods
print("\nlength:", num_stack.get_length())
print("is_empty:", num_stack.is_empty())
print("peek:", num_stack.peek())

# show the current stack
print("\nPopping off some items...")

# test the pop method
for i in range(5):
  print("pop:", num_stack.pop())

# show the current stack
print("\nCurrent stack after popping some items:", num_stack.get_stack())
print("Current length of the stack:", num_stack.get_length())
print("is_empty:", num_stack.is_empty())

# test the pop method and pop off too many
print("\nPopping off too many items...")
for i in range(5):
  print("pop:", num_stack.pop())

# show the current stack
print("\nCurrent stack after popping more items:", num_stack.get_stack())
print("Current length of the stack:", num_stack.get_length())
print("is_empty:", num_stack.is_empty())
