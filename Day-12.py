class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber


class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores = scores

    def calculate(self):
        a = int(0)
        a = (sum(self.scores)) / len(self.scores)

        if a >= 90 and a <= 100:
            return 'O'

        elif a >= 80 and a < 90:
            return 'E'

        elif a >= 70 and a < 80:
            return 'A'

        elif a >= 55 and a < 70:
            return 'P'

        elif a >= 40 and a < 55:
            return 'D'

        elif a < 40:
            return 'T'



line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input())  # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()