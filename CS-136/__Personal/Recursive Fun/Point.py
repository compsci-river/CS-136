#
#River Sheppard
#Point
#

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def X(self):
        return self.x

    def Y(self):
        return self.y

    def str(self):
        s = ("("+str(self.x)+","+str(self.y)+")")
        return s
