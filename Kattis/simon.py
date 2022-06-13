n = int(input())
order = []

for i in range(0, n):
    item = input()

    if item.startswith("Simon says"):
        order.append(item[11:])

for i in order:
    print(i)

