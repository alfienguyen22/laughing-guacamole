import math

inp = [int(j) for j in input().split()]

rad = math.pi*inp[1]/180
length = inp[0]/math.sin(rad)
final = math.ceil(length)

print(final)

