#Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operator"

print(calculate(5, 3, '+'))  
print(calculate(5, 3, '-'))  
print(calculate(5, 3, '*'))  
print(calculate(5, 0, '/'))  
