from Ball import *
from PublicFunctions import *
from CitedFunctions import *


# This is the function in control of the billiards table.

class Table(object):

    def __init__(self, data, width, height):
        self.width = width
        self.height = height
        self.centerX = data.width // 2
        self.centerY = data.height // 2
        # The rgbString fucntions are cited from 15112 course notes:
        # https://www.cs.cmu.edu/~112-n19/notes/notes-graphics.html
        self.color = rgbString(50, 88, 59)
        self.horiBarLen = data.width
        self.vertBarLen = data.height
        self.barWidth = 25
        self.barColor = rgbString(76, 39, 10)

    def draw(self, canvas):

        # table
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

        if ball.cx - ball.r < self.barWidth or ball.cx + ball.r > self.width \
                - self.barWidth:
            ball.dx = -ball.dx
        if ball.cy - ball.r < self.barWidth or \
                ball.cy + ball.r > self.height - self.barWidth:
            ball.dy = -ball.dy

    def addBalls(self, data):

        example = Ball(100, 100, "pink")
        # adjust is used to prevent balls stuck into each other
        adjust = 1.5

        # customColor is used to pick RGB value from
        # real pool balls.
        # The rgbString fucntions are cited from 15112 course notes:
        # https://www.cs.cmu.edu/~112-n19/notes/notes-graphics.html

        # first column:

        firstColumnGap = 2 * example.r

        customColor = rgbString(246, 140, 51)
        data.balls.append(Ball(data.width // 4,
                               data.height // 3 + 1 * firstColumnGap + adjust,
                               customColor))

        # customColor = rgbString(13, 34, 106)
        # data.balls.append(Ball(data.width // 4,
        #                        data.height // 3 + 2 * firstColumnGap + 2 * adjust,
        #                        customColor))
        #
        # customColor = rgbString(239, 18, 14)
        # data.balls.append(Ball(data.width // 4,
        #                        data.height // 3 + 3 * firstColumnGap + 3 * adjust,
        #                        customColor))
        #
        # customColor = rgbString(47, 34, 87)
        # data.balls.append(Ball(data.width // 4,
        #                        data.height // 3 + 4 * firstColumnGap + 4 * adjust,
        #                        customColor))
        #
        # customColor = rgbString(255, 61, 35)
        # data.balls.append(Ball(data.width // 4,
        #                        data.height // 3 + 5 * firstColumnGap + 5 * adjust,
        #                        customColor))
        #
        # # second column:
        # # calculated by trigonometry
        # secondRowGap = (3 ** 0.5) * example.r + 2 * adjust
        #
        # customColor = rgbString(29, 55, 38)
        # data.balls.append(Ball(data.width // 4 + secondRowGap,
        #                        data.height // 3 + 3 * example.r + adjust,
        #                        customColor))
        #
        # customColor = rgbString(144, 18, 4)
        # data.balls.append(Ball(data.width // 4 + secondRowGap,
        #                        data.height // 3 + 5 * example.r + 2 * adjust,
        #                        customColor))
        #
        # customColor = rgbString(239, 18, 14)
        # data.balls.append(Ball(data.width // 4 + secondRowGap,
        #                        data.height // 3 + 7 * example.r + 3 * adjust,
        #                        customColor))
        #
        # customColor = rgbString(246, 140, 51)
        # data.balls.append(Ball(data.width // 4 + secondRowGap,
        #                        data.height // 3 + 9 * example.r + 4 * adjust,
        #                        customColor))
        #
        # # third column:
        # thirdRowGap = 2 * (3 ** 0.5) * example.r + 3 * adjust
        #
        # customColor = rgbString(13, 34, 106)
        # data.balls.append(Ball(data.width // 4 + thirdRowGap,
        #                        data.height // 3 + 4 * example.r + adjust,
        #                        customColor))
        #
        # customColor = rgbString(8, 11, 15)
        # data.balls.append(Ball(data.width // 4 + thirdRowGap,
        #                        data.height // 3 + 6 * example.r + 2 * adjust,
        #                        customColor))
        #
        # customColor = rgbString(47, 34, 87)
        # data.balls.append(Ball(data.width // 4 + thirdRowGap,
        #                        data.height // 3 + 8 * example.r + 3 * adjust,
        #                        customColor))
        #
        # #forth column:
        #
        # forthRowGap = 3 * (3 ** 0.5) * example.r + 5 * adjust
        #
        # customColor = rgbString(255, 61, 35)
        # data.balls.append(Ball(data.width // 4 + forthRowGap,
        #                        data.height // 3 + 5 * example.r + adjust,
        #                        customColor))
        #
        # customColor = rgbString(29, 55, 38)
        # data.balls.append(Ball(data.width // 4 + forthRowGap,
        #                        data.height // 3 + 7 * example.r + 2 * adjust,
        #                        customColor))
        #
        # #fifth column:
        #
        # fifthRowGap = 4 * (3 ** 0.5) * example.r + 6 * adjust
        #
        # customColor = rgbString(144, 18, 4)
        # data.balls.append(Ball(data.width // 4 + fifthRowGap,
        #                        data.height // 3 + 6 * example.r + adjust,
        #                        customColor))



