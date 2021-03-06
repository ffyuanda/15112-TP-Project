from Ball import *
from Table import *
from numpy import linalg
import numpy as np

import math


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# speedX and speedY are used to
# record the original value of the
# self ball in the function getDirection and
# setDirection and setSpeed, cause the cx and
# cy would likely be changed.


def getDirection(cx, cy, dx, dy, r):
    # cx and cy is the self's position, which is the active ball.
    # dx and dy is the other's position, which is the reactive ball.
    # "dimension" means from other to self (other in self's X dimension).
    direction = 0

    if cx > dx and cy < dy:
        # 3 dimension glancing collision (sin)
        # other relative to self
        # print("3 dimension with sin")

        direction = math.asin((dy - cy) / (2 * r)) + math.pi

    elif cx < dx and cy > dy:
        # 1 dimension glancing collision (sin)
        # other relative to self
        # print("1 dimension with sin")
        direction = -math.asin((dy - cy) / (2 * r))

    elif cx < dx and cy < dy:
        # 4 dimension glancing collision (sin)
        # other relative to self
        # print("4 dimension with cos")
        direction = 2 * math.pi - math.acos((dx - cx) / (2 * r))


    elif (cx > dx and cy > dy):
        # 2 dimension glancing collision (cos)
        # other relative to self
        # print("2 dimension with cos")
        direction = math.acos((dx - cx) / (2 * r))

    elif cx == dx and cy < dy:
        # self above the other
        # print("head-on collision")
        direction = "Up"

    elif cx == dx and cy > dy:
        # self under the other
        # print("head-on collision")
        direction = "Down"


    elif cx > dx and cy == dy:
        # self at the right of the other
        # print("head-on collision")
        direction = "Right"

    elif cx < dx and cy == dy:
        # self at the left of the other
        # print("head-on collision")
        direction = "Left"

    return direction


def setDirection(self, other, angle):
    # dy = math.sin(angle)
    if type(angle) != str:

        other.dx = math.cos(angle)
        other.dy = -math.sin(angle)
        self.dx = math.cos(angle - 0.5 * math.pi)  # rotate 90 degrees
        self.dy = math.sin(angle - 0.5 * math.pi)  # rotate 90 degrees

        if (0 < angle < 0.5 * math.pi) or \
                (math.pi < angle < 1.5 * math.pi):
            # 1 and 3 dimension
            self.dx = self.dx
            self.dy = -self.dy

        elif (0.5 * math.pi < angle < math.pi) or \
                (1.5 * math.pi < angle < 2 * math.pi):
            # 2 and 4 dimension
            self.dx = -self.dx
            self.dy = self.dy

    elif angle == "Up":
        # head-on collision
        other.dx = self.dx
        other.dy = self.dy + 1

    elif angle == "Down":
        # head-on collision
        other.dx = self.dx
        other.dy = self.dy - 1

    elif angle == "Right":
        # head-on collision
        other.dx = self.dx - 1
        other.dy = self.dy

    elif angle == "Left":
        # head-on collision
        other.dx = self.dx + 1
        other.dy = self.dy

        pass


def setSpeed(self, other, speedX=0, speedY=0):
    # angle is the angle that created by the getDirection function

    # Physics:
    # Since the conservation of momentum in physics, that the momentum
    # on the x axis and the momentum on the y axis should be the same
    # as those before collision in the current colliding system, respectively.

    # The formula for the system of equations below is
    # other.dx * other.speed + self.dx * self.speed = speedX
    # other.dy * other.speed + self.dy * self.speed = speedY
    # In the equations above, dx and dy could be seen as vectors
    # of the two balls in the system at the instant of collision.
    # And the speed is not the actual vector speed, it is an attribute
    # which belongs to each ball. The speedX and speedY is the original
    # self ball's vector before collision. Therefore, by listing this
    # equation, the momentum is conserved due to the conservation of momentum.

    # The numpy package is cited from the scientific calculation set
    # NumPy under the Scipy scientific calculation kit.
    # The NumPy's website is https://numpy.org/
    # And the Scipy's website is https://scipy.org/

    buffer = 0.1
    nrow1 = [other.dx, self.dx]
    nrow2 = [other.dy, self.dy]

    nmat = np.array([nrow1, nrow2])
    cons = np.array([speedX, speedY])

    answer = linalg.solve(nmat, cons)

    other.speed = answer[0] + buffer
    self.speed = answer[1]

    print(other.speed, self.speed)

    pass


def drawScore(data, canvas):
    canvas.create_text(data.width // 2, 80,
                       text="Score: %d" % data.score,
                       fill="grey", font="Helvetica 30 bold italic")
