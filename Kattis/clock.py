item = []


data = input().split()
for j in range(0, len(data)):
    data[j] = int(data[j])

hour = data[0]
minute = data[1]

if (hour == 0) and (minute < 45):
    print(23, minute+15)

elif minute > 45:
    print(hour, minute-45)

elif minute < 45:
    print(hour-1, minute+15)

elif minute == 45:
    print(hour, minute-45)



