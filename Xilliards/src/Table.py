from Ball import *



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
                                fill = self.color
                                )
        # first bar (up)
        canvas.create_rectangle(0, 0, self.horiBarLen, self.barWidth,
                                fill=self.barColor, width = 0)
        # second bar (down)
        canvas.create_rectangle(0, self.height - self.barWidth,
                                self.horiBarLen, self.height,
                                fill=self.barColor, width = 0)
        # third bar (left)
        canvas.create_rectangle(0, self.barWidth,
                                self.barWidth, self.vertBarLen,
                                fill=self.barColor, width = 0)
        # second bar (down)
        canvas.create_rectangle(self.width - self.barWidth, 0,
                                self.width, self.height,
                                fill=self.barColor, width = 0)


    # def drawPocket(self, data):



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



# The run fucntions are cited from 15112 course notes:
# https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part1.html

# Basic Animation Framework

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.table = table(data, data.width, data.height)
    data.pockets = []
    data.pocketInit = pocket(0, 0)
    data.pocketInit.addPockets(data)
    data.balls = []

    data.testBall = ball(data.width // 2, data.height // 2, 0, 0, "blue")
    data.testBall2 = ball(data.width // 3, data.height // 2 + 10, 0, 0, "red")
    data.testBall2.dx = 5
    data.balls.append(data.testBall)
    data.balls.append(data.testBall2)

    pass

def mousePressed(event, data):
    # use event.x and event.y



    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    data.testBall.collide(data.testBall2)
    for ball in data.balls:
        ball.move()
    pass

def redrawAll(canvas, data):
    # draw in canvas
    data.table.draw(canvas)

    for pocket in data.pockets:
        pocket.draw(canvas)
    for ball in data.balls:
        ball.draw(canvas)
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

