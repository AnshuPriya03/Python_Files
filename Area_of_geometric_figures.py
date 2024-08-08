import math

class Shape:
    def __init__(self):
     self.area=0
     self.name=" "
    def showArea(self):
        print("The area of the ",self.name," is" ,self.area," units")

class Circle(Shape):
   def __init__(self,radius):
      self.area=0
      self.name="Circle"
      self.radius=radius
   def calcArea(self):
      self.area = math.pi * self.radius * self.radius
      
class Rectangle(Shape):
   def __init__(self,lenght,breadth):
      self.area=0
      self.name="Rectangle"
      self.length=lenght
      self.breadth=breadth
   def calcArea(self):
      self.area=self.length*self.breadth


class Triangle(Shape):
   def __init__(self,base,height):
      self.area=0
      self.name="Triangle"
      self.base=base
      self.height=height
   def calcArea(self):
      self.area=self.base*self.height/2

c1=Circle(5)
c1.calcArea()
c1.showArea()

c2=Rectangle(5,4)
c2.calcArea()
c2.showArea()

c3=Triangle(3,4)
c3.calcArea()
c3.showArea()