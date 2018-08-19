import math
import random
import View

enemyCount = 50
playArea = 1000

class Transform:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

class Character:
    characters = set()
    size = 10
    def __init__(self, x, y, controller, drawer):
        self.controller = controller
        self.drawer = drawer
        self.direction = 0
        self.position = Transform(x,y)
        self.lastPos = None
        self.alive = True
        self.controller.Init(self)
        self.drawer.Init(self)
        self.characters.add(self)
        self.distances = list()

    def Update(self, deltaTime):
        self.direction %= math.pi*2
        self.GetDistances()
        self.lastPos = Transform(self.position.x, self.position.y)
        self.controller.Update(deltaTime)
        self.CheckWalls()
    
    def GetDistances(self):
        self.distances.clear()
        for character in self.characters:
            if(character != self):
                distance = character.position.distance(self.position)
                self.distances.append((distance, character))
                if(distance <= character.size + self.size):
                    self.controller.Collision(character)
        self.distances.sort()

    def CheckWalls(self):
        distanceFromCenter = (self.position.x**2+self.position.y**2)**0.5
        if(distanceFromCenter >= playArea-self.size):
            self.position = Transform(self.lastPos.x, self.lastPos.y)

    def Die(self):
        self.alive = False
        characters.remove(this)

class Controller:
    def __init__(self):
        pass
    def Init(self, character):
        self.character = character
    @property
    def position(self):
        return self.character.position
    def Update(self, deltaTime):
        pass
    def Collision(self, character):
        pass

class PlayerController(Controller):
    speed = 70
    def PlayerInput(self, inputState):
        self.inputState = inputState

    def Update(self, deltaTime):
        deltaX = 0
        deltaY = 0
        
        if(self.inputState.up):
            deltaY -= self.speed * deltaTime
        if(self.inputState.down):
            deltaY += self.speed * deltaTime
        if(self.inputState.left):
            deltaX -= self.speed * deltaTime
        if(self.inputState.right):
            deltaX += self.speed * deltaTime

        self.position.x += deltaX
        self.position.y += deltaY
        
        self.character.direction = math.atan2(deltaY, deltaX)


class EnemyController(Controller):
    turnSpeed = 0.1
    speed = 50
    randomMove = 20
    safeDistance = 150
    closeEnoughThreshhold = 0.1
    def __init__(self):
        self.targetCharacter = None
        self.targetPosition = None
        self.setRandomWaitTime()

    def Init(self, character):
        Controller.Init(self, character)
        self.character.direction = random.random()*math.pi*2
        
    def RandomPerturb(self):
        return (random.random()*self.randomMove - self.randomMove/2, random.random()*self.randomMove - self.randomMove/2)

    def setRandomWaitTime(self):
        self.targetTimer = random.random() * 10

    def Update(self, deltaTime):
        self.targetCharacter = self.character.distances[0][1]
        #print(self.position.x, self.position.y)
        #print(self.targetCharacter.position.x, self.targetCharacter.position.y)
        angle = math.atan2(self.position.y-self.targetCharacter.position.y,
                           self.position.x-self.targetCharacter.position.x)
        #print(angle)
        self.character.direction = angle
        #print(self.character.direction)
        self.position.x += math.cos(self.character.direction) * self.speed * deltaTime
        self.position.y += math.sin(self.character.direction) * self.speed * deltaTime
        '''
        if self.targetPosition == None or self.targetPosition.distance(self.position) <= self.closeEnoughThreshhold:
            self.getNewTargetPosition()
        
        self.targetTimer -= deltaTime
        if(self.targetTimer <= 0):
            self.getNewTargetPosition()
            self.setRandomWaitTime()

        
        
        if(self.character.direction <= math.pi/2 and angle >= math.pi*3/2 or
           self.character.direction >= math.pi*3/2 and angle <= math.pi/2):
             pass
        self.character.direction = angle

        
        #deltaAngle = self.character.direction - angle
        #self.character.direction += min(deltaAngle, self.turnSpeed)
            '''
        

    def getNewTargetPosition(self):
        perturb = self.RandomPerturb()
        angle = math.atan2(self.position.y-self.targetCharacter.position.y,
                           self.position.x-self.targetCharacter.position.x)
        distance = self.position.distance(self.targetCharacter.position) - self.safeDistance
        self.targetPosition = Transform(math.cos(angle)*distance + self.position.x+ perturb[0],
                                        math.sin(angle)*distance + self.position.y + perturb[1])
        
        

def Initialize():
    InitializePlayer()
    InitializeOthers()

player = None

def InitializePlayer():
    global player
    
    playerControl = PlayerController()    
    playerView = View.PlayerDrawer()

    player = Character(0, 0, playerControl, playerView)

def InitializeOthers():
    for i in range(enemyCount):
        enemyControl = EnemyController()
        enemyDrawer = View.EnemyDrawer()
        
        direction = random.random() * math.pi*2
        distance = random.random() * playArea * 0.9
        character = Character(math.cos(direction) * distance,
                  math.sin(direction) * distance,
                  enemyControl, enemyDrawer)
        enemyControl.Init(character)
        enemyDrawer.Init(character)


updateDistance = 720

def Model(deltaTime):
    for character in Character.characters:
        if(character.position.distance(player.position) < updateDistance):
            character.Update(deltaTime)

if __name__ == "__main__":
    import __init__
    __init__.Main()
            

