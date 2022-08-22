import pygame
from data.modules.sprites import playerSprites


class Player:
    def __init__(self, player_x, player_y, player_width, player_height):
        self.player_x = player_x
        self.player_y = player_y
        self.player_width = player_width
        self.player_height = player_height

    def createPlayerRect(self):
        playerRectangle = pygame.Rect(self.player_x, self.player_y, self.player_width, self.player_height)
        return playerRectangle
    
