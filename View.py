import pygame
import Model

Background = (0,0,0)
Red = (255,0,0)
Grey = (188,188,188)
Blue = (0,0,255)

WindowSize = (500,500)
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

class PlayerDrawer(Drawer):
    gunSize = 3
    
    def Draw(self, screen):
        pos = (round(WindowSize[0]/2), round(WindowSize[1]/2))
        pygame.draw.circle(screen, Red, pos, self.character.size)
        gunSquare = pygame.Rect(2,2, self.gunSize, self.gunSize)
        pygame.draw.rect(screen,  Grey, gunSquare)

class EnemyDrawer(Drawer):
    def Draw(self, screen):
        pygame.draw.circle(screen, Blue, self.getDrawPos(), self.character.size)  

font = None

def Initialize():
    global font
    font = pygame.font.SysFont('Comic Sans MS', 30)


def View(screen, FPS): #update visuals
    screen.fill(Background)#clear screen
    Draw(screen)
    text = font.render(FPS, False, (255,255,0))
    screen.blit(text, (0,0))
    pygame.display.update()

def Draw(screen):
    global cameraCenter
    cameraCenter = [-1 * a for a in Model.player.drawer.getPos()]
    for character in Model.Character.characters:
        character.Draw(screen)

if __name__ == "__main__":
    import __init__
    __init__.Main()
