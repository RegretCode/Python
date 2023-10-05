# Create a function to count the numbers of vowels in a given string.

def vowelsCount(s):
    vowels = ("a", "e", "i", "o", "u")
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count

st = "Vaaaaaaaai Cunrintiaaaaaaaaaaa"

print("Number of vowels:", vowelsCount(st))
