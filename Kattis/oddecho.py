n = int(input())
count = 0

for i in range(0, n):
    word = input()
    count = count + 1

    if count % 2 == 1:
        print(word)