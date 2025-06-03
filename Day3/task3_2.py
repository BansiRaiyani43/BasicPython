#Create a program that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the 
#range a, b inclusive

def sum_divisible_by_c(a, b, c):
    if c == 0:
        raise ValueError("Division by zero is not allowed.")
    return sum(x for x in range(a, b + 1) if x % c == 0)

# Example usage:
print(sum_divisible_by_c(1, 10, 3)) 