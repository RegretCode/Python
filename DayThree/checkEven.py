# Create a loop that prints the first 10 even numbers.

lst = list(range(1, 21))
print(lst)

for value in lst:
    if (value % 2) == 0:
        print(value)
