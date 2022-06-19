inp = [int(j) for j in input().split()]
count = 1

for j in range(0, inp[2]):
    if count % inp[0] == 0 and count % inp[1] == 0:
        print("Fizzbuzz")

    elif count % inp[0] == 0:
        print("Fizz")

    elif count % inp[1] == 0:
        print("Buzz")

    else:
        print(count)

    count = count + 1
