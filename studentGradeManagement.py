from datetime import datetime

students = {}
courses = {}
marks = {}

numOfStudents = int(input("Enter number of students: "))

for _ in range(numOfStudents):
    sid = input("Enter student ID: ")
    sname = input("Enter student's name: ")
    dob_input = input("Date of birth (dd/mm/yyyy): ")

    # Convert string to datetime object
    dob = datetime.strptime(dob_input, "%d/%m/%Y")

    students[sid] = {
       "student's name": sname,
       "dob": dob
   }

numOfCourses = int(input("Enter number of courses: "))
for _ in range(numOfCourses):
    cid = input("Enter course ID: ")
    cname = input("Enter course's name: ")

    courses[cid] = {
        "course name": cname
    }

course_id = input("Enter course ID to input marks: ")
marks[course_id] = {}

if course_id in courses:
    for sid in students:
        mark = float(input(f"Enter mark for student {sid}: "))
        marks[course_id][sid] = mark
else: 
    print("no course found")

print(students)
print(courses)
print(marks)


