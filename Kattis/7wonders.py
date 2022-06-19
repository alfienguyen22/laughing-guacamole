inp = input()

t = inp.count("T")
c = inp.count("C")
g = inp.count("G")

lst1 = [t, c, g]
lst1.sort()
n = lst1[0]

point = t**2 + c**2 + g**2 + n*7

print(point)