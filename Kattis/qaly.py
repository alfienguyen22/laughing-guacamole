n = int(input())
total = 0

for i in range(0, n):
    line = input()
    a, b = line.split()
    a = float(a)
    b = float(b)

    total += a*b

print(total)
