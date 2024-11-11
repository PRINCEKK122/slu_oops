class Student:
    def __init__(self, stuID):
        self._stuID = stuID
        self._name = ["", ""]
        self._testScores = []
        self._avg = 0.0

    def getID(self):
        return self._stuID
    
    def getName(self):
        return self._name
    
    def getTestScores(self):
        return self._testScores
    
    def getAvg(self):
        return self._avg
    
    def setName(self, firstName, lastName):
        self._name = [firstName, lastName]

    def addTest(self, testScore):
        self._testScores.append(testScore)
        self._calcAvg()

    def _calcAvg(self):
        self._avg = sum(self._testScores) / len(self._testScores)

    def __str__(self):
        result = f"Student: {self._stuID} {self._name[0]} {self._name[1]}"
        result += "\nTest Scores: "
        for test in self._testScores:
            result += f"{str(test)} "
        result += f"\nTest Average: {self.getAvg():.2f}\n"
        return result