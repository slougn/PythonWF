import sys

import pygame

def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rocket)

def check_keydown_events(event,rockt):
    if event.key == pygame.K_RIGHT:
        rockt.rocket_move_right = True
    if event.key == pygame.K_LEFT:
        rockt.rocket_move_left = True
    if event.key == pygame.K_DOWN:
        rockt.rocket_move_down = True
    if event.key == pygame.K_UP:
        rockt.rocket_move_up = True

def check_keyup_events(event,rockt):
    if event.key == pygame.K_RIGHT:
        rockt.rocket_move_right = False
    if event.key == pygame.K_LEFT:
        rockt.rocket_move_left = False
    if event.key == pygame.K_DOWN:
        rockt.rocket_move_down = False
    if event.key == pygame.K_UP:
        rockt.rocket_move_up = False