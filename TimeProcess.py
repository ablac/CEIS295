# Name: Keith V Swoger
# Date:  10/29/2022

# use time library to time the code executions
import time

# get number of requested loops
loops_input = input("How many loops? ")

# convert to int.
loops = int(loops_input)

# get current time before the process
start_time = time.time()

# run the process
for i in range(loops):
    print( "Hello Everyone!" )

# get current time after the process
end_time = time.time()

# subtract start time from end time to get time used by process
total_time = end_time - start_time

# Show the result.  Note: .6f means “show six decimal places”
print("\nSeconds to run " + str(loops) + " times: {:.6f}".format(total_time))

print ("Returning to mainm menu")
import main