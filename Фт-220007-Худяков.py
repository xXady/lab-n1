a = int(input())

b = int(input())

a1 = abs(a)

b1 = abs(b)

if a1 > b1:
    
    m = a1 - b1

else:

    m = b1 - a1

k = a/b

print(a + b)

print(a - b)

print(a * b)

print((a+b)/2)

print(m)

print("Частное чисел с точностью до сотых равно:",f"{k:.2f}")
