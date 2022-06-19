num = [int(j) for j in input().split()]


def reverse_number(number):
    if type(number) == int:
        return int(str(number)[::-1])


if reverse_number(num[0]) > reverse_number(num[1]):
    print(reverse_number(num[0]))

elif reverse_number(num[0]) < reverse_number(num[1]):
    print(reverse_number(num[1]))