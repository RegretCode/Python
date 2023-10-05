# Write a program that converts a given number od days into years, weeks, and days.

value = float(input("Insert the amount you want to convert: "))

weeks = value / 7
year = value / 365

print(f"Years: {year}\nWeeks: {weeks}\nDay: {value}")