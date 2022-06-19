inp = [int(j) for j in input().split()]
llist = [inp[1], inp[0] - inp[1]]
wlst = [inp[2], inp[0] - inp[2]]

length = max(llist)
width = max(wlst)

volume = length * width * 4

print(volume)
