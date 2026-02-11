def classify_triangle(a, b, c):
    if a == b == c:
        result = "equilateral"
    elif a == b or b == c or c == a:
        result = "isosceles"
    else:
        result = "scalene"
    print(f"classify_triangle({a, b, c}) = {result}")

if __name__ == "__main__":
    classify_triangle(5, 5, 5)
    classify_triangle(3, 3, 4)
    classify_triangle(3, 4, 5)
