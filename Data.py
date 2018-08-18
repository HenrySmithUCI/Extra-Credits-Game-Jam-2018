import math
import random

class Transform:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

class Character:
    characters = set()
    def __init__(self, x, y, controller, drawer):
        self.controller = controller
        self.drawer = drawer
        self.position = Transform(x,y)
        self.alive = True
        self.controller.Init(self)
        self.drawer.Init(self)
        self.characters.add(self)

    def Update(self, deltaTime):
        self.controller.Update(deltaTime)

    def Draw(self, screen):
        self.drawer.Draw(screen)

    def Die():
        self.alive = False
        characters.remove(this)

class Controller:
    speed = 50
    def __init__(self):
        pass
    
    def Init(self, character):
        self.character = character
    
    def Update(self, deltaTime):
        pass

    def Move(self, x, y):
        pass

class PlayerController(Controller):
    speed = 70
    
    def PlayerInput(self, inputState):
        self.inputState = inputState

    def Update(self, deltaTime):
        if(self.inputState.up):
            self.character.position.y -= self.speed * deltaTime
        if(self.inputState.down):
            self.character.position.y += self.speed * deltaTime
        if(self.inputState.left):
            self.character.position.x -= self.speed * deltaTime
        if(self.inputState.right):
            self.character.position.x += self.speed * deltaTime


class EnemyController(Controller):
    distance = 100
    turnSpeed = 10
    randomMove = 30
    def __init__(self):
        self.target = None

    def GetClosest(self):
        closest = Character.characters[0]
        minDistance = float("inf")
        for character in Character:
            newDist = character.position.distance(self.character.position)
            if(character != self.character and newDist < minDistance):
                closest = character
                minDistance = newDist
        return closest
            

    def Update(self, deltaTime):
        '''
        if self.Target == None or not self.Target.alive:
            self.Target = self.GetClosest()
        distance =
        '''
        self.character.position.x += self.speed * deltaTime
            

