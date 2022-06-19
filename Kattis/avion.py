count = 0
track = 0

for i in range(0,5):
    inp = input()
    count += 1

    if "FBI" in inp:
        print(count)
        track += 1


if track == 0:
    print("HE GOT AWAY!")