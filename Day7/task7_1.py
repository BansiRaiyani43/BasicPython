#Create a Program that takes a string (a random name). If the last character of the name is an "a", return True, otherwise return False.

def ends_with_a(name):
    return name[-1].lower() == 'a' if name else False

print(ends_with_a("Maria"))
print(ends_with_a("apple"))

#Create a Program that takes a string (a random name). If the last and first character of the name is an "d", return True, otherwise return False.

def starts_and_ends_with_d(name):
    name = name.strip().lower() 
    return len(name) > 0 and name[0] == 'd' and name[-1] == 'd'

print(starts_and_ends_with_d("David"))  
print(starts_and_ends_with_d("john"))      

