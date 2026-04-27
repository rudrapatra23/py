def get_student_data():
    students = []
    n = int(input("Enter the number of students: "))

    for i in range(n):
        print(f"\nEntering details for Student {i+1}")
        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        dept = input("Enter Department: ")
        marks = []
        for j in range(1, 6):
            m = float(input(f"Enter marks for subject {j}: "))
            marks.append(m)
        sorted_marks = tuple(sorted(marks, reverse=True))
        student_tuple = (name, (roll, dept), sorted_marks)
        students.append(student_tuple)

    return tuple(students)

def search_student(all_students):
    search_roll = input("\nEnter Roll No to search: ")
    found = False

    for student in all_students:
        name = student[0]
        roll, dept = student[1]
        marks = student[2]

        if roll == search_roll:
            print("\n--- Student Found ---")
            print(f"Name: {name}")
            print(f"Roll: {roll}")
            print(f"Department: {dept}")
            print(f"Marks (Descending): {marks}")
            found = True
            break

    if not found:
        print("Student with that roll number not found.")


data = get_student_data()
search_student(data)