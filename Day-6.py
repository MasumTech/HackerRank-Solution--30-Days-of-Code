n = int(input())

for i in range(0, n):
    a = input()
    for j in range(0, len(a)):
        if j % 2 == 0:
            print(a[j], end='')

    print(" ", end='')

    for j in range(0, len(a)):
        if j % 2 == 1:
            print(a[j], end='')
    print('')
