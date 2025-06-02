class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __repr__(self):
        return f"{self.firstname} {self.lastname}, {self.age}"

def people_sort(people, attribute):
    return sorted(people, key=lambda person: getattr(person, attribute))

p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

print(people_sort([p1, p2, p3], "firstname"))
print(people_sort([p1, p2, p3], "lastname"))
print(people_sort([p1, p2, p3], "age"))
