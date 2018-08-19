import pygame
import Model
import View
import Control
import random

def Main():
    targetFPS = 60

    pygame.init()
    
    screen = pygame.display.set_mode(View.WindowSize) #make window

    running = True
    clock = pygame.time.Clock() #keeps framerate synced
    
    try: #in case of error, close app
        
        Model.Initialize()
        View.Initialize(screen)
    
        while running: #main loop
        
            for event in pygame.event.get(): #check if red X is pressed to close app
                if event.type == pygame.QUIT:
                    running = False
                
            inputState = Control.Control() #get the current input state from controller
            #mainly gets key presses but can also be mouse position if necessary

            Model.player.controller.PlayerInput(inputState)

            deltaTime = clock.get_time()/1000
            
            Model.Model(deltaTime) #updates game logic
            #passes in the new input and time since last frame in seconds

            View.View(screen, deltaTime) #update visuals
        
            clock.tick(targetFPS) #wait for next frame
            
    except Exception as e: #close app on exception
        pygame.quit()
        raise e

    pygame.quit() #quit app


if __name__ == "__main__": #main call
    Main()
