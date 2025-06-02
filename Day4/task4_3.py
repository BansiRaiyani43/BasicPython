"""
Given a list nums where each integer is between 1 and 100, return a sorted list containing only duplicate numbers from the given 
nums list
"""

def duplicate_nums(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return sorted(duplicates)

print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
	