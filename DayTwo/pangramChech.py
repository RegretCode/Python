# Write a program in Python to check if a given string is a pangram (contains all letter of the alphabet).

def pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for c in alphabet:
        if c not in s.lower():
            return False
    
    return True

st = "Leoon, Help meeeeeeee"

ans = pangram(st)

if ans:
    print("It is a pangram")
else:
    print("Is not a pangram")