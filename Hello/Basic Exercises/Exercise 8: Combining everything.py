def average(grades):
    return round(sum(grades) / len(grades), 1)

def get_status(avg):
    if avg >= 5.0:
        result = "PASS"
    else:
        result = "FAIL"
    return result


if __name__ == "__main__":

    students = [
        {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
        {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
        {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
        {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
        {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
    ]

    passed = 0
    failed = 0
    for student in students:
        avg = average(student['grades'])
        status = get_status(avg)
        print(f"{student['name']}: {avg} -> {status}")
        if status == "PASS":
            passed += 1
        elif status == "FAIL":
            failed += 1
    print(f"Results: {passed} passed, {failed} failed.")



