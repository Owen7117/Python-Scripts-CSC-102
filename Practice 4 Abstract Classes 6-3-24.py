#Practice 4: Abstract Classes
#6/3/24

import abc #import Abstract Base Clases

class Polygon(metaclass = abc.ABCMeta):
    def __init__(self, shape):
        self.shape = shape
        
    @abc.abstractmethod
    def area(self):
        pass
    
class Triangle(Polygon):
    def area(self, base, hight):
        if base < 0 or hight < 0:
            return ValueError("Base and or Hight can not be negative")
        else:
            return float(.5*base*hight)
    
class Parallelogram(Polygon):
    def area(self, base, hight):
        if base < 0 or hight < 0:
            return ValueError("Base and or Hight cannot be negative")
        else:
            return (base*hight)

class Trapezoid(Parallelogram):
    def area(self, base1, base2, height):
        if base1 < 0 or base2 < 0 or height < 0:
            return ValueError("Base and or Hight can not be negative")
        else:
            return float(.5*height*(base1 + base2))


##MAIN PROGRAM##

T= Triangle(Triangle)
P= Parallelogram(Parallelogram)
Trp = Trapezoid(Trapezoid)
print(T.area(-1,15))
print(P.area(4,5))
print(Trp.area(4,6,10))


#Question 1
#If the base or hight is 0 then the area of the shape should be 0

#Question 2
#If the base or high is less than zero then an error statement is printed

#Question 3
#If you try to creat a polygon object there should be a type error
