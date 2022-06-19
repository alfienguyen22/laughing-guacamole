inp = input().lower()
count = 0


for i in inp:
    if i == "a":
        count = count + 1
    if i == "e":
        count = count + 1
    if i == "i":
        count = count + 1
    if i == "o":
        count = count + 1
    if i == "u":
        count = count + 1

print(count)
