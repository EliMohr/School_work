#Module 1 Assignment INFO 1020
#Please use this template and fill in code after each comment

#Import the turtle module (see page 19, section 1.5 of text 4th ed.)
#from dp import *

def drawCircle(myTurtle,radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(myTurtle, sideLength, 360)

def drawPolygon(myTurtle, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)

def drawTriangle(myTurtle, sideLength):
    for i in range(3):
        myTurtle.forward(sideLength)
        myTurtle.right(120)

def drawSpiral(myTurtle, maxSide):
    for sideLength in range(1, maxSide + 1, 5):
        myTurtle.forward(sideLength)
        myTurtle.right(90)

def drawSquare(myTurtle, sideLength):
    for i in range (4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)


import turtle
#Have the turtle draw something interesting.

#Use at least two different shapes.  You _can_ use the drawPolygon() 
#and drawCircle() functions from the book.
#If you aren't sure what to draw, do Programming Exercise 1.1 in the book.

#def drawCircle():

t = turtle.Turtle()

for i in range(10):

    drawPolygon(t, 100)

    t.right(5)

    drawCircle(t, 50)

#drawPolygon(t, 100)

drawCircle(t, 100)

drawTriangle(t, 200)

drawSpiral(t, 100, 5)

drawSquare(t, 200)







#When finished, submit both this .py file and a png screenshot of your drawing.
