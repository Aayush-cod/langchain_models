from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Provides proper validation for data passing through pydantic base model unlike typed dict which do not validates

class Student(BaseModel):

    name : str
    # setting default value
    # name : str = 'Aayush'

    # Setting optional value
    age : Optional[int] = None

    email : EmailStr

    cgpa : float = Field(gt=0, lt= 10, default = 6, description = 'A decimal value representing the cgpa of students.')

# new_student = {'name': 'Aayush', 'age': 21}

# type coercing - pydantic it self can change datatype if needed according to its levek like here changinng str 21 to int 21
# new_student = {'name': 'Aayush', 'age': '21'}

# built in validation or validators
# new_student = {'name': 'Aayush', 'age': '21', 'email': "abc@gmail.com"}

# Field Function - can add default values , constraints, description or regex expressions
new_student = {'name': 'Aayush', 'age': '21', 'email': "abc@gmail.com", 'cgpa':8.2}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict)

student_json = student.model_dump_json()

print(student_json)

# print(type(student))