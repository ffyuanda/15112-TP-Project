from Ball import *
from PublicFun import *


# This is the function in control of the billiards table.

class table(object):

    def __init__(self, data, width, height):
        self.width = width
        self.height = height
        self.centerX = data.width // 2
        self.centerY = data.height // 2
        self.color = "green"
        self.horiBarLen = data.width
        self.vertBarLen = data.height
        self.barWidth = 25
        self.barColor = "brown"

    def draw(self, canvas):
        canvas.create_rectangle(self.centerX - self.width // 2,
                                self.centerY - self.height // 2,
                                self.centerX + self.width // 2,
                                self.centerY + self.height // 2,
                                fill=self.color
                                )
        # first bar (up)
        canvas.create_rectangle(0, 0, self.horiBarLen, self.barWidth,
                                fill=self.barColor, width=0)
        # second bar (down)
        canvas.create_rectangle(0, self.height - self.barWidth,
                                self.horiBarLen, self.height,
                                fill=self.barColor, width=0)
        # third bar (left)
        canvas.create_rectangle(0, self.barWidth,
                                self.barWidth, self.vertBarLen,
                                fill=self.barColor, width=0)
        # second bar (down)
        canvas.create_rectangle(self.width - self.barWidth, 0,
                                self.width, self.height,
                                fill=self.barColor, width=0)
        # foot rail
        canvas.create_line(self.width // 1.3, self.barWidth,
                           self.width // 1.3, self.height - self.barWidth,
                           fill="white", width=3)

    def collide(self, ball):

        if ball.cx - ball.r < self.barWidth or ball.cx + ball.r > self.width\
            - self.barWidth:
            ball.dx = -ball.dx
        if ball.cy - ball.r < self.barWidth or \
                ball.cy + ball.r > self.height - self.barWidth:
            ball.dy = -ball.dy

    def initBalls(self, data):
        example = Ball(100, 100, "pink")

        data.balls.append(Ball(data.width // 4, data.height // 3 + 2 * example.r, "red"))
        data.balls.append(Ball(data.width // 4, data.height // 3 + 4 * example.r, "red"))
        data.balls.append(Ball(data.width // 4, data.height // 3 + 6 * example.r, "red"))
        data.balls.append(Ball(data.width // 4, data.height // 3 + 8 * example.r, "red"))
        data.balls.append(Ball(data.width // 4, data.height // 3 + 10 * example.r, "red"))
        pass


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
                           fill = self.color)





