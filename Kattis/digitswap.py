num = int(input())


def reverse_number(number):
    if type(number) == int:
        return int(str(number)[::-1])


print(reverse_number(num))