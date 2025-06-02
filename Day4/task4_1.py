""" 
Create a function that returns the amount of duplicate characters in a string. It will be case sensitive and spaces are
included. If there are no duplicates, return 0.
"""

def count_duplicates(s):
    seen = {}
    duplicates = 0
    for char in s:
        if char in seen:
            if seen[char] == 1:
                duplicates += 1  # Count only the first time a duplicate is found
            seen[char] += 1
        else:
            seen[char] = 1
    return duplicates
 
print(count_duplicates("aab"))          
print(count_duplicates("abc"))          
