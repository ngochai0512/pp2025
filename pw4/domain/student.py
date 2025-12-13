from datetime import datetime

class Students:
    def __init__(self, studentID, name, dob):
        self.__studentID = studentID
        self.__name = name
        self.__dob = dob

    def getID(self):
        return self.__studentID

    def getName(self):
        return self.__name

    def getDOB(self):
        return self.__dob

    def __str__(self):
        return f"{self.__studentID} - {self.__name}, DOB: {self.__dob.strftime('%d/%m/%Y')}"