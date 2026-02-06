a = 0
b = 1
result = []
for i in range(11):
    result.append(a)
    c = a + b
    a = b
    b = c

for i in result:
 print(i, end=" ")


