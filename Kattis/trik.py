inp = list(input())

def swap_orderA(order):
    order[0], order[1] = order[1], order[0]

def swap_orderB(order):
    order[1], order[2] = order[2], order[1]

def swap_orderC(order):
    order[0], order[2] = order[2], order[0]

order = [1,0,0]

for item in inp:
    if item == "A":
        swap_orderA(order)
    elif item == "B":
        swap_orderB(order)
    elif item == "C":
        swap_orderC(order)

print(order.index(1) +1)