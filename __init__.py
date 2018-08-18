import pygame
import Model
import View
import Control
import Data
import random

def Main():
    size = (500,500) #size of window
    targetFPS = 60

    pygame.init()
    screen = pygame.display.set_mode(size) #make window

    running = True
    clock = pygame.time.Clock() #keeps framerate synced
    
    try: #in case of error, close app
        
        player = InitializePlayer()
        InitializeOthers()
    
        while running: #main loop
        
            for event in pygame.event.get(): #check if red X is pressed to close app
                if event.type == pygame.QUIT:
                    running = False
                
            inputState = Control.Control() #get the current input state from controller
            #mainly gets key presses but can also be mouse position if necessary

            player.controller.PlayerInput(inputState)
            
            Model.Model(clock.get_time()/1000) #updates game logic
            #passes in the new input and time since last frame in seconds

            View.View(screen) #update visuals
            #passes 
        
            clock.tick(targetFPS) #wait for next frame
            
    except Exception as e: #close app on exception
        pygame.quit()
        raise e

    pygame.quit() #quit app

def InitializePlayer():
    playerControl = Data.PlayerController()    
    playerView = View.PlayerDrawer()

    player = Data.Character(200, 200, playerControl, playerView)

    return player

def InitializeOthers():
    toMake = 20
    for i in range(toMake):
        enemyControl = Data.EnemyController()
        enemyDrawer = View.EnemyDrawer()
        Data.Character(random.random() * 500, random.random() * 500, enemyControl, enemyDrawer)

if __name__ == "__main__": #main call
    Main()
