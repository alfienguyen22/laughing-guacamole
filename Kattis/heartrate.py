n = int(input())


for i in range (0, n):
    a, b = [float(x) for x in input().split()]
    true_hr = 60*a/b
    min_hr = true_hr-60/b
    max_hr = true_hr+60/b
    print(min_hr,true_hr,max_hr)