if __name__ == "__main__":

    student = {
        "name": "Carlos",
        "age": 22,
        "subjects": ["PNE", "Networks", "Databases"],
        "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
    }

    print(f"Name: {student['name']}")
    print(f"Number of subjects: {len(student['subjects'])}")
    print(f"Enrolled in PNE: {is student['PNE'] in student['subjects']}")
