problems = input().split(';')
sum = 0
count = 0

for i in range(0, len(problems)):
    if "-" in problems[i]:
        a, b = [int(x) for x in problems[i].split("-")]

        sum += b-a+1;

    else:
        count += 1;

print(sum+count)