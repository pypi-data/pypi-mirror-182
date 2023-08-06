print("1")
"""
from faker import Faker
import json
from random import randint



fake=Faker()

def input_data(x):
    student_data={}
    for i in range(0,x):
        student_data[i]={}
        student_data[i]['ID']=randint(1,100)
        student_data[i]['name']=fake.name()
        student_data[i]['address']=fake.address()
        student_data[i]['latitide']=str(fake.latitude())
        student_data[i]['longitude']=str(fake.longitude())
        print(student_data)


    with open('students.json','w')as fp:
        json.dump(student_data,fp)


def main():
    number_of_students=10
    input_data(number_of_students)
main()
"""
