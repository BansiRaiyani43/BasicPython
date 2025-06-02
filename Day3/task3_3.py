#Create a program that takes a list of numbers and returns the sum of all prime numbers in the list.

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    """Return the sum of all prime numbers in the list."""
    return sum(num for num in numbers if is_prime(num))

# Example usage:
numbers = [2, 3, 4, 5, 6, 7, 10, 13, 17]
print("Sum of primes:", sum_of_primes(numbers))
