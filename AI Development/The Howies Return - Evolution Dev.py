# https://trinket.io/python/06c6867e11

"And cook for 10,000 generations or until crispy brown!"

import turtle
from random import randint, choice
from time import sleep

speed = 15
steps = 32
gens = 800
mutationChance = 25
pause = 0.5
display = 'allbests'
#---------------------------
"""
Speed:   0+   -   How far each point can be from each other
Steps:   0+   -   How many points for each
Gens:    1+   -   How many generations to run through
MutationChance:  0+  -  Chance for the path to change (lower = higher chance)
pause:   0+   -   How long the display should pause for (in sec)
display:  individual, gen, eachbest, allbests, best  -  Shows what to display
"""
gen = 0
count = 0
howies = []
bests = []
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'pink', 'turquoise', 'brown']

chances = {
    1: [],
    2: [],
    3: []
}

class Howie():
    def __init__(self):
        self.genes = []
        self.endPoint = [-180,0]
        self.color = None
        self.fitness = 0

def newGene():
    distance = randint(0, speed)
    x = randint(distance*-1,distance)
    y = (distance-abs(x)) * choice((-1,1))
    return ((x, y))

def displayPath(gene, color, reveal):
    stamper.color(color)
    stamper.goto(-180,0)
    stamper.stamp()
    for point in gene:    # point is relative
        stamper.goto(point[0]+stamper.xcor(), point[1]+stamper.ycor())
        stamper.stamp()
        if reveal == 'locs':
            screen.update()
    if reveal == 'path':
        screen.update()

def updateGen(gen):
    stamper.color('black')
    stamper.clear()
    stamper.goto(-180,180)
    stamper.write('Gen: ' + str(gen), False, 'center')
    screen.update()

def getInheritance():
    return chances[choice([1,2,2,3,3,3])]

screen = turtle.Screen()
screen.tracer(0)

drawer = turtle.Turtle()
drawer.speed(0)
drawer.penup()
drawer.hideturtle()
drawer.goto(180,200)
drawer.pendown()
drawer.sety(-200)
drawer.penup()
del drawer

stamper = turtle.Turtle()
stamper.penup()
stamper.shape('turtle')
stamper.hideturtle()
stamper.speed(0)

for howie in range(10):
    howies.append(Howie())

#-----------------------------------------------------------------------------
while gen <= gens:
    gen += 1
    if gen == 1:
        # Set Up First Gen
        for howie in howies:
            howie.color = (colors+['black'])[howies.index(howie)-1]
            for pos in range(steps):
                howie.genes.append(newGene())
    else:
        # Reset Howies
        for howie in howies:
            howie.fitness = 0
            howie.color = colors[howies.index(howie)-1]
            howie.endPoint = [-180,0]
            howie.genes = []
            for gene in getInheritance():
                howie.genes.append(gene)
        howies[0].color = 'black'
        howie.genes = []
        for gene in getInheritance():
            howie.genes.append(gene)

    # Mutation
    for howie in howies[1:]:
        for geneNum in range(len(howie.genes)):
            if randint(0,mutationChance) == 0:
                howie.genes[geneNum] = newGene()
    
    # Find End Points
    for howie in howies:
        howie.endPoint = [-180,0]
        for gene in howie.genes:
            howie.endPoint[0] += gene[0]
            howie.endPoint[1] += gene[1]
    
    # Death
    for howie in howies:
        for point in howie.genes:
            if point[1] >= 200 or point[1] <= -200 or point[0] <= -200:
                howie.fitness += -500
                break
    
    # Evaluate Fitness
    allFits = {}
    for howie in howies:
        howie.fitness += howie.endPoint[0]
        while True:
            if allFits.has_key(howie.fitness):
                howie.fitness += -1
                continue
            else:
                allFits[howie.fitness] = howie
                break
    rankedFits = allFits.keys()
    rankedFits.sort(reverse=True)       # large to small
    bests.append([])
    for gene in allFits[rankedFits[0]].genes:
        bests[-1].append(gene)
    chances[3] = allFits[rankedFits[0]].genes
    chances[2] = allFits[rankedFits[1]].genes
    chances[1] = allFits[rankedFits[2]].genes
    
    # Display Each Individual
    if display == 'individual':
        updateGen(gen)
        for howie in howies:
            displayPath(howie.genes, howie.color, 'locs')
        sleep(pause)
    
    # Display Entire Gen
    if display == 'gen':
        updateGen(gen)
        for howie in howies:
            displayPath(howie.genes, howie.color, 'path')
        sleep(pause)
  
    # Display Best of Gen
    if display == 'eachbest':
        updateGen(gen)
        displayPath(bests[-1], 'black', 'locs')
        sleep(pause)
    

# Display Bests
if display == 'allbests':
    gen = 0
    for genes in bests[:-1]:
        gen += 1
        updateGen(gen)
        count += 1
        if count >= len(colors):
            count = 0
        displayPath(genes, colors[count], 'path')
    displayPath(bests[-1], 'black', 'path')

if display == 'best':
    displayPath(bests[-1], 'black', 'locs')

"""
Large Issue Fixed:
    The genes would refernce a list instead of copying it
    so whenever one instance changed it it would change
    for all. I fixed it by copying each item individually
    into a newly created list. This took so long....
Works Perfectly as of Oct 27th 2021, 12:24 AM. 
"""
