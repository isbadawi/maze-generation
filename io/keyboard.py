import pygame

def user_pressed_escape():
    for event in pygame.event.get():
        return event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
