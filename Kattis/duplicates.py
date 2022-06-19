def checkDuplicates(inp):
    if len(inp) == len(set(inp)):
        return False
    else:
        return True


inp = list(input().split())

result = checkDuplicates(inp)

if result:
    print("no")

else:
    print("yes")


