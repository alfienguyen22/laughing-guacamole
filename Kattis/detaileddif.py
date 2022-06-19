def compare(lst1, lst2):
    lst1 = list(lst1)
    lst2 = list(lst2)
    ans = ''

    for i in range(0, len(lst1)):
        if lst1[i] == lst2[i]:
            ans = ans + '.'

        else:
            ans = ans + '*'

    return ans


n = int(input())

for j in range(0, n):
    lst1 = input()
    lst2 = input()
    ans = compare(lst1, lst2)
    print(lst1)
    print(lst2)
    print(ans)