# Given a list of numbers, find the sum and average.

num = [10, 20, 30, 40, 50]

sum = 0

for x in num:
    sum = sum + x

average = sum / (len(num))
print(average)