from PublicFun import *
from Table import *

# This is the function in control of the billiards balls.

class Ball(object):

    def __init__(self, cx, cy, color, speed=0, dx=0, dy=0, mass = 5):
        self.cx = cx
        self.cy = cy
        self.color = color
        self.speed = speed
        self.dx = dx
        self.dy = dy
        self.r = 17
        self.mass = mass

        pass

    def collide(self, other, x = 0, y = 0):
        # collision engine
        # self should be the active ball

        if distance(self.cx, self.cy, other.cx, other.cy) < 2 * self.r:
            # if collide
            # other.cy += 4
            angle = getDirection(self.cx, self.cy, other.cx, other.cy, self.r)
            print(angle)
            setDirection(self, other, angle)
            setSpeed(self, other)
            pass

    def setDirection(self):

        pass




    def friction(self):

        self.speed -= .2

        pass


    def move(self):

        self.cx += self.dx * self.speed
        self.cy += self.dy * self.speed

        pass

    def draw(self, canvas):

        # canvas.create_line(self.cx,self.cy,self.cx + 1,self.cy + 1, fill = "black")

        canvas.create_oval(self.cx - self.r, self.cy - self.r,
                           self.cx + self.r, self.cy + self.r,
                           fill = self.color)
