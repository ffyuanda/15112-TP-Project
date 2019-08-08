from Table import *
from Ball import *
from PublicFunctions import *
from Pocket import *
from Cue import *
from tkinter import *
from AnimationFunctions import *

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

    # used to keep record of the times space is pressed
    data.spaceTime = 0
    data.forceCounter = 0
    data.placeCueStick = False

    data.score = 0

    # game state control
    data.gameOver = False
    data.scratched = None
    data.hitted = False
    data.scratchReplace = False

    data.time = 0


def mousePressed(event, data):
    # use event.x and event.y

    cueStickClickControl(event, data)

    scratchReplace(event, data)

    pass


def keyPressed(event, data):
    # use event.char and event.keysym

    cueStickSpaceControl(event, data)

    if event.keysym == "r":
        init(data)

    pass


def timerFired(data):
    data.time += 1

    frictionControl(data)

    cueStickControl(data)

    ballsCollision(data)

    scratchControl(data)

    pocketScoring(data)

    pass


def redrawAll(canvas, data):
    # draw in canvas
    if data.gameOver:
        gameOverDraw(canvas, data)


    else:
        data.table.draw(canvas)

        for pocket in data.pockets:
            pocket.draw(canvas)

        for ball in data.balls:
            ball.draw(canvas)

        cueStickDraw(canvas, data)

        drawScore(data, canvas)

        if data.scratchReplace:

            scratchReplaceDraw(canvas, data)

    pass

# The run fucntions are cited from 15112 course notes:
# https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part1.html
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