n = int(input())
lst = []

if n % 2 == 1:
    print("still running")

else:
    for i in range(0, n):
        x = int(input())

        lst.append(x)

        odd = {j for j in lst if lst.index(j) % 2 == 0}
        even = {k for k in lst if lst.index(k) % 2 == 1}

    ans = sum(even) - sum(odd)

    print(ans)





