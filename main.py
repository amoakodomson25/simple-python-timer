import time

seconds = int(input("Enter time in second: "))

while seconds:
    print(seconds)
    time.sleep(1)
    seconds -= 1
print ("Time Up")
