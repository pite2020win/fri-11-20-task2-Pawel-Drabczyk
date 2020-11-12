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

'''
class student:
  def __init__(self, n, sn):
    self.name = n
    self.surname = sn
    self.grades = []
    self.presences = []
  
  def addGrade(self,g):
    self.grades.append(g)

  def addPresence(self,p):
    self.presences.append(p)

  def getStudentGradeAverage(self):
    return float(sum(self.grades))/len(self.grades)
  
  def getStudentAttendance(self):
    numerator = 0
    for i in range len(self.presences): 
      if self.presences[i]:
        numerator = numerator + 1 
    return float(numerator)/len(self.presences)

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
    return float(numerator)/len(self.listOfStudents)

  def getClassAverageGrade(self):
    numerator = 0
    for i in range(len(self.listOfStudents))
      numerator = numerator + self.listOfStudents[i].getStudentAttendance()
    return float(numerator)/len(self.listOfStudents)

class School:
  def __init__(self, n):
    self.name = n
    self.listOfClasses = []

  def addClass(self, c)
    self.listOfClasses.append(c)
'''

import random
import logging
import json
import statistics as stat

def calculateAverage(dict):
  averages = []
  if "schoolsList" in dict:
    for school in dict["schoolList"]:
      averages.append( calculateAverage(school) )
  elif "clasList" in dict:
    for clas in dict["clasList"]:
      averages.append( calculateAverage(clas) )
  elif "studentList" in dict:
    for student in dict["studentList"]:
      averages.append( calculateAverage(student) )
  elif "grades" in dict:
    averages = dict["grades"]
  else:
    logging.warning(f'Watch out! Wrong type of dictonary! ')
    return -1
  return stat.mean(averages)

if __name__ == '__main__':
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)
  nStudents = 15

################## creating dictionaries ##########################

  randomNames = ["Florentyna", "Agnieszka", "Ewelina", "Edyta", "Klaudia", "Aniela", "Paula", "Angelika", "Julianna", "Adrianna", "Gabriela", "Matylda", "Jolanta", "Beata","Weronika"]
  randomSurnames = ["Makowska", "Lewandowska", "Jakubowska", "Walczak", "Gajewska", "Zawadzaka", "Baran", "Przybylska", "Wojciechowska", "Chmielewska", "Pawlak", "Kolodziej", "Jaworska", "Zakrzewska", "Sobczak" ]

  studentListTemp = []
  for i in range(nStudents):
    student = {
      "name" : randomNames[i],
      "surname" : randomSurnames[i],
      "grades" : random.choices([1,2,3,4,5],k=5),
      "presences" : random.choices([True,False], k=5)
    }
    studentListTemp.append(student)

  clas1 = {
    "name" : "1a",
    "studentList" : [studentListTemp[0], studentListTemp[1], studentListTemp[2], studentListTemp[3], studentListTemp[4], studentListTemp[5], studentListTemp[6]]
  }
  clas2 = {
    "name" : "2a",
    "studentList" : [studentListTemp[7], studentListTemp[8], studentListTemp[9] ]
  }
  clas3 = {
    "name" : "1a",
    "studentList" : [studentListTemp[10], studentListTemp[11], studentListTemp[12], studentListTemp[13], studentListTemp[14] ]
  }

  school1 = {
    "name" : "Liceum numer 1",
    "clasList" : [clas1, clas2]
  }
  school2 = {
    "name" : "Liceum numer 2",
    "clasList" : [clas3]
  }

  schools = {
    "name" : "Zespol szkol licealnych w krakowie",
    "schoolList" : [school1, school2]
  }

################ showcases ###########################

  if logger.level == logging.DEBUG:
    gradesTemp = studentListTemp[1]["grades"]
    presencesTemp = studentListTemp[1]["presences"]
    logging.debug(f"studentList[1].grades = {gradesTemp} studentListTemp[1].presences = {presencesTemp}")

  testAverageStudent = calculateAverage( schools["schoolList"][0]["clasList"][0]["studentList"][0] )
  logging.info(f'Testing calculateAverage function for student1  from clas1 from school1. Grades: {schools["schoolList"][0]["clasList"][0]["studentList"][0]["grades"]}, average: {testAverageStudent}')

  testAveragesClas = []
  for stud in schools["schoolList"][0]["clasList"][0]["studentList"]:
    testAveragesClas.append( calculateAverage(stud) )
  testAverageClas = calculateAverage(schools["schoolList"][0]["clasList"][0])
  logging.info(f'Testing calculateAverage function for clas1 from school1. Averages of individual students: {testAveragesClas}, average of the clas {schools["schoolList"][0]["clasList"][0]["name"]}: {testAverageClas:.2f}')

  testAveragesSchool = []
  for clas in schools["schoolList"][0]["clasList"]:
    testAveragesSchool.append( calculateAverage(clas) )
  testAverageSchool = calculateAverage(schools["schoolList"][0])
  logging.info(f'Testing calculateAverage function for school1. Averages of individual clases: {testAveragesSchool}, average of the school  {schools["schoolList"][0]["name"]} : {testAverageSchool:.2f}')

################### writing to a file ###############################

  with open('schools.txt', 'w') as outFile:
    json.dump(schools, outFile)

  with open('schools.txt') as inputFile:
    schoolsFromJson = json.load(inputFile)

################## more showcases ###################################

  testAveragesSchool = []
  for clas in schoolsFromJson["schoolList"][0]["clasList"]:
    testAveragesSchool.append( calculateAverage(clas) )
  testAverageSchool = calculateAverage(schoolsFromJson["schoolList"][0])
  logging.info(f'Testing writing to and reading from json file. Once again testing calculateAverage function for school1 (after rereading from json file). \n Averages of individual clases: {testAveragesSchool}, average of the school  {schoolsFromJson["schoolList"][0]["name"]} : {testAverageSchool:.2f}')
