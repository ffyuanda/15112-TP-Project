# This is the function in control of the pockets.
from PublicFunctions import *


class pocket(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 20
        self.color = "black"
        self.barWidth = 20

    def addPockets(self, data):
        data.pockets.append(pocket(self.barWidth + self.r,
                                   self.barWidth + self.r))
        data.pockets.append(pocket(data.width // 2,
                                   self.barWidth + self.r))
        data.pockets.append(pocket(data.width - self.r - self.barWidth,
                                   self.r + self.barWidth))
        data.pockets.append(pocket(self.r + self.barWidth,
                                   data.height - self.r - self.barWidth))
        data.pockets.append(pocket(data.width // 2,
                                   data.height - self.r - self.barWidth))
        data.pockets.append(pocket(data.width - self.r - self.barWidth,
                                   data.height - self.r - self.barWidth))

    def draw(self, canvas):

        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r,
                           fill=self.color)

    def score(self, data):

        for ball in data.balls:

            dis = distance(self.x, self.y, ball.cx, ball.cy)

            if dis <= self.r + 10:
                data.balls.remove(ball)
                data.score += 1

        pass
