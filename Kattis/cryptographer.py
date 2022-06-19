count = 0
word = input()

for i in range(0, len(word)):
    if i % 3 == 0 and word[i] != "P":
        count = count + 1

    elif i % 3 == 1 and word[i] != "E":
        count = count + 1

    elif i % 3 == 2 and word[i] != "R":
        count = count + 1

print(count)
