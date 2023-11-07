import turtle

# for i in range(10):
#     print("*")
#     for j in range(i):
#         print("*",end="")

shelly = turtle.Turtle()
shelly.shape('turtle')

# shelly.forward(100) # moves shelly forward 100 steps
# shelly.right(90) # turns shelly right 90 degrees
# shelly.left(60) # turns shelly left 60 degrees
# shelly.backward(100) # moves shelly backward 100 steps
# shelly.color('red') # makes shelly draw in color red
# shelly.circle(10) # makes shelly draw a circle of size 10
# shelly.penup() # makes shelly lift pen
# shelly.pendown() # makes shelly put the pen down to draw
# shelly.reset() # clears screen and goes back to start position
# shelly.goto(35, 80) # move to x coordinate 35,y coordinate 80
# shelly.hideturtle() # makes shelly not visible on the screen
###############################
# for j in range(12):
#     for i in range(4):
#         shelly.speed(1)
#         shelly.forward(100)
#         shelly.left(90)
#     shelly.right(30)
# turtle.bgcolor('black')
# colors = ['red', 'yellow', 'blue', 'orange','green', 'red']
# for j in range(36):
#     for i in range(6):
#         shelly.color(colors[i])
#         shelly.forward(100)
#         shelly.left(60)
#     shelly.right(10)
# shelly.penup()
# shelly.color('white')
# # repeat 36 times to match the 36 hexagons
# for i in range(36):
#     shelly.forward(220)
#     shelly.pendown()
#     j = 0
#     if j >len(colors):
#         j=0
#     shelly.color(colors[j])
#     j+=1    
#     shelly.circle(5)
#     shelly.penup()
#     shelly.backward(220)
#     shelly.right(10)
# # hide turtle to finish the drawing
# shelly.hideturtle()
#################################
# for i in range(6):
#     colors = ['red', 'yellow', 'blue', 'orange','green', 'purple']
#     shelly.color(colors[i])
#     shelly.pensize(5)
#     for j in range(4):
#         shelly.forward(20)
#         shelly.left(90)
#     shelly.penup()
#     shelly.forward(30)
#     shelly.pendown()
# shelly.hideturtle()
#####################################
# shelly.begin_fill()
# shelly.color('green')
# shelly.circle(100)
# shelly.end_fill()

# shelly.goto(-30,100)
# shelly.begin_fill()
# shelly.color('white')
# shelly.circle(30)
# shelly.end_fill()
# shelly.begin_fill()
# shelly.color('black')
# shelly.circle(20)
# shelly.end_fill()

# shelly.penup()

# shelly.goto(30,100)
# shelly.begin_fill()
# shelly.color('white')
# shelly.circle(30)
# shelly.end_fill()
# shelly.begin_fill()
# shelly.color('black')
# shelly.circle(20)
# shelly.end_fill()
######################################
# colors = ['red', 'yellow', 'blue', 'orange','green', 'purple']
# j = 0

# turtle.bgcolor('black')
# for i in range(72):
#     shelly.speed(10)
#     shelly.color(colors[j])
#     j= j +1
#     if j >= len(colors):
#         j = 0
#     shelly.circle(100)
#     shelly.left(5)
##############################
# turtle.bgcolor('blue')
# shelly.begin_fill()

# for i in range(4):
#     shelly.color('white')
#     shelly.forward(100)
#     shelly.left(90)
# shelly.end_fill()


# shelly.begin_fill()
# shelly.goto(5,50)
# for i in range(4):
#     shelly.color('yellow')
#     shelly.forward(20)
#     shelly.left(90)
# shelly.end_fill()
# shelly.penup()


# shelly.begin_fill()
# shelly.goto(-10,100)
# shelly.pendown()
# for i in range(3):
#     shelly.speed(1)
#     shelly.color('red')
#     shelly.forward(120)
#     shelly.left(120)
# shelly.end_fill()
# shelly.hideturtle()
##########################
turtle.bgcolor('black')
shelly.hideturtle()

colors = ['red', 'yellow', 'blue', 'orange','green', 'purple']
j = 0
for i in range(36):
    shelly.speed(10)
    shelly.penup()
    shelly.forward(200)
    for k in range(8):
        if j >= len(colors):
            j = 0
            shelly.color(colors[j])
        else:
            shelly.color(colors[j])
            j+=1
        shelly.pendown()
        shelly.circle(5)
        shelly.penup()
        shelly.back(20)
        print(j)
    shelly.goto(0,0)
    shelly.right(10)

turtle.done()