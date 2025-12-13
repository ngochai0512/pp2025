import math as m
from datetime import datetime
from domain import Students, Course

def add_student(university):
    sid = input("Enter student ID: ")
    name = input("Enter student's name: ")
    dob = datetime.strptime(input("Date of birth (dd/mm/yyyy): "), "%d/%m/%Y")
    university.students[sid] = Students(sid, name, dob)

def add_course(university):
    cid = input("Enter course ID: ")
    cname = input("Enter course name: ")
    credits = int(input("Enter course credits: "))
    university.courses[cid] = Course(cid, cname, credits)

def input_marks(university):
    cid = input("Enter course ID to input marks: ")
    if cid not in university.courses:
        print("Course not found!")
        return

    university.marks[cid] = {}

    for sid, student in university.students.items():
        raw_mark = float(input(f"Enter mark for {student.getName()}: "))
        mark = m.floor(raw_mark * 10) / 10
        university.marks[cid][sid] = mark