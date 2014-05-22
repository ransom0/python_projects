timestring = input("Enter the time in XX:XX: ")

ms = [60, 1]

time = sum([a*b for a,b in zip(ms, [int(i) for i in timestring.split(":")])])
print(time)