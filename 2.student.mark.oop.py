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
    def __init__(self, courseID, courseName):
        self.__courseID = courseID
        self.__courseName = courseName
    
    def getCourseID(self):
        return self.__courseID
    
    def getCourseName(self):
        return self.__courseName
    
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

        course = Course(cid, cname)
        self.__courses[cid] = course

    def input_mark(self):
        course_id = input("Enter course ID to input marks: ")

        if course_id not in self.__courses:
            print("Course not found!")
            return

        self.__marks[course_id] = {}

        for sid, student in self.__students.items():
            mark = float(input(f"Enter mark for {student.getID()} ({student.getName()}): "))
            self.__marks[course_id][sid] = mark

    def show_data(self):
        print("\n--- Students ---")
        for student in self.__students.values():
            print(student)

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