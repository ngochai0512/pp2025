import math as m
import os
from datetime import datetime
from domain.student import Students
from domain.course import Course

# --- Data Loading Function (New) ---
def load_data(university):
    # Load Students
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    sid, name, dob_str = parts
                    dob = datetime.strptime(dob_str, "%d/%m/%Y")
                    university.students[sid] = Students(sid, name, dob)

    # Load Courses
    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    cid, cname, credits = parts
                    university.courses[cid] = Course(cid, cname, int(credits))

    # Load Marks
    if os.path.exists("marks.txt"):
        with open("marks.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    cid, sid, mark = parts
                    if cid not in university.marks:
                        university.marks[cid] = {}
                    university.marks[cid][sid] = float(mark)
    print("Data loaded successfully from text files.")

# --- Updated Input Functions ---

def add_student(university):
    sid = input("Enter student ID: ")
    name = input("Enter student's name: ")
    dob = datetime.strptime(input("Date of birth (dd/mm/yyyy): "), "%d/%m/%Y")
    
    # Add to memory
    university.students[sid] = Students(sid, name, dob)
    
    # Write to file immediately
    with open("students.txt", "a") as f:
        f.write(f"{sid},{name},{dob.strftime('%d/%m/%Y')}\n")

def add_course(university):
    cid = input("Enter course ID: ")
    cname = input("Enter course name: ")
    credits = int(input("Enter course credits: "))
    
    # Add to memory
    university.courses[cid] = Course(cid, cname, credits)
    
    # Write to file immediately
    with open("courses.txt", "a") as f:
        f.write(f"{cid},{cname},{credits}\n")

def input_marks(university):
    cid = input("Enter course ID to input marks: ")
    if cid not in university.courses:
        print("Course not found!")
        return

    if cid not in university.marks:
        university.marks[cid] = {}

    # Open file in append mode once for this batch
    with open("marks.txt", "a") as f:
        for sid, student in university.students.items():
            raw_mark = float(input(f"Enter mark for {student.getName()}: "))
            mark = m.floor(raw_mark * 10) / 10
            
            # Update memory
            university.marks[cid][sid] = mark
            
            # Write to file
            f.write(f"{cid},{sid},{mark}\n")