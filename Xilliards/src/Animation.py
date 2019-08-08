from Table import *
from Ball import *
from PublicFunctions import *
from Pocket import *
from Cue import *
from tkinter import *


# The run fucntions are cited from 15112 course notes:
# https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part1.html

# Basic Animation Framework


####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.table = Table(data, data.width, data.height)
    data.cue = Cue(0, 0, 0, 0, 0)
    data.pockets = []
    data.balls = []
    data.pocketInit = pocket(0, 0)
    data.pocketInit.addPockets(data)
    data.table.addBalls(data)
    data.cueBall = Ball(data.width // 2 + 100, data.height // 2, "white")
    data.balls.append(data.cueBall)

    # used to keep record of the time space is pressed
    data.spaceTime = 0
    data.forceCounter = 0
    data.placeCueStick = False

    data.score = 0
    data.gameOver = False

    data.time = 0


def mousePressed(event, data):
    # use event.x and event.y
    if data.cueBall.speed == 0:
        data.placeCueStick = True
        data.cue.getStickCoor(event, data.cueBall)
        data.cue.hitX = event.x
        data.cue.hitY = event.y
        data.spaceTime = 0
    # print(data.placeCueStick)

    pass


def keyPressed(event, data):
    # use event.char and event.keysym
    if event.keysym == "space":

        data.spaceTime += 1

        if data.spaceTime == 1:

            data.forceCounter = 0


        elif data.spaceTime == 2:

            data.cue.speed = data.forceCounter / 25
            data.cue.hit(event, data.cueBall)

    if event.keysym == "r":
        init(data)

    pass


def timerFired(data):
    data.time += 1

    # friction control system:
    # adjust the frequency the friction()
    # function executed.
    if data.time % 10 == 0:

        for ball in data.balls:

            if ball.speed > 0:
                ball.friction()

            if ball.speed <= 0:
                ball.speed = 0

    # cue stick control system:
    # add the forceCounter by time
    if data.time % 5 == 0 and data.placeCueStick:
        data.forceCounter += 1

    # balls colliding system:
    # loop through each ball in the balls list
    # and mutually check the collision state
    for ball in data.balls:

        ball.move()

        data.table.collide(ball)

        for nextBall in data.balls:

            if nextBall != ball:
                ball.collide(nextBall)

    # pocket scoring system:

    for pocket in data.pockets:
        pocket.score(data)

    if data.cueBall not in data.balls:
        data.gameOver = True

    pass


def redrawAll(canvas, data):
    # draw in canvas
    if data.gameOver:
        canvas.create_text(data.width // 2, data.height // 2,
                           text="Game Over"
                                " Press 'r' to restart", font="Times 30 bold")
    else:
        data.table.draw(canvas)

        for pocket in data.pockets:
            pocket.draw(canvas)

        for ball in data.balls:
            ball.draw(canvas)

        if data.placeCueStick and data.spaceTime != 2:
            data.cue.draw(data, canvas)

            if data.spaceTime == 1:
                data.cue.drawForce(data, canvas)

        drawScore(data, canvas)
    pass


####################################
# use the run function as-is
##############################
# ######

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
    data.timerDelay = 5  # milliseconds
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
