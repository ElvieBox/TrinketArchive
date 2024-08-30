import turtle, random, time

#Notes:
  #- First Pillar -USED TO- Doesn't Have Collison (It's a "feature", not a bug, yeah, meant it that way)
  #- Space to jump
  
  #-2nd turtle doesn't have collision

# Setup:
pillarSpeed = 18  #Increases/Decreases the distance in which each pillar moves left
DevMode = False   #False = PlayerMode, can end game   True = no end
flappy = turtle.Turtle()
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
colluemTurtles = [t, t1, t2]
flappy.speed(6)

wall = turtle.Screen()
#wall.delay(1) #--------------------------------------------------Added in after
gravity = 7  #Change this to change how fast it falls
jumpHeight = 2  #Change this to change high flappy jumps
flappyFacing = 0
acceleration = 0
accelerationIncrease = 0

pastHeight = 0

# Bars + Others setup
for x, y in ((-1, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)):
  if x == y:
    flappy.penup()
  else:
    flappy.pendown()
  flappy.goto(200*x , 180*y)

for i, turt in ((67, t), (-67, t1), (-200, t2)):
  turt.speed(1000)
  turt.penup()
  turt.goto(i, 180)
  turt.right(90)

# Functions
def colluemHeight(lastH, turt):
  global pastHeight
  global heights
  while True:
    roll = random.randint(-140, 140)
    if abs(pastHeight-roll) >= 200 or abs(pastHeight-roll) <= 30:
      continue
    else:
      pastHeight = roll
      try:
        heights[turt] = roll
      except:
        pass
      return roll

def colluemPrint(turt, height):
  for i in [1, -1]:
    turt.pendown()
    turt.goto(turt.xcor() , height+(37*i))
    turt.right(90)
    turt.forward(25)
    turt.right(90)
    turt.goto(turt.xcor() , (180* i))
    turt.penup()
    turt.goto(turt.xcor() , -180)
  turt.goto(turt.xcor() , 180)


def flap():
  global acceleration
  global accelerationIncrease
  #global flappyFacing
  acceleration = -3   # Change this also
  accelerationIncrease = -2
  
  for i in range(jumpHeight):
    if i <= jumpHeight/4:
      flappy.goto(0, flappy.ycor()+i )
      #flappyFacing += i
      time.sleep(.005)
    elif i+(jumpHeight/3+4) > jumpHeight:  #Also change +?
      flappy.goto(0, flappy.ycor()+jumpHeight-i)
      #flappyFacing += jumpHeight-i
    else:
      flappy.goto(0, flappy.ycor()+jumpHeight/2)
      #flappyFacing += jumpHeight/2
    #flappy.setheading(flappyFacing)
  
#   time.sleep(.2)
    
# function dependendent variables:
heights = {
  t : colluemHeight(pastHeight, t),
  t1 : colluemHeight(pastHeight, t1),
  t2 : colluemHeight(pastHeight, t2)
  }

#----------------


#Setup Loop
mark1 = time.time()
flappy.speed(500)
instanceTime = 8     #Change this to adjust the bird to wall update ratio
flappy.goto(0,0)
instanceTimeTracker = 0
end = False

# Main Loop
while True:
  if instanceTimeTracker > instanceTime:
    mark1 = time.time()
    instanceTimeTracker = 0
    
    #Background Moves:
    for tempT in colluemTurtles:
      tempT.clear()
      colluemPrint(tempT, heights[tempT])
      if tempT.xcor() <= -200:
        tempT.goto(200, 180)
        colluemHeight(pastHeight, tempT)
        pillarSpeed += .5
      else:
        tempT.goto(tempT.xcor()-pillarSpeed , 180)
    
    
    

  else:
    #Bird's Move---v
    instanceTimeTracker += 1
    
    accelerationIncrease += 1

    if accelerationIncrease == gravity:
      accelerationIncrease = 0
      acceleration += 2
  
    if flappy.ycor() <= -180:
      flappy.goto(0,-180)
      acceleration = 0
      accelerationIncrease = 0
    elif flappy.ycor() >= 175:
      flappy.goto(0, 170)
      accelerationIncrease += -1
    else:
      if flappyFacing > -75:
        #flappyFacing += -5
        #flappy.setheading(flappyFacing)
        pass
    
  
    flappy.goto(0 , flappy.ycor()-acceleration )
  
    wall.onkey( flap , "Space")
    wall.listen()
    #time.sleep(.2)

    #Bird Updates
    
    
  if DevMode == False:
    for turtTest in colluemTurtles: #Look for issue
      if (turtTest.xcor()+pillarSpeed-25 <= 0) and (turtTest.xcor()+pillarSpeed >= 0 ):
        if flappy.ycor() >= heights[turtTest] +37 or flappy.ycor() <= heights[turtTest]-37:
          end = True
  
  if end == True:
    break
  
    
  time.sleep(.01)

#Ending
responces = ["pro tip: only the tip of the arrow is tested", "tip: the first pillar can't affect you (totally not a glitch)- Beta","Uh oh, you booped the pillar too hard", "ouch", "Flappy, flappy, flappy of the turtle watch out for that pil---! crash!%", "boop", "why are you even playing this?", "crash!", "<sarcastic responce here>", "flappy hit the ground too hard", "-You Died- (ominous dark souls music)", "its 11:31 please send help-dev", "9% battery-dev", "pro tip: press space to jump", "Acheivement Gained: Rare Death Message", "I put a typo somewhere in here and am too lazy to correct it", "Game Over", "Maybe Try Again?", "wow", "good luck next time", "please don't quit my game", "that looked like it hurt", "so how was your day?", "good day to you- butler", "just try it again, probally was a glitch", "there are no accidents- master ouigway", "*flap, *flap, *frantic flap, *splat", "this took too long", "sorry, no scores are implimented yet"]
print(random.choice(responces))


