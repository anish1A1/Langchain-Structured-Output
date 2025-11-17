from pydantic import BaseModel

# to create a pydantic model a class needs to inherit pydantic class.
# Pydantic models helps to validate data type and if added wrong data type then it will give error 
class Student(BaseModel):
    name: str 
    age: int = 21
    # we can also set default value
    # name: str = 'aj'
    

# creating a dict
new_student ={
    'name': 'anish'
}

student = Student(**new_student)
print(student)
print(student.name)
print(student.age)
