n = int(input())
result = 0

for i in range(0, n):
    inp = input()
    last_digit_str = inp[-1]
    num = inp[:-1]

    power = int(last_digit_str)
    base = int(num)
    result += base**power

print(result)
