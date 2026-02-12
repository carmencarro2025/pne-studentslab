if __name__ == "__main__":

    student = {
        "name": "Carlos",
        "age": 22,
        "subjects": ["PNE", "Networks", "Databases"],
        "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
    }

    print(f"Name: {student['name']}")
    print(f"Number of subjects: {len(student['subjects'])}")
    print(f"Enrolled in PNE: {'PNE' in student['subjects']}")
    print(f"Databases grade: {student['grades']["Databases"]}")
    total_grades = 0
    subjects = 0
    for subject, grade in student['grades'].items():
        total_grades = total_grades + grade
        subjects = subjects + 1
    print(f"Average grade: {round(total_grades / subjects, 2)}")
    print("Subject grades:")
    for sub, grade in student['grades'].items():
        print(f"    {sub}: {grade}")
