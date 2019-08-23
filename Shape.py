
class Shape():

    def __init__(self,length, hight):
        self.length = length
        self.hight = hight

    def area(self):
        print "Use child method"




class rect(Shape):

    def __init__(self,length,height):
        return Shape(length,height)


    def area(self):
        return self.shapeObj.length * self.shapeObj.hight


if __name__ == '__main__':

    rectObj = rect(4,5)












