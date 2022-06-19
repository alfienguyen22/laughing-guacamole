n = int(input())
inp1 = [int(j) for j in input().split()]
inp2 = [int(k) for k in input().split()]

dup = list(set(inp1) & set(inp2))
rem = inp1.remove(dup)

print(rem)
