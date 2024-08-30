from brain import Brain
from math import sqrt
blobs = []
food = []
deactiveBlobs = []
deactiveFood = []

class Blob:
    def __init__(self):
        blobs.append(self)
        self.xcor = 0
        self.ycor = 0
        self.speed = 2
        self.health = 2
        self.attack = 2
        self.color = [255, 255, 255]
        self.eaten = 0
        self.blobsKilled = 0
        self.score = 0
        self.deactivated = False
        self.network = None
    
    def goto(self, x, y):
        self.xcor = x
        self.ycor = y
        
    
    def addBrain(self, input_network):
        self.network = input_network
        self.brain = Brain(input_network)
    
    def run(self, inputs):
        try:
            outputs = self.brain.run(inputs)
        except: 
            from functions import printNetwork
            printNetwork(self.network)
        self.xcor += outputs["move_horizontally"]*self.speed
        self.ycor += outputs["move_vertically"]*self.speed
        if (self.xcor > 170):
            self.xcor = 170
        if (self.xcor < -170):
            self.xcor = -170
        if (self.ycor > 170):
            self.ycor = 170
        if (self.ycor < -170):
            self.ycor = -170
        
    def mutateNetwork(self):
        # Delete Neuron  Y/N (1/5)
        # Create Neurons Y/N (1/3)
        # Mutate Existing Weights Y/N (1/2 chance for each weight)
        pass

    def nearestFood(self):
        if len(food) == 0:
            return None
        nearest = food[0]
        nearestDistance = sqrt(abs(food[0].xcor-self.xcor)**2 + abs(food[0].ycor-self.ycor)**2)
        for fruit in food[1:]:
            distance = sqrt(abs(fruit.xcor-self.xcor)**2 + abs(fruit.ycor-self.ycor)**2)
            if (distance < nearestDistance):
                nearest = fruit
                nearestDistance = distance
        return nearest
  
    def nearestBlob(self):
        if blobs[0] == self and len(blobs) > 1:
            nearest = blobs[1]
            nearestDistance = sqrt(abs(blobs[1].xcor-self.xcor)**2 + abs(blobs[1].ycor-self.ycor)**2)
        elif len(blobs) <= 1:
            return None
        else:
            nearest = blobs[0]
            nearestDistance = sqrt(abs(blobs[0].xcor-self.xcor)**2 + abs(blobs[0].ycor-self.ycor)**2)
        for blob in blobs[1:]:
            if blob == self:
                continue
            distance = sqrt(abs(blob.xcor-self.xcor)**2 + abs(blob.ycor-self.ycor)**2)
            if (distance < nearestDistance):
                nearest = blob
                nearestDistance = distance
        return nearest
  
    def tryEat(self, food):
        distance = sqrt(abs(food.xcor-self.xcor)**2 + abs(food.ycor-self.ycor)**2)
        if distance <= 10:
            self.eaten += 1
            self.score += 1
            food.deactivate()
            return True
        else:
            return False

    def tryAttack(self, blob):
        distance = sqrt(abs(blob.xcor-self.xcor)**2 + abs(blob.ycor-self.ycor)**2)
        if distance <= 10 and (not self.deactivated):
            blob.health -= self.attack
            if blob.health <= 0:
                self.blobsKilled += 1
                self.score += (blob.eaten+blob.blobsKilled*0.5) / 2 + 0.5
                blob.deactivate()
            return True
        else:
            return False
    
    def deactivate(self):
        self.score -= 0.5
        self.deactivated = True
        deactiveBlobs.append(self)
        blobs.pop(blobs.index(self))

class Food:
    def __init__(self, x, y):
        food.append(self)
        self.xcor = x
        self.ycor = y

    def goto(self, x, y):
        self.xcor = x
        self.ycor = y
    
    def deactivate(self):
        deactiveFood.append(self)
        food.pop(food.index(self))


# Pallete
# Green:  #19c419
# Red:    #c41919
# Orange: #c46f19
# Blue:   #1919c4
