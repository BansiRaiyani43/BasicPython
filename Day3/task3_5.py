#Finding the maximum difference between tuple pairs

def difference(pairs):
    return max(abs(a - b) for a, b in pairs)

pairs = [(5, 7), (2, 6), (1, 9), (1, 3)]
result = difference(pairs)
print(result) 
