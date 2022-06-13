price = float(input())
n = int(input())
cost = 0

for i in range (0, n):
    a, b = [float(x) for x in input().split()];
    cost += a*b*price

print(cost)