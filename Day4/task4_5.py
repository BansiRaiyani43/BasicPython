#Create a function/input that returns the sum of all even elements in a 2D matrix.

def sum_of_evens(matrix):
    total = 0
    for row in matrix:
        for num in row:
            if num % 2 == 0:
                total += num
    return total

print(sum_of_evens([[1, 0, 2], [5, 5, 7], [9, 4, 3]]))  
print(sum_of_evens([[1, 1], [1, 1]]))
print(sum_of_evens([[42, 9], [16, 8]]))
	