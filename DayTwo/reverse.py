# Create a function to reverse a given string

def reverse(s):
    s = s[::-1]
    return s

st = input("Insert a string:")

print(reverse(st))