cards = input()

count = 1;

for i in range (0,len(cards)):
    for j in range(i+1,len(cards)):
        if (cards[i] == cards[j] and cards[i]!=''):
            count = count + 1;
            cards = cards[:j] + '0'+ cards[j+1:];

if(count>1):
    print(0)
else:
    print(1)




