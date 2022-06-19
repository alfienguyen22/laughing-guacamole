n = int(input())

for i in range(0,n):
    m = int(input())
    cities = []

    for j in range(0,m):
        cities.append(input())

    num = len(set(cities))

    print(num)