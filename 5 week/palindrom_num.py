A = int(input())
B = int(input())

for num in range(A, B + 1):
    if num % 10 == num // 1000 and \
            (num % 100) // 10 == (num // 100) % 10:
        print(num)
