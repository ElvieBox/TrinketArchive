#https://trinket.io/python/99cbb6abeb





# Adds in mutation in AI Blobs and inheritance - D


import turtle
from random import randint, choice, random, randrange
from time import sleep
from classes import *
from networks import *
from functions import*

# User Changed Variables
number_of_blobs = 8
number_of_fruit = 15
gens = 100000
maxframes = 350

# Static Variables
gen = 0
rankings = []
for i in range(4):
    rankings.append(blankNetwork)

# Screen
screen = turtle.Screen()
screen.bgcolor("black");
screen.tracer(0)

# Drawer
drawer = turtle.Turtle()
drawer.penup()
drawer.speed(0)
drawer.color("#0ab00a")
drawer.shape("circle")
drawer.ht()
drawer.left(90)
drawer.goto(-180, -180)
drawer.begin_fill()
drawer.sety(180)
drawer.setx(180)
drawer.sety(-180)
drawer.setx(-180)
drawer.end_fill()

# Stamper
stamper = turtle.Turtle()
stamper.speed(0)
stamper.left(90)
stamper.ht()
stamper.penup()
stamper.shape("circle")

# Scorer
scorer = turtle.Turtle()
scorer.speed(0)
scorer.left(90)
scorer.ht()
scorer.penup()
scorer.shape("circle")
scorer.color("white")



# MAINLOOP
while gen < gens:
    gen += 1
    
    # RESET
    clear(blobs)
    clear(food)
    clear(deactiveBlobs)
    clear(deactiveFood)
    scorer.clear()
    runGen = True
    stillMoving = None
    frame = 0
    
    # Display Gen
    scorer.goto(-175, 160)
    scorer.write("Gen: " + str(gen), font=("Arial", 10))
    
    # Add Fruit
    for fruit in range(number_of_fruit):
        Food(randint(-170, 170), randint(-170, 170))
    
    # Add Blobs
    for blobnum in range(number_of_blobs):
        blob = Blob()
        blob.goto(randint(-170, 170), randint(-170, 170))
        networkNum = randint(0,6)
        if networkNum <= 1:
            network = deepCopy(rankings[0])
        elif networkNum <= 4:
            network = deepCopy(rankings[1])
        elif networkNum <= 6:
            network = deepCopy(rankings[2])
        # Failsafe for devolving
        if blobnum == 0:
            network = deepCopy(rankings[0]) 
        # Mutate Network
        if blobnum > 0:
            mutation = mutate(network)
            while mutation != "QUIT":
                mutation = mutate(network)
        blob.addBrain(network)

    
    # Run Gen
    while runGen and frame <= maxframes:
        screen.update()
        sleep(0.01)
        frame += 1
    
        for blob in blobs:
            nearestFood = blob.nearestFood()
            nearestBlob = blob.nearestBlob()
            if nearestFood == None:
                break
            if nearestBlob == None:
                inputs = {
                    "food_x": nearestFood.xcor - blob.xcor,
                    "food_y": nearestFood.ycor - blob.ycor,
                    "blob_x": 0,
                    "blob_y": 0,
                }
                if stillMoving == None:
                    lastx = blob.xcor
                    lasty = blob.ycor
                    blob.run(inputs)
                    if (blob.xcor == lastx) or (blob.ycor == lasty):
                        runGen = False
                        stillMoving = False
                        break
                    else:
                        stillMoving = True
            else:
                inputs = {
                    "food_x": nearestFood.xcor - blob.xcor,
                    "food_y": nearestFood.ycor - blob.ycor,
                    "blob_x": nearestBlob.xcor - blob.xcor,
                    "blob_y": nearestBlob.ycor - blob.ycor,
                }
            blob.run(inputs)
            blob.tryEat(nearestFood)
            if nearestBlob != None:
                blob.tryAttack(nearestBlob)
        
        stamper.clear()
        for blob in blobs:
            stamper.color(blob.color[0], blob.color[1], blob.color[2])
            stamper.goto(blob.xcor, blob.ycor)
            stamper.stamp()
        stamper.color("#c41919")
        for fruit in food:
            stamper.goto(fruit.xcor, fruit.ycor)
            stamper.stamp()
    
        if len(food) == 0:
            runGen = False
    
    
    # End Frame
    stamper.clear()
    for blob in blobs:
        stamper.color(blob.color[0], blob.color[1], blob.color[2])
        stamper.goto(blob.xcor, blob.ycor)
        stamper.stamp()
    screen.update()
    
    # Display Stats
    scorer.goto(0,((len(blobs)+len(deactiveBlobs))*15)/2)
    for blob in blobs:
        scorer.write("Score: " + str(blob.score) + " | Survived: Yes | Fruits Collected: " + str(blob.eaten) + " | Blobs Killed: " + str(blob.blobsKilled), align="center")
        scorer.sety(scorer.ycor()-15)
    for blob in deactiveBlobs:
        scorer.write("Score: " + str(blob.score) + " | Survived: No | Fruits Collected: " + str(blob.eaten) + " | Blobs Killed: " + str(blob.blobsKilled), align="center")
        scorer.sety(scorer.ycor()-15)
    screen.update()
    
    
    # Evaluate
    for deactivated in deactiveBlobs:
        blobs.append(deactivated)
    blobs.sort(key=getScore, reverse=True)
    if blobs[0].score >= 1 or gen < 5:
        rankings = [rankings[0]]
        for blob in blobs[:2]:
            if blob.score >= 1:
                rankings.append(blob.network)
            else:
                rankings.append(rankings[0])
    else:
        rankings[0] = blobs[0].network
    
    sleep(1)




