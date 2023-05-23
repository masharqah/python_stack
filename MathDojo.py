class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for num in nums:
            self.result += num
        return self

    def subtract(self, *nums):
        for num in nums:
            self.result -= num
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
y=md.add(6).subtract(5,8,5).result
print(x)	
print(y)