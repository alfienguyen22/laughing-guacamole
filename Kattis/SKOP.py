n = int(input())


for i in range(0, n):
    inp = [int(j) for j in input().split()]

    lst = list(range(1, inp[1] + 1))
    even = [element * 2 for element in lst]
    odd = [element * 2 - 1 for element in lst]

    total = sum(lst)
    total_even = sum(even)
    total_odd = sum(odd)

    print(inp[0], total, total_odd, total_even)

