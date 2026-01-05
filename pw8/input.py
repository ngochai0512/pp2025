import math as m
import pickle
import os
import threading
import zipfile
import time
from datetime import datetime
from domain.student import Students
from domain.course import Course

# --- Background Persistence Logic ---

def _save_worker(university):
    """
    Worker function to be run in a separate thread.
    Handles Pickling -> Compressing -> Cleanup.
    """
    try:
        print("\n[Background Thread] Starting data persistence...")
        
        # 1. Pickle the data
        with open("university.pkl", "wb") as f:
            pickle.dump(university, f)
        
        # 2. Compress into zip
        with zipfile.ZipFile("students.dat", 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write("university.pkl")

        # 3. Cleanup raw pickle file
        if os.path.exists("university.pkl"):
            os.remove("university.pkl")
            
        print("[Background Thread] Data successfully compressed and saved to students.dat")
        
    except Exception as e:
        print(f"[Background Thread] Error during saving: {e}")

def save_data(university):
    """
    Initiates the saving process in a background thread.
    """
    # Create a thread targeting the worker function
    # args=(university,) passes the object to the thread
    thread = threading.Thread(target=_save_worker, args=(university,))
    
    # Starting the thread
    thread.start()
    
    print("Background save process initiated.")
    return thread

def load_data():
    """
    Deserializes the University object from a binary file.
    (Kept synchronous as data is usually needed immediately on startup)
    """
    if os.path.exists("university.pkl"):
        # If raw pickle exists (e.g. from a crash), load it
        try:
            with open("university.pkl", "rb") as f:
                return pickle.load(f)
        except:
            return None
    return None

# --- Standard Input Functions ---

def add_student(university):
    sid = input("Enter student ID: ")
    name = input("Enter student's name: ")
    try:
        dob_str = input("Date of birth (dd/mm/yyyy): ")
        dob = datetime.strptime(dob_str, "%d/%m/%Y")
        university.students[sid] = Students(sid, name, dob)
    except ValueError:
        print("Invalid date format. Student not added.")

def add_course(university):
    cid = input("Enter course ID: ")
    cname = input("Enter course name: ")
    try:
        credits = int(input("Enter course credits: "))
        university.courses[cid] = Course(cid, cname, credits)
    except ValueError:
        print("Invalid credits. Course not added.")

def input_marks(university):
    cid = input("Enter course ID to input marks: ")
    if cid not in university.courses:
        print("Course not found!")
        return

    if cid not in university.marks:
        university.marks[cid] = {}

    for sid, student in university.students.items():
        try:
            raw_mark = float(input(f"Enter mark for {student.getName()}: "))
            # Floor to 1 decimal place
            mark = m.floor(raw_mark * 10) / 10
            university.marks[cid][sid] = mark
        except ValueError:
            print("Invalid mark entered.")