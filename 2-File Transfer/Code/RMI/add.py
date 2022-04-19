import json
class Add:
    def __init__(self, num1, num2, sum):
        self.num1 = num1
        self.num2 = num2
        self.sum = sum

    def getSum(self):
        return self.sum

    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def findSum(self):
        self.sum = self.num1 + self.num2

    def getJson(self):
        return {"num1": self.num1, "num2": self.num2, "sum":self.sum}
    
    def fromJson(self, json):
        self.num1 = int(json["num1"])
        self.num2 = int(json["num2"])
        self.sum = int(json["sum"])
        return self
