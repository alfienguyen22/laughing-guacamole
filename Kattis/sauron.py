eye = input()

pos1 = len(eye) / 2
pos2 = eye.find("(") + 1

if pos1 == pos2:
    print("correct")

else:
    print("fix")