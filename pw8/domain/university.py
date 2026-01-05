import numpy as np
from domain.student import Students
from domain.course import Course

class University:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    def calculate_gpa(self, student_id):
        marks = []
        credits = []

        for cid, course_marks in self.marks.items():
            if student_id in course_marks:
                marks.append(course_marks[student_id])
                credits.append(self.courses[cid].getCredits())

        if not marks:
            return 0.0

        marks_arr = np.array(marks)
        credits_arr = np.array(credits)

        return float(np.sum(marks_arr * credits_arr) / np.sum(credits_arr))