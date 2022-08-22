import pygame


class Bullet:
    def __init__(self, gun_x, gun_y, bullet_width, bullet_height, damage):
        self.gun_x = gun_x
        self.gun_y = gun_y
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.damage = damage

    def createBullet(self):
        bulletx = self.gun_x + 10
        bullety = self.gun_y + 10
        bulletRectangle = pygame.Rect(bulletx, bullety, self.bullet_width, self.bullet_height)
        theBullet = [bulletRectangle, self.damage]
        return theBullet
