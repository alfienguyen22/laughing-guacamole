
hand = list(input().split())
# List input
freq = [x[0] for x in hand]
# Read only the first character in list input

max = 1
# Set default value to 1 as the lowest frequency

length = len(freq)
for i in range(0, length - 1):
    count = 1
    for j in range(i + 1, length):
        if freq[i] == freq[j]:
            count += 1
            if max < count:
                max = count

print(max)