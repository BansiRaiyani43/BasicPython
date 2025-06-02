#Create a function/input that counts the integer's number of digits.Solve this without using strings.

def count(n):
    n = abs(n)  # abs - positive
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

print(count(318))     
print(count(-92563))  
print(count(4666))    
print(count(-314890))    
print(count(654321)) 
print(count(638476))  



