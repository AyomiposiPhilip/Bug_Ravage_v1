import pygame, os


sprites = {
    "bullet": pygame.image.load(os.path.join('data', 'gfx', 'bullet.png')),
    "ground": pygame.image.load(os.path.join('data', 'gfx', 'ground.png')),
    "levelborder": pygame.image.load(os.path.join('data', 'gfx', 'level_bullet_border.png')),
    "bulletsborder": pygame.image.load(os.path.join('data', 'gfx', 'bullets_border.png')),
    "coinsborder": pygame.image.load(os.path.join('data', 'gfx', 'coins_border.png')),
    "splashScreenBg": pygame.image.load(os.path.join('data', 'gfx', 'splashscreen.png')),
    "palmtree": pygame.image.load(os.path.join('data', 'gfx', 'palmtree2.png')),
    "playerUsed": pygame.image.load(os.path.join('data', 'gfx', 'playerUsed.png')),
    "gunUsed": pygame.image.load(os.path.join('data', 'gfx', 'gunUsed.png')),
    "splashScreenTitle": pygame.image.load(os.path.join('data', 'gfx', 'splashscreentitle.png')),
    "levelcompleted": pygame.image.load(os.path.join('data', 'gfx', 'levelcompleted.png')),
    "levelfailed": pygame.image.load(os.path.join('data', 'gfx', 'levelfailed.png')),
}

playerSprites = {
    "default": pygame.image.load(os.path.join('data', 'gfx', 'player.png')),
    "ghost": pygame.image.load(os.path.join('data', 'gfx', 'ghost.png')),
    "grandpa": pygame.image.load(os.path.join('data', 'gfx', 'grandpa.png')),
    "butterguy": pygame.image.load(os.path.join('data', 'gfx', 'butterguy.png')),
    "bread": pygame.image.load(os.path.join('data', 'gfx', 'bread.png')),
}

gunSprites = {
    "gun1": pygame.image.load(os.path.join('data', 'gfx', 'gun1.png')),
    "gun2": pygame.image.load(os.path.join('data', 'gfx', 'gun2.png')),
    "gun3": pygame.image.load(os.path.join('data', 'gfx', 'gun3.png')),
    "gun4": pygame.image.load(os.path.join('data', 'gfx', 'gun4.png')),
}

enemySprites = {
    "wood": pygame.image.load(os.path.join('data', 'gfx', 'wood.png')),
    "metal": pygame.image.load(os.path.join('data', 'gfx', 'metal.png')),
    "woodbroken": pygame.image.load(os.path.join('data', 'gfx', 'woodbroken.png')),
    "metalbroken": pygame.image.load(os.path.join('data', 'gfx', 'metalbroken.png')),
    "weakenemy": pygame.image.load(os.path.join('data', 'gfx', 'weakenemy.png')),
    "strongenemy": pygame.image.load(os.path.join('data', 'gfx', 'strongenemy.png')),
    "weakenemybroken": pygame.image.load(os.path.join('data', 'gfx', 'weakenemybroken.png')),
    "strongenemybroken": pygame.image.load(os.path.join('data', 'gfx', 'strongenemybroken.png')),
}

buttonSprites = {
    "playButton": pygame.image.load(os.path.join('data', 'gfx', 'playButton.png')),
    "customButton": pygame.image.load(os.path.join('data', 'gfx', 'customButton.png')),
    "bigPlayButton": pygame.image.load(os.path.join('data', 'gfx', 'bigPlayButton.png')),
    "bread": pygame.image.load(os.path.join('data', 'gfx', 'useBreadButton.png')),
    "butterguy": pygame.image.load(os.path.join('data', 'gfx', 'useButterGuyButton.png')),
    "ghost": pygame.image.load(os.path.join('data', 'gfx', 'useGhostButton.png')),
    "grandpa": pygame.image.load(os.path.join('data', 'gfx', 'useGrandpaButton.png')),
    "default": pygame.image.load(os.path.join('data', 'gfx', 'useDefaultButton.png')),
    "usegun1": pygame.image.load(os.path.join('data', 'gfx', 'useGun1.png')),
    "usegun2": pygame.image.load(os.path.join('data', 'gfx', 'useGun2.png')),
    "usegun3": pygame.image.load(os.path.join('data', 'gfx', 'useGun3.png')),
    "usegun4": pygame.image.load(os.path.join('data', 'gfx', 'useGun4.png')),
    "playAgain": pygame.image.load(os.path.join('data', 'gfx', 'playAgainButton.png')),
    "nextLevel": pygame.image.load(os.path.join('data', 'gfx', 'nextLevelButton.png')),
}

