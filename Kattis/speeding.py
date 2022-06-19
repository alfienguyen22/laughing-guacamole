import math

n = int(input())
count = 0
snap = []
speed = []

for i in range(0, n):
    item = input().split()
    for j in range(0, len(item)):
        item[j] = int(item[j])
    snap.append(item)

time = [item[0] for item in snap]
pos = [item[1] for item in snap]

for i in range(0, len(snap)-1):
    speed.append( (pos[i+1]-pos[i]) / (time[i+1]-time[i]) )

v = max(speed)
print(math.trunc(v))

