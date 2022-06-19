n = int(input())

for i in range(0, n):
    k = int(input())
    inp = [int(j) for j in input().split()]

    optimal = max(inp) - min(inp)

    dist = 2 * optimal

    print(dist)
