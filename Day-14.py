class Difference:
    def __init__(self, a):
        self.__elements = a

# Add your code here
    def computeDifference(self):
        mx = max(self.__elements)
        mn = min(self.__elements)
        self.maximumDifference = mx - mn


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)