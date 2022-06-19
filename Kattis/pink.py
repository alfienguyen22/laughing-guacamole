n = int(input())
count = 0

for i in range(0, n):
    colors = input().lower()
    if "rose" in colors or "pink" in colors:
        count +=1

if count !=0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")