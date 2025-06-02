#Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the 
#total in a list.

def count_data_types(*args):
    type_counts = {}
    
    for arg in args:
        data_type = type(arg)
        if data_type in type_counts:
            type_counts[data_type] += 1
        else:
            type_counts[data_type] = 1
    
    return [len(type_counts)]

result = count_data_types(1, "hello", 3.14, True,[1, 2], {"a": 1})
print(result)
