# dictionary for this specific problem
phonedict = {
    "a": 2,
    "b": 22,
    "c": 222,
    "d": 3,
    "e": 33,
    "f": 333,
    "g": 4,
    "h": 44,
    "i": 444,
    "j": 5,
    "k": 55,
    "l": 555,
    "m": 6,
    "n": 66,
    "o": 666,
    "p": 7,
    "q": 77,
    "r": 777,
    "s": 7777,
    "t": 8,
    "u": 88,
    "v": 888,
    "w": 9,
    "x": 99,
    "y": 999,
    "z": 9999,
    " ": 0,
}

# taking in multiple x inputs
n = int(input())

List = []

for i in range(n):

    elem = input()

    List.append(elem)
    print(elem)

# print out the dictionary
# how should I get the program to read the input and return a number? Thank you!
for key, value in phonedict.items():
    print(key, ':', value)
