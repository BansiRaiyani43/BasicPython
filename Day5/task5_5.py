#Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(num):
    if num <= 2:
        return 2
    candidate = num
    while not is_prime(candidate):
        candidate += 1
    return candidate

print(next_prime(7))   
print(next_prime(8))