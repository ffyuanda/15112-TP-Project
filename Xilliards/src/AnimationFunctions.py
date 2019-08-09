#############################
#############################
# timerFired:
#############################
#############################

from Animation import *

def frictionControl(data):

    # friction control system:
    # adjust the frequency the friction()
    # function executed.

    if data.time % 10 == 0:

        for ball in data.balls:

            if ball.speed > 0:
                ball.friction()

            if ball.speed <= 0:
                ball.speed = 0


def ballsCollision(data):

    # balls colliding system:
    # loop through each ball in the balls list
    # and mutually check the collision state

    for ball in data.balls:

        ball.move()

        data.table.collide(ball)

        for nextBall in data.balls:

            if nextBall != ball:

                ball.collide(nextBall, data)


def cueStickControl(data):

    # cue stick control system:
    # add the forceCounter by time
    if data.time % 5 == 0 and data.placeCueStick:
        if data.forceCounter < 100:
            data.forceCounter += 1


def scratchControl(data):

    # scratch control system:
    if data.cueBall.speed == 0:

        if data.scratched and data.hitted:

            data.scratchReplace = True
            data.scratched = False


def pocketScoring(data):
    # pocket scoring system:

    for pocket in data.pockets:
        pocket.score(data)

    if data.cueBall not in data.balls:
        data.gameOver = True


#########################
# keyPressed:
#########################

def cueStickSpaceControl(event, data):

    if event.keysym == "space":

        data.spaceTime += 1

        if data.spaceTime == 1:
            # the first time press the space:
            # started to count the force, set the
            # data.hitted to False, because the hit
            # is not conducted yet. And set the scratched
            # to True, because the program wants to check
            # if the cue ball hit any of the balls, if so, then
            # in the collide() function in the Ball class, the
            # scratched would be turned to False, so on and so forth.

            data.hitted = False
            data.forceCounter = 0
            data.scratched = True

        elif data.spaceTime == 2:

            # here you can adjust the relation
            # between the forceCounter and the actual
            # force, the bigger the number, the less the force, vice versa.
            data.cue.speed = data.forceCounter / 20
            data.cue.hit(event, data.cueBall)
            data.hitted = True



######################
# mousePressed:
######################

def cueStickClickControl(event, data):

    if data.cueBall.speed == 0 and data.scratchReplace is False:
        data.placeCueStick = True
        data.cue.getStickCoor(event, data.cueBall)
        data.cue.hitX = event.x
        data.cue.hitY = event.y
        data.spaceTime = 0

def scratchReplace(event, data):

    if data.scratchReplace:
        data.cueBall.cx = event.x
        data.cueBall.cy = event.y
        data.scratchReplace = False


#######################
# redrawAll:
#######################

def cueStickDraw(canvas, data):

    if data.placeCueStick and data.spaceTime != 2:
        data.cue.draw(data, canvas)

        if data.spaceTime == 1:
            data.cue.drawForce(data, canvas)


def gameOverDraw(canvas, data):

    canvas.create_text(data.width // 2, data.height // 2,
                       text="Game Over"
                            " Press 'r' to restart", font="Times 30 bold")


def scratchReplaceDraw(canvas, data):

    canvas.create_text(data.width // 2, data.height // 2,
                       text="Scratched!\n"
                            "Click to replace the cue ball.",
                       font="Times 30 bold")


pass