import numpy as np
import math as m

from datetime import datetime

class Students:
    def __init__(self, studentID, name, dob):
        self.__studentID = studentID
        self.__name = name
        self.__dob = dob
    
    def getID(self):
        return self.__studentID
    
    def getName(self):
        return self.__name
    
    def getDOB(self):
        return self.__dob

    def set_name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return f"{self.__studentID} - {self.__name}, DOB: {self.__dob.strftime('%d/%m/%Y')}"

class Course:
    def __init__(self, courseID, courseName, credits):
        self.__courseID = courseID
        self.__courseName = courseName
        self.__credits = credits
    
    def getCourseID(self):
        return self.__courseID
    
    def getCourseName(self):
        return self.__courseName

    def getCredits(self):
        return self.__credits
    
    def __str__(self):
        return f"{self.__courseID} - {self.__courseName}"
    
class University:
    def __init__(self):
        self.__students = {}
        self.__courses = {}
        self.__marks = {}
    
    def add_student(self):
        sid = input("Enter student ID: ")
        name = input("Enter student's name: ")
        dob_input = input("Date of birth (dd/mm/yyyy): ")
        dob = datetime.strptime(dob_input, "%d/%m/%Y")

        student = Students(sid, name, dob)
        self.__students[sid] = student 

    def add_course(self):
        cid = input("Enter course ID: ")
        cname = input("Enter course's name: ")
        credits = int(input("Enter course credits: "))

        course = Course(cid, cname, credits)
        self.__courses[cid] = course

    def input_mark(self):
        course_id = input("Enter course ID to input marks: ")

        if course_id not in self.__courses:
            print("Course not found!")
            return

        self.__marks[course_id] = {}

        for sid, student in self.__students.items():
            raw_mark = float(input(f"Enter mark for {student.getID()} ({student.getName()}): "))
            mark = m.floor(raw_mark * 10) / 10
            self.__marks[course_id][sid] = mark

    def calculate_gpa(self, student_id):
        marks = []
        credits = []

        for cid, course_marks in self.__marks.items():
            if student_id in course_marks:
                marks.append(course_marks[student_id])
                credits.append(self.__courses[cid].getCredits())

        if not marks:
            return 0.0

        marks_arr = np.array(marks)
        credits_arr = np.array(credits)

        return float(np.sum(marks_arr * credits_arr) / np.sum(credits_arr))

    def show_data(self):
        print("\n--- Students (sorted by GPA descending) ---")
        students_with_gpa = []
        for sid, student in self.__students.items():
            gpa = self.calculate_gpa(sid)
            students_with_gpa.append((student, gpa))

        students_with_gpa.sort(key=lambda x: x[1], reverse=True)

        for student, gpa in students_with_gpa:
            print(f"{student} | GPA: {gpa:.2f}")

        print("\n--- Courses ---")
        for course in self.__courses.values():
            print(course)

        print("\n--- Marks ---")
        for cid, mark_data in self.__marks.items():
            print(f"Course: {self.__courses[cid].getCourseName()}")
            for sid, mark in mark_data.items():
                print(f"  Student {self.__students[sid].getName()}: {mark}")
        print("----------------")

# Main Program
system = University()

numOfStudents = int(input("Enter number of students: "))
for _ in range(numOfStudents):
    system.add_student()

numOfCourses = int(input("Enter number of courses: "))
for _ in range(numOfCourses):
    system.add_course()

system.input_mark()
system.show_data()