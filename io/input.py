import pygame

def user_wants_to_stop():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return True
        if event.type == pygame.QUIT:
            return True
    return False
