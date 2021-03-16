second = round(int(input("Enter Second: ")))

hour = second / 3600
OutOfPlace= hour * 3600 - second
minute = OutOfPlace / 60
second2 = 60 * minute  - OutOfPlace

print(f"{hour} : {minute} : {second2}")
