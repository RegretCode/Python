# Implement a program that checks if a given stringing is a palindrome.

entry = input("Insert to check if is a palindrome: ")


def palindrome(s):
    return s == s[::-1]

response = palindrome(entry)

if response:
    print("Is a palindrome.")
else:
    print("Is not a palindrome")

