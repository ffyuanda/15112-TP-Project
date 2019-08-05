from PublicFun import *

# This is the function in control of the billiards balls.




class ball(object):
    def __init__(self, cx, cy, angle, force, color, speed = 1, dx = 0, dy = 0):

        self.cx = cx
        self.cy = cy
        self.angle = angle
        self.force = force
        self.color = color
        self.speed = speed
        self.dx = dx
        self.dy = dy
        self.r = 17
        self.mass = 6

        pass



    def collide(self, other):
        # collision engine

        if distance(self.cx, self.cy, other.cx, other.cy) < 2 * self.r:

            if self.cy < other.cy and self.cx < other.cx:
                # second dimension glancing collision
                print("YES")
                other.dx = self.dx
                other.dy = self.dy
                self.dx, self.dy = self.dy, -self.dx

            elif self.cy < other.cy and self.cx > other.cx:
                # first dimension glancing collision
                other.dx = self.dx
                other.dy = self.dy
                self.dx, self.dy = -self.dy, self.dx

            elif self.cy > other.cy and self.cx > other.cx:
                # forth dimension glancing collision
                other.dx = self.dx
                other.dy = self.dy
                self.dx, self.dy = self.dy, -self.dx

            elif self.cy > other.cy and self.cx < other.cx:
                # third dimension glancing collision
                other.dx = self.dx
                other.dy = self.dy
                self.dx, self.dy = -self.dy, self.dx

            elif self.cy == other.cy or self.cx == other.cx:
                other.dx = self.dx
                other.dy = self.dy

    def friction(self):
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
