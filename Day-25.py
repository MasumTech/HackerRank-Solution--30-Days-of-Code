import math


def is_prime(a):
    if a == 1:
        return False
    else:
        root_a = math.sqrt(a)
        root_a = int(root_a)
        for i in range(2, root_a + 1):
            if (a % i == 0 and i != a):
                return False
        return True


n = int(input())
for _ in range(n):
    a = int(input())
    if is_prime(a):
        print("Prime")
    else:
        print("Not prime")

