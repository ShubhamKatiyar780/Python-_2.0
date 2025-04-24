print("Hello", "World")
print(5)
print(True)

# use of the separator
print(2.7, 'Hello', False)
print(2.7, 'Hello', False, sep='/')

# use of the end='\n'
print("Hello", end="-")
print("World")

# use of file=sys.stdout   (standard output shows on the screen) by default  but you can change
with open('output.txt', 'w') as f:
    print("hello from shubham", file=f) # this write the msg in output.txt file not shows on the scren

# use of the flush=false  that means the output is temporarily stored in memory
# flush=True    forces python to write the output immediately
# when you want to rel-time output like progress bars, live updates
import time
for i in range(5):
    print(i, end=" ", flush=True)  #  Without flush=True, the numbers might all show up together after the loop ends
    # print(i, end=" ", flush=False) 
    time.sleep(1)



print(type(print))