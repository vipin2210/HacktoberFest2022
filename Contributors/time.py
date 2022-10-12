# Python program to explain time.time() method

# importing time module
import time

# Get the epoch
obj = time.gmtime(0)
epoch = time.asctime(obj)
print("epoch is:", epoch)

# Get the time in seconds
# since the epoch
time_sec = time.time()

# Print the time
print("Time in seconds since the epoch:", time_sec)
