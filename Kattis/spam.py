inp = input()
length = len(inp)
count1 = 0
count2 = 0

for i in inp:
      if(i.islower()):
            count1 = count1+1
      elif(i.isupper()):
            count2 = count2+1

c = inp.count("_")
symbols = 1 - c / length - count1 / length - count2 / length

print(c / length)
print(count1 / length)
print(count2 / length)
print(symbols)