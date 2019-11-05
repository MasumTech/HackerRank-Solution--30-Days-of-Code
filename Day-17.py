#Write your code here
class Calculator:
    def power(self, n, p):
          if int(n)>=0 and int(p)>=0:
               return n**p
          else:
            raise Exception('n and p should be non-negative')


myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e    