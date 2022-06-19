n = int(input())
total = 0

for i in range(0, n):
    m = [int(j) for j in input().split()]
    total += sum(m)
    length = total - n + 1

print(length)