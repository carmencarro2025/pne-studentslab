def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(f"5th Fibonacci element {fibo(5)}")
print(f"10th Fibonacci element {fibo(10)}")
print(f"15th Fibonacci element {fibo(15)}")

