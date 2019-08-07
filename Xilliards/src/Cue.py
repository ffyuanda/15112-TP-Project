from Ball import *
from Table import *
from PublicFun import *

class Cue(object):

    def __init__(self, headX, headY, toeX, toeY, speed):
        self.headX = headX
        self.headY = headY
        self.toeX = toeX
        self.toeY = toeY
        self.speed = speed
        self.stickLength = 70

        # bandage fixes
        self.dx = 0
        self.dy = 0

    def hit(self, event, ball):

        ball.speed += self.speed
        lengthToCenter = distance(event.x, event.y, ball.cx, ball.cy)

        # in order to get "r", which is half of the distance
        # between the hitting point and the center.
        lengthToCenter /= 2
        hitAngle = getDirection(event.x, event.y, ball.cx,
                                ball.cy, lengthToCenter)
        setDirection(self, ball, hitAngle)




