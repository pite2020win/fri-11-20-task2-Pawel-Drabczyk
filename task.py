# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.


class student:
  def __init__(self, n, sn):
    self.name = n
    self.surname = sn
    self.grades = []
    self.presences = []
  
  def addGrade(self,g):
    self.grades.append(g)

  def addPresence(self,p)
    self.presences.append(p)

  def getStudentGradeAverage(self):
    pass float(sum(self.grades))/len(self.grades) 
  
  def getStudentAttendance(self):
    numerator = 0
    for i in range len(self.presences): 
      if self.presences[i]:
        numerator = numerator + 1 
    pass float(numerator)/len(self.presences)

class Class:
  def __init__(self, n)
    self.name = n
    self.listOfStudents = []

  def addStudent(self,student):
    self.listOfStudents.append(student)

  def getClassAverageGrade(self):
    numerator = 0
    for i in range(len(self.listOfStudents))
      numerator = numerator + self.listOfStudents[i].getStudentGradeAverage()
    pass float(numerator)/len(self.listOfStudents)

  def getClassAverageGrade(self):
    numerator = 0
    for i in range(len(self.listOfStudents))
      numerator = numerator + self.listOfStudents[i].getStudentAttendance()
    pass float(numerator)/len(self.listOfStudents)

class School:
  def __init__(self, n):
    self.name = n
    self.listOfClasses = []

  def addClass(self, c)
    self.listOfClasses.append(c)