seconds = int(input("Enter Seconds: "))

hour = seconds // 3600
minutes = (seconds % 3600) // 60
s = (seconds % 3600) % 60

print(f"{hour} : {minutes} : {s}")
