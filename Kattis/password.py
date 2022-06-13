first = list(input())
second = list(input())

count = 0

for i in range (0, len(first)):
    if first[i] != second[i]:
        count +=1

print(2**count)


