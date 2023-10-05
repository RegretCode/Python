# Given a list of integers, find the sum of all positive numbers.

list_of_numbers = [1, -1, 5, 10, -20, -6, 7]

sum = 0
i = 0

for i in list_of_numbers:
    if i > 0:
        sum = sum + i
        
print(sum)