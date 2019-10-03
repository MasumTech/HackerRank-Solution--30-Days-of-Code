n = int(input())
mydict = {}

for i in range(n):
    r1 = input().split(' ')
    a, b = r1
    mydict[a] = b

while True:
    try:
        c = str(input())

        if c in mydict:
            print(c + '=' + mydict[c])
        else:
            print('Not found')
    except:
        break