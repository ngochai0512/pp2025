import math as m
import pickle
import os
from datetime import datetime
from domain.student import Students
from domain.course import Course

# --- Pickle Persistence Functions ---

def save_data(university):
    """
    Serializes the University object to a binary file.
    """
    with open("university.pkl", "wb") as f:
        pickle.dump(university, f)
    print("Data serialized to university.pkl")

def load_data():
    """
    Deserializes the University object from a binary file.
    Returns a new University object if file exists, else None.
    """
    if os.path.exists("university.pkl"):
        try:
            with open("university.pkl", "rb") as f:
                university = pickle.load(f)
            print("Data successfully loaded from pickle file.")
            return university
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    return None

# --- Standard Input Functions (Cleaned) ---

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

    if cid not in university.marks:
        university.marks[cid] = {}

    for sid, student in university.students.items():
        raw_mark = float(input(f"Enter mark for {student.getName()}: "))
        mark = m.floor(raw_mark * 10) / 10
        university.marks[cid][sid] = mark