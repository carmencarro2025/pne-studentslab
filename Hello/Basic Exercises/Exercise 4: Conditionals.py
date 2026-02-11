def get_letter(score):
    if score >= 9.0 and score <= 10.0:
        result = "A"
    elif score >= 7.0 and score <= 8.9:
        result = "B"
    elif score >= 5.0 and score <= 6.9:
        result = "C"
    elif score >= 3.0 and score <= 4.9:
        result = "D"
    elif score >= 0.0 and score <= 2.9
        result = "F"
    return result

if __name__ == "__main__":
    print(f"Score -> {get_letter(9.5)}")
    print(f"Score -> {get_letter(7.0)}")
    print(f"Score -> {get_letter(5.5)}")
    print(f"Score -> {get_letter(3.2)}")
    print(f"Score -> {get_letter(1.0)}")


