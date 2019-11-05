d, m, y = [int(e) for e in input().strip().split(' ')]

d1, m1, y1 = [int(e) for e in input().strip().split(' ')]

fine = int(0)

if int(y) > int(y1):
    fine = int(10000)

elif int(m) > int(m1) and int(y) == int(y1):
    fine = (int(m) - int(m1)) * 500

elif int(d) > int(d1) and int(m) == int(m1) and int(y) == int(y1):
    fine = (int(d) - int(d1)) * 15

print(fine)






