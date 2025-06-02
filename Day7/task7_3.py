def double_swap(txt, c1, c2):
    result = ''
    for char in txt:
        if char == c1:
            result += c2
        elif char == c2:
            result += c1
        else:
            result += char
    return result

print(double_swap("aabbccc", "a", "b"))  
print(double_swap("random w#rds writt&n h&r&", "#", "&"))  
print(double_swap("128 895 556 788 999", "8", "9"))  
