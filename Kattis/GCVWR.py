inp = [int(j) for j in input().split()]
weight = [int(i) for i in input().split()]

lim = (inp[0]-inp[1]) * 0.9
total = sum(weight)
final = int(lim - total)

print(final)