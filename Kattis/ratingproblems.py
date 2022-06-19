inp = [int(j) for j in input().split()]
score = []


for i in range(0, inp[1]):
    p = int(input())

    score.append(p)

current = sum(score)
remain = inp[0] - inp[1]

large = float((remain*3 + current) / inp[0])
small = float((remain*-3 + current) / inp[0])

print(small, large)
