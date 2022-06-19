data = int(input())
n = int(input())
total = data*(n+1)

for i in range(0, n):
   leftovers = int(input())
   total = total - leftovers

print(total)
