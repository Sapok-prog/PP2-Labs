class Point():
    def __init__(self):
        pass
    def show(self):
        self.x = int(input("fill x "))
        self.y = int(input("fill y "))
        print(f'coordinates of the point : ({self.x} ; {self.y})')
    def move(self):
        self.new_x = int(input("fill new x "))
        self.new_y = int(input("fill new y "))
        print(f'changed coordinates of the point : ({self.new_x} ; {self.new_y})')
    def dist(self):
        print(f'distance between 2 points : {((self.x - self.new_x)**2 + (self.y - self.new_y)**2)**(1/2)}')
        self.x = self.new_x
        self.y = self.new_y

start = Point()
start.show()
start.move()
start.dist()
