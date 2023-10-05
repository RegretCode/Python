# Create a python function to check if a given string is a palindrome.

def palindrome(x):
    return x == x[::-1]

x = "arara"

resp = palindrome(x)

if resp:
    print("Yes")
else: 
    print("No")