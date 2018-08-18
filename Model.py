import math
import random
import View

enemyCount = 100
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
    speed = 50
    def __init__(self, x, y, controller, drawer):
        self.controller = controller
        self.drawer = drawer
        self.position = Transform(x,y)
        self.alive = True
        self.controller.Init(self)
        self.drawer.Init(self)
        self.characters.add(self)
        self.distances = list()

    def Update(self, deltaTime):
        self.GetDistances()
        self.controller.Update(deltaTime)
    
    def GetDistances(self):
        self.distances.clear()
        for character in self.characters:
            distance = character.position.distance(self.position)
            self.distances.append((distance, character))
            if(distance <= character.size + self.size):
                self.controller.Collision(character)

    def Draw(self, screen):
        self.drawer.Draw(screen)

    def Die():
        self.alive = False
        characters.remove(this)

class Controller:
    def __init__(self):
        pass
    
    def Init(self, character):
        self.character = character
    
    def Update(self, deltaTime):
        pass

    def Collision(self, character):
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
    turnSpeed = 10
    randomMove = 20
    def __init__(self):
        self.targetPosition = None
            
    def RandomPerturb(self):
        return (random.random()*randomMove, random.random()*randomMove)

    def Update(self, deltaTime):
        pass
        #if self.Target == None or not self.Target.alive:
        #    self.Target = self.GetClosest()
        #    self.TargetPosition = 
        #distance = self.Target.position.distance(self.character.position)

def Initialize():
    InitializePlayer()
    InitializeOthers()

player = None

def InitializePlayer():
    global player
    
    playerControl = PlayerController()    
    playerView = View.PlayerDrawer()

    player = Character(200, 200, playerControl, playerView)

def InitializeOthers():
    for i in range(enemyCount):
        enemyControl = EnemyController()
        enemyDrawer = View.EnemyDrawer()
        Character(random.random() * playArea,
                  random.random() * playArea,
                  enemyControl, enemyDrawer)


def Model(deltaTime):
    for character in Character.characters:
        character.Update(deltaTime)

if __name__ == "__main__":
    import __init__
    __init__.Main()
            

