n = int(input())


for i in range(0, n):
    days = 0
    lst = [int(j) for j in input().split()]

    for num in range(0, lst[1]):
        days = days + num

    total = days + 2*lst[1]

    print(lst[0], total)
