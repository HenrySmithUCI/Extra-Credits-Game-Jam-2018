import pygame

class InputState:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.fire = False

def Control():
    state = InputState()

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        state.left = True

    if pygame.key.get_pressed()[pygame.K_a]:
        state.left = True

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        state.right = True

    if pygame.key.get_pressed()[pygame.K_d]:
        state.right = True

    if pygame.key.get_pressed()[pygame.K_UP]:
        state.up = True

    if pygame.key.get_pressed()[pygame.K_w]:
        state.up = True

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        state.down = True

    if pygame.key.get_pressed()[pygame.K_s]:
        state.down = True

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        state.fire = True

    return state

if __name__ == "__main__":
    import __init__
    __init__.Main()
