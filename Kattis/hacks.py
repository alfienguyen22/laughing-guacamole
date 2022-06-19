n = int(input())


for i in range(0, n):
    r, e, c = [int(x) for x in input().split()]
    total = e - c - r

    if total > 0:
        print("advertise")

    elif total == 0:
        print("does not matter")

    elif total < 0:
        print("do not advertise")