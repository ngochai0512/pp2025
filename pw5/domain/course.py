class Course:
    def __init__(self, courseID, courseName, credits):
        self.__courseID = courseID
        self.__courseName = courseName
        self.__credits = credits

    def getCourseID(self):
        return self.__courseID

    def getCourseName(self):
        return self.__courseName

    def getCredits(self):
        return self.__credits

    def __str__(self):
        return f"{self.__courseID} - {self.__courseName} ({self.__credits} credits)"