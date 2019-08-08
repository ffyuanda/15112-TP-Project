from Ball import *
from Table import *
import math


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def getDirection(cx, cy, dx, dy, r):
    # cx and cy is the self's position, which is the active ball.
    # dx and dy is the other's position, which is the reactive ball.
    # "dimension" means from other to self (other in self's X dimension).
    direction = 0
    if cx > dx and cy < dy:
        # 3 dimension glancing collision (sin)
        # other relative to self
        print("3 dimension with sin")

        direction = math.asin((dy - cy) / (2 * r)) + math.pi

    elif cx < dx and cy > dy:
        # 1 dimension glancing collision (sin)
        # other relative to self
        print("1 dimension with sin")
        direction = -math.asin((dy - cy) / (2 * r))

    elif cx < dx and cy < dy:
        # 4 dimension glancing collision (sin)
        # other relative to self
        print("4 dimension with cos")
        direction = 2 * math.pi - math.acos((dx - cx) / (2 * r))


    elif (cx > dx and cy > dy):
        # 2 dimension glancing collision (cos)
        # other relative to self
        print("2 dimension with cos")
        direction = math.acos((dx - cx) / (2 * r))

    elif cx == dx and cy < dy:
        # self above the other
        print("head-on collision")
        direction = "Up"

    elif cx == dx and cy > dy:
        # self under the other
        print("head-on collision")
        direction = "Down"


    elif cx > dx and cy == dy:
        # self at the right of the other
        print("head-on collision")
        direction = "Right"

    elif cx < dx and cy == dy:
        # self at the left of the other
        print("head-on collision")
        direction = "Left"

    return direction


def setDirection(self, other, angle):
    # dy = math.sin(angle)
    if type(angle) != str:

        other.dx = math.cos(angle) + 0.2
        other.dy = -(math.sin(angle) + 0.2)
        self.dx = math.cos(angle - 0.5 * math.pi)  # rotate 90 degrees
        self.dy = math.sin(angle - 0.5 * math.pi)  # rotate 90 degrees

        if (0 < angle < 0.5 * math.pi) or \
                (math.pi < angle < 1.5 * math.pi):
            # 1 and 3 dimension
            self.dx = -self.dx
            self.dy = self.dy

        elif (0.5 * math.pi < angle < math.pi) or \
                (1.5 * math.pi < angle < 2 * math.pi):
            # 2 and 4 dimension
            self.dx = self.dx
            self.dy = -self.dy

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


def setSpeed(self, other, angle=0):
    # angle is the angle that created by the getDirection function

    # Physics:
    # Since the conservation of momentum in physics, that the momentum
    # on the x axis and the momentum on the y axis should be the same
    # as those before collision in the current colliding system, respectively.

    # bandage fix: The code below is not actual physics! Need to be fixed!
    other.speed = self.speed
    self.speed /= 4

    pass
