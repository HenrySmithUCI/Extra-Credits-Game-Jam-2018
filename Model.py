import Data
import View
import Control

def Model(deltaTime):
    for character in Data.Character.characters:
        character.Update(deltaTime)
    
