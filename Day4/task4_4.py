#Create a function/input that, given a number, returns the corresponding value of that index in the Fibonacci series.
#The Fibonacci Sequence is the series of numbers:
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...
  
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci(4))
print(fibonacci(6))