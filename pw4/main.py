from domain import University
from input import add_student, add_course, input_marks
from output import show_data

def main():
    system = University()

    n = int(input("Enter number of students: "))
    for _ in range(n):
        add_student(system)

    m = int(input("Enter number of courses: "))
    for _ in range(m):
        add_course(system)

    input_marks(system)
    show_data(system)

if __name__ == "__main__":
    main()