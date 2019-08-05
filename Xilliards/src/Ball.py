from PublicFun import *

# This is the function in control of the billiards balls.




class ball(object):
    def __init__(self, cx, cy, angle, force, color, speed = 3, dx = 0, dy = 0):

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

        slope = (other.cy - self.cy) / (other.cx - self.cx)
        # angle = other.cy - self

        if distance(self.cx, self.cy, other.cx, other.cy) < 2 * self.r:
            print("YES")


            if other.cx > self.cx and other.cy < self.cy:
                # first dimension

                self.dx = self.speed * slope
                self.dy = self.dx * slope
                other.dx = other.speed * -slope
                other.dy = other.dx * -slope
            elif other.cx < self.cx and other.cy > self.cy:
                # third dimension
                self.dx = self.speed * -slope
                self.dy = self.dx * slope
                other.dx = other.speed * slope
                other.dy = other.dx * slope
            elif other.cx < self.cx and other.cy < self.cy:
                # second dimension

                other.dx = self.dx
                other.dy = self.dy

                self.dx = self.speed
                self.dy = self.dx * slope

            elif other.cx > self.cx and other.cy > self.cy:
                # forth dimension
                self.dx = self.speed * -slope
                self.dy = self.dx * slope
                other.dx = other.speed * slope
                other.dy = other.dx * -slope


        pass
    # def collide(self,other):




        pass
    def move(self):

        self.cx += self.dx
        self.cy += self.dy


        pass
    def draw(self, canvas):

        # canvas.create_line(self.cx,self.cy,self.cx + 1,self.cy + 1, fill = "black")

        canvas.create_oval(self.cx - self.r, self.cy - self.r,
                           self.cx + self.r, self.cy + self.r,
                           fill = self.color)
