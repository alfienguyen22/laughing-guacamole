x = []
y = []

for i in range(0, 3):
    inp = [int(j) for j in input().split()]

    x.append(inp[0])
    y.append(inp[1])

    dup1 = {n for n in x if x.count(n) < 2}
    dup2 = {m for m in y if y.count(m) < 2}

print(*dup1, *dup2)

