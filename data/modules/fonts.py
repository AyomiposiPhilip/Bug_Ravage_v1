import os
import pygame
import pygame.freetype
pygame.freetype.init()


fonts = {
    "font10": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 10),
    "font15": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 15),
    "font20": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 20),
    "font25": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 25),
    "font30": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 30),
    "font35": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 35),
    "font40": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 40),
    "font45": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 45),
    "font50": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 50),
    "font55": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 55),
    "font60": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 60),
    "font65": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 65),
    "font70": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 70),
    "font75": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 75),
    "font80": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 80),
    "font85": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 85),
    "font90": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 90),
    "font95": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 95),
    "font100": pygame.freetype.Font(os.path.join('data', 'fonts', 'GameFont.ttf'), 100),
}

scoreFonts = {
    "font10": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 10),
    "font15": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 15),
    "font20": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 20),
    "font25": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 25),
    "font30": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 30),
    "font35": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 35),
    "font40": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 40),
    "font45": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 45),
    "font50": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 50),
    "font55": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 55),
    "font60": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 60),
    "font65": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 65),
    "font70": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 70),
    "font75": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 75),
    "font80": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 80),
    "font85": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 85),
    "font90": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 90),
    "font95": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 95),
    "font100": pygame.freetype.Font(os.path.join('data', 'fonts', 'ScoreFont.ttf'), 100),
}