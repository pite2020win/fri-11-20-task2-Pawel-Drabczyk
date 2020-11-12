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
      "grades" : random.choices([1,2,3,4,5],k=5)
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

  studName = 'Agnieszka'
  studSurname = 'Lewandowska'
  clasName =  '1a'
  schoolName = 'Liceum numer 1'
  schoolsName = 'Zespol szkol licealnych w krakowie'
  if schoolsName == schools["name"]:
    for s in schools['schoolList']:
      if s["name"] == schoolName:
        clases = s['clasList']
        for c in clases:
          if c['name'] == clasName:
            for stud in c['studentList']:
              if stud['name'] == studName and stud['surname'] == studSurname:
                searchedStudent = stud

  searchedStudentGrades = searchedStudent['grades']
  searchedStudentAverage = calculateAverage(searchedStudent)
  logging.info(f'Searching for the grades of the student with\nname: {studName}\nsurname: {studSurname}\nclasName: {clasName}\nschoolName: {schoolName}\nschoolsName: {schoolsName}\nResults:\ngrades: {searchedStudentGrades}\naverage: {searchedStudentAverage}')

  if schoolsName == schools["name"]:
    for s in schools['schoolList']:
      if s["name"] == schoolName:
        clases = s['clasList']
        for c in clases:
          if c['name'] == clasName:
            searchedClas = c

  searchedClasAverages = []
  for stud in searchedClas['studentList']:
    searchedClasAverages.append( calculateAverage(stud) )
  searchedClasAverage = calculateAverage(searchedClas)
  logging.info(f'Searching for the avera of the clas with\nclasName: {clasName}\nschoolName: {schoolName}\nschoolsName: {schoolsName}\nResults:\naverages of the students: {searchedClasAverages}\naverage of the clas: {searchedClasAverage}')

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
