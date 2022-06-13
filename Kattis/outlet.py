n = int(input())
spots = []

for i in range(0, n):
    item = input().split()
    for j in range(0, len(item)):
        item[j] = int(item[j])
    spots.append(item)

    total = sum(item) - 2 * item[0] + 1

    print(total)
