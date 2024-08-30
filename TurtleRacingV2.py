# https://trinket.io/python/9604c81609

import turtle, time, random
r = turtle.Turtle()
y = turtle.Turtle()
b = turtle.Turtle()
g = turtle.Turtle()
t = [r,y,b,g]
rp = 0
yp = 0
bp = 0
gp = 0
p = [rp, yp, bp, gp]
colors = ["firebrick", "dark orange", "dark turquoise", "green"]
colornames = ["Red ","Orange ", "Blue ", "Green "]
x = -150

r.speed(100)
for num1 in range(-1, 2, 2):
  r.penup()
  r.goto((150*num1) , 200)
  r.pendown()
  r.goto((150*num1) , (-200))
r.penup()
r.goto(0,0)
r.speed(3)

for i in range(len(t)):
  r = t[i]
  r.shape("turtle")
  r.penup()
  r.color(colors[i])
  r.goto(-180,x)
  x += 100

def racingaction():
  while True:
    for num2 in range(len(t)):
      rand = random.randint(0, (len(t)-1))
      r2 = t[rand]
      r2.forward(random.randint(20,35))
      if r2.xcor() > 150:
        print(colornames[rand]+"Won!")
        p[rand] += 1
        return False

while True:
  if input("Start(end)-") == "end":
    break
  for back in range(len(t)):
    r = t[back]
    r.setx(-180)
  print("----------")
  time.sleep(1)
  racingaction()
for points in range(len(p)):
  colorp = p[3-points]
  print(colornames[3-points]+"- "+str(colorp))
