inp = [int(j) for j in input().split()]

king = 1 - inp[0]
queen = 1 - inp[1]
rooks = 2 - inp[2]
bishops = 2 - inp[3]
knights = 2 - inp[4]
pawns = 8 - inp[5]

print(king, queen, rooks, bishops, knights, pawns)