total = []

while True:
    item = []
    n = int(input())
    if n < 0:
        break

    for i in range(0, n):
        data = input().split()
        for j in range(0, len(data)):
            data[j] = int(data[j])
        item.append(data)

    velo = [item[0] for item in item]
    time = [item[1] for item in item]

    dist = (velo[0] * time[0])

    for i in range(1, len(item)):
        dist = velo[i] * (time[i] - time[i - 1]) + dist

    total.append(dist)

    print(total[-1], "miles")


