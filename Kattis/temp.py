n = int(input())
inp = [int(j) for j in input().split(" ", n-1)]

count = 0

for i in range(0, n):
    if inp[i] < 0:
        count = count + 1

print(count)