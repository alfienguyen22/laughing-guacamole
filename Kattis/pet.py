ovr = []

for i in range(0, 5):
    inp = [int(j) for j in input().split()]
    points = sum(inp)
    ovr.append(points)

pos = ovr.index(max(ovr))

print(pos + 1, max(ovr))
