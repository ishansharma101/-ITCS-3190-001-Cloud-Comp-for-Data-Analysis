
while True:

    year = int(input("Enter a year: "))

    if year < 999 or year > 9999:
        print ("You entered an invalid year.")
        continue

    if year % 4 == 0 and year % 100 != 0:
        print (year,"is a leap year.")
    elif year % 400 == 0: 
        print (year,"is a leap year.")
    else:
        print(year, "is not a leap year.")

