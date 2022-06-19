n = int(input())
inp = [int(j) for j in input().split()]

lst = [i for i in inp if i < 0]

total = sum(lst) * -1

print(total)

