class Shape():
    def __init__(self):
        pass
    def Area(self):
        return 0 

class Rectangle():
    def __init__(self , length , width):
        super().__init__
        self.length = length
        self.width = width
    def Area(self):
        return self.width * self.length
    
audan = Rectangle(1 , 2)
print(audan.Area())