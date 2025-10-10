class Car:
    # def __new__(cls):
    #     pass

    count = 0

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        Car.count += 1

    def __str__(self):
        return f"[{self.model}, {self.color}, {self.year}]"
    
    @classmethod
    def GetCount(cls):
        return cls.count

    @staticmethod
    def About():
        print("This is a class for dealing with Cars")


#--------------------------------------------------------------------------


c1 = Car("Civic", "White", 2024)
c2 = Car("Camry", "Red", 2021)

print(c1)
print(c2)
print(c1.GetCount())
print(Car.GetCount())
Car.About()