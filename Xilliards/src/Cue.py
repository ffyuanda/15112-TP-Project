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
        self.stickLength = 300
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

        # build the cue stick
        print("hitAngle: " + str(hitAngle))
        self.getStickCoor(event, ball)

    def getStickCoor(self, event, ball):

        lengthToCenter = distance(event.x, event.y, ball.cx, ball.cy)
        # in order to get "r", which is half of the distance
        # between the hitting point and the center.
        lengthToCenter /= 2

        # ballAngle is the relative angle for
        # the white ball (from clicking point)
        ballAngle = getDirection(ball.cx, ball.cy,
                                     event.x, event.y, lengthToCenter)

        # hitAngle is the relative angle for
        # the clicking point (from the white ball)
        hitAngle = getDirection(event.x, event.y, ball.cx,
                                ball.cy, lengthToCenter)

        hitToBall = lengthToCenter * 2 - self.stickLength

        print("ballDirection: " + str(ballAngle))
        self.headX = ball.cx + (ball.r + 10) * math.cos(ballAngle)
        self.headY = ball.cy - (ball.r + 10) * math.sin(ballAngle)
        self.toeX = event.x + hitToBall * math.cos(hitAngle)
        self.toeY = event.y - hitToBall * math.sin(hitAngle)


    def draw(self, canvas):

        canvas.create_line(self.headX, self.headY,
                           self.toeX, self.toeY,
                           fill="ivory", width=5)
