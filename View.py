import pygame
import Model
import Data

#List of Colors
Background = (0,0,0)

class Drawer:
    def __init__(self):
        pass
    
    def Init(self, character):
        self.character = character
        
    def getDrawPos(self):
        return [round(self.character.position.x),round(self.character.position.y)]
        
    def Draw(self):
        pass

class PlayerDrawer(Drawer):
    Red = (255,0,0)
    size = 50
    def Draw(self, screen):
        pygame.draw.circle(screen, self.Red, self.getDrawPos(), self.size)

class EnemyDrawer(Drawer):
    Blue = (0,0,255)
    size = 40
    def Draw(self, screen):
        pygame.draw.circle(screen, self.Blue, self.getDrawPos(), self.size)  

def View(screen): #update visuals
    screen.fill(Background)#clear screen
    Draw(screen)
    pygame.display.update()

def Draw(screen):
    for character in Data.Character.characters:
        character.Draw(screen)
