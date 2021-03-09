class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, id1, scores):
       Person.__init__(self, firstName, lastName, id1)
       self.scores = scores
       
    def calculate(self):
        avg1 = sum(self.scores)/len(self.scores)
        if 90<=avg1<=100:
            neg = 'O'
        elif 80<=avg1<=90:
            neg = 'E'
        elif 70<=avg1<=80:
            neg = 'A'
        elif 55<=avg1<=70:
            neg = 'P'
        elif 40<=avg1<=55:
            neg = 'D'
        else:
            neg = 'T'
        return neg
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())