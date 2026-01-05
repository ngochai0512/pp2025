def show_data(university):
    print("\n--- Students (sorted by GPA descending) ---")

    students_with_gpa = []
    for sid, student in university.students.items():
        gpa = university.calculate_gpa(sid)
        students_with_gpa.append((student, gpa))

    students_with_gpa.sort(key=lambda x: x[1], reverse=True)

    for student, gpa in students_with_gpa:
        print(f"{student} | GPA: {gpa:.2f}")

    print("\n--- Courses ---")
    for course in university.courses.values():
        print(course)

    print("\n--- Marks ---")
    for cid, mark_data in university.marks.items():
        print(f"Course: {university.courses[cid].getCourseName()}")
        for sid, mark in mark_data.items():
            print(f"  {university.students[sid].getName()}: {mark}")