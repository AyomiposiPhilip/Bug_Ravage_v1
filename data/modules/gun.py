import pygame


def updateGunPosition(gun_width, gun_height, player_x, player_y, player_width, player_height):
    new_gun_x = (player_x + player_width) - 20
    new_gun_y = (player_y + (gun_height / 2)) - 10
    gunRectangle = pygame.Rect(new_gun_x, new_gun_y, gun_width, gun_height)
    return gunRectangle