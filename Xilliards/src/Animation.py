from Table import *
from Ball import *
from PublicFun import *
from Cue import *





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
    data.table.initBalls(data)
    data.ball = Ball(data.width // 2 , data.height // 2, "red")
    data.testBall2 = Ball(data.width // 2 + 100, data.height // 2, "white")
    data.testBall2.dx = 0
    data.testBall2.dy = 0
    data.balls.append(data.ball)
    data.balls.append(data.testBall2)
    data.time = 0


    data.cue = Cue(0, 0, 0, 0, 2)

    pass

def mousePressed(event, data):
    # use event.x and event.y

    for ball in data.balls:

        if ball.color == "white":

            data.cue.hit(event, ball)


    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    data.time += 1
    if data.time % 5 == 0:
        for ball in data.balls:
            if ball.speed > 0:
                ball.friction()
            if ball.speed <= 0:
                ball.speed = 0

    collided = []
    # if data.time % 2 == 0:
    for ball in data.balls:

        ball.move()

        data.table.collide(ball)

        for nextBall in data.balls:

            if nextBall != ball:


                ball.collide(nextBall)

        collided.append(ball)

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

def run(width=1000, height=700):
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
    data.timerDelay = 7 # milliseconds
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