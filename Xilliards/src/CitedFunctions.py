from Animation import *
from tkinter import *

# The rgbString fucntions are cited from 15112 course notes:
# https://www.cs.cmu.edu/~112-n19/notes/notes-graphics.html


def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)


# The run fucntions are cited from 15112 course notes:
# Since the run function would call the init in the Animation
# file, so I comment it here to make the function run correctly.

# https://www.cs.cmu.edu/~112-n19/notes/notes-animations-part1.html
# def run(width=1000, height=700):
#     def redrawAllWrapper(canvas, data):
#         canvas.delete(ALL)
#         canvas.create_rectangle(0, 0, data.width, data.height,
#                                 fill='white', width=0)
#         redrawAll(canvas, data)
#         canvas.update()
#
#     def mousePressedWrapper(event, canvas, data):
#         mousePressed(event, data)
#         redrawAllWrapper(canvas, data)
#
#     def keyPressedWrapper(event, canvas, data):
#         keyPressed(event, data)
#         redrawAllWrapper(canvas, data)
#
#     def timerFiredWrapper(canvas, data):
#         timerFired(data)
#         redrawAllWrapper(canvas, data)
#         # pause, then call timerFired again
#         canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
#
#     # Set up data and call init
#     class Struct(object): pass
#
#     data = Struct()
#     data.width = width
#     data.height = height
#     data.timerDelay = 5  # milliseconds
#     root = Tk()
#     init(data)
#     # create the root and the canvas
#     canvas = Canvas(root, width=data.width, height=data.height)
#     canvas.configure(bd=0, highlightthickness=0)
#     canvas.pack()
#     # set up events
#     root.bind("<Button-1>", lambda event:
#     mousePressedWrapper(event, canvas, data))
#     root.bind("<Key>", lambda event:
#     keyPressedWrapper(event, canvas, data))
#     timerFiredWrapper(canvas, data)
#     # and launch the app
#     root.mainloop()  # blocks until window is closed
#     print("bye!")
