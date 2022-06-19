import math

inp = [int(j) for j in input().split()]
x = math.sqrt(inp[1] ** 2 + inp[2] ** 2)

for i in range(0, inp[0]):
    length = int(input())

    if x >= length:
        print("DA")

    else:
        print("NE")



