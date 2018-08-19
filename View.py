import pygame
import Model
import math
  

Red = (255,0,0)
White = (255,255,255)
Grey = (188,188,188)
Grey2 = (67,67,67)
Blue = (0,0,255)
Black = (0,0,0)

Background = Grey2


WindowSize = (1000,1000)
cameraCenter = [0,0]

class Drawer:
    def __init__(self):
        pass
    def Init(self, character):
        self.character = character
    def getPos(self):
        return [round(self.character.position.x),round(self.character.position.y)]
    def getDrawPos(self):
        return [round(self.character.position.x) + cameraCenter[0]
                ,round(self.character.position.y) + cameraCenter[1]]
    def Draw(self):
        pass
    @property
    def size(self):
        return self.character.size

class PlayerDrawer(Drawer):
    gunSize = 3
    pos = (round(WindowSize[0]/2), round(WindowSize[1]/2))
    def Draw(self, screen):
        self.DrawBody(screen)
        self.DrawWeapon(screen)
        
    def DrawBody(self, screen):
        pygame.draw.circle(screen, Red, self.pos, self.size)
        
    def DrawWeapon(self, screen):
        center = (round(math.cos(self.character.direction)*self.size+self.pos[0]),
                  round(math.sin(self.character.direction)*self.size+self.pos[0]))
        pygame.draw.circle(screen, Grey2, center, self.gunSize)

class EnemyDrawer(Drawer):
    def Draw(self, screen):
        pos = self.getDrawPos()
        pygame.draw.circle(screen, Blue, pos, self.size)

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 15)

def Initialize(screen):
    screen.fill(Background)
    pygame.display.update()

totalTime = 0
def View(screen, deltaTime): #update visuals
    screen.fill(Grey2)
    #clear screen

    Draw(screen)
    
    if(deltaTime == 0):
        deltaTime = 1
    text = font.render(str(round(1/deltaTime)), False, Grey2)
    
    screen.blit(text, (0,0))
    pygame.display.update()

def Draw(screen):
    global cameraCenter
    
    cameraCenter = [round(Model.player.position.x - WindowSize[0]/2) * -1,round(Model.player.position.y - WindowSize[1]/2) * -1]

    pygame.draw.circle(screen, Grey, cameraCenter, Model.playArea)

    pygame.draw.line(screen, Grey2,(cameraCenter[0] % WindowSize[0], 0),
                     (cameraCenter[0] % WindowSize[0],WindowSize[1]), 1)

    pygame.draw.line(screen, Grey2,((cameraCenter[0] + round(WindowSize[0]/2)) % WindowSize[0], 0),
                     ((cameraCenter[0] + round(WindowSize[0]/2)) % WindowSize[0],WindowSize[1]), 1)

    pygame.draw.line(screen, Grey2,(0, (cameraCenter[1] + round(WindowSize[1]/2)) % WindowSize[1]),
                     (WindowSize[0],(cameraCenter[1] + round(WindowSize[1]/2)) % WindowSize[1]), 1)

    pygame.draw.line(screen, Grey2,(0, cameraCenter[1] % WindowSize[1]),
                     (WindowSize[0],cameraCenter[1] % WindowSize[1]), 1)
    
    for character in Model.Character.characters:
        character.drawer.Draw(screen)

if __name__ == "__main__":
    import __init__
    __init__.Main()
