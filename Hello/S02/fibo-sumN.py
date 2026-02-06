def fibosum(n):
    a = 0
    b = 1
    result = []
    for i in range(n + 1):
        result.append(a)
        c = a + b
        a = b
        b = c
    return sum(result)

print(f"Sum of the first 5 terms of the Fibonacci series: {fibosum(5)}")
print(f"Sum of the first 10 terms of the Fibonacci series: {fibosum(10)}")
