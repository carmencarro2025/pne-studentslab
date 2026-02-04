def fibonacci(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        c = a + b
        a = b
        b = c
    return result

def fibosum(n):
    k = fibonacci(n)
    return sum(k)

print(fibosum(5))
