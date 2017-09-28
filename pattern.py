from turtle import *

'''
Program for generating patterns using polygons repeated in circular manner.
first argument to shape() is vertices of polygon.
Second argument is optional which increases the density of pattern.
'''
setup(height=0.92,startx=670,starty=0)

def myfunc(vertices,density=1):
    clearscreen()
    t=Turtle()
    tracer(0)
    t.ht()
    for i in range(vertices*density*2):
        t.right(180/(vertices*density))
        t.circle(150,steps=vertices)
    update()

while True:
    args=map(int,input().split())
    try:
    	myfunc(*args)
    except TypeError:
    	raise SystemExit