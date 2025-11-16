from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    
new_person : Person = {'name': 'Aj','age': 24}

# new_person : Person = {'name': 'Aj','age': "24"}

print(new_person)

# Typed disctionary are used so that it will help with varable data type miss alining its value.
# it only a type safety. for e.g. it will not throw error if the value of int is writen in str.
