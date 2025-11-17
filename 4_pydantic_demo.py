from typing import Optional
from pydantic import BaseModel, EmailStr, Field

# to create a pydantic model a class needs to inherit pydantic class.
# Pydantic models helps to validate data type and if added wrong data type then it will give error 
class Student(BaseModel):
    name: str 
    age: int = 21
    job: Optional[int] = None
    # we can also set default value
    # name: str = 'aj'
    
    # email: EmailStr
    percentage: float = Field(gt=0, lt=10, default=0, description='A decimal value representing percentage of the student')
    

# creating a dict
new_student ={
    'name': 'anish',
    'age': '23',
    'email' : 'abc@gmail.com'
    # Here written age in string but still pydantic will get it sa int. since add int in the class
}

student = Student(**new_student)
print(student)
print(student.name)
print(student.age)


print('\n')

# modifing it into a dictionary for ease of use and requirements
dict_student = dict(student)
print(dict_student)
print(dict_student['name'])

print('\n')


# modifing into json format

json_student = student.model_dump_json()
print(json_student)

