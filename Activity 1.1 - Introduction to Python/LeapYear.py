# For this activity, you will write a script that will ask a user to enter a year and display whether the year is a leap year or not.

# Note: A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. 




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

