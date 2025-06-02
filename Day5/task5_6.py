#Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.

def sort_students(student_dict):
    return sorted(student_dict.keys())
students = {
    "Alice": 85,
    "John": 88,
    "Charlie": 90,
    "Bob": 78
    
}

print(sort_students(students)) 

