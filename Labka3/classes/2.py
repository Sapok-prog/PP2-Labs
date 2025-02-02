class Shape():
    def __init__(self):
        pass
    def Area(self):
        return 0 

class Square():
    def __init__(self , length):
        super().__init__
        self.length = length
    def Area(self):
        return self.length ** 2

square = Square(7)
print(square.Area())