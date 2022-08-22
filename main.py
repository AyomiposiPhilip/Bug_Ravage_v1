from asyncio.windows_events import NULL
import random
import pygame
import os
import sys
from data.modules.colors import colors
from data.modules.sprites import sprites, playerSprites, gunSprites, enemySprites, buttonSprites
from data.modules.player import Player
from data.modules.bullet import Bullet
from data.modules.level import levelBullets, load_level, levelBugs, levelLimitedNumber
from data.modules.gun import updateGunPosition
from data.modules.buttons import *
from data.modules.fonts import fonts, scoreFonts
from data.modules.costs import *
from data.modules.sounds import *
from data.modules.saves import save_data, set_default, load_data
import pygame.freetype
pygame.font.init()
pygame.freetype.init()
pygame.mixer.init()


# window and screen
gameScreenStuffs = {
    "width": 900,
    "height": 600,
    "splashScreen": True,
    "homeScreen": False,
    "inGameScreen": False,
    "gameOverScreen": False,
    "gameLevel": 1,
}
homeScreenStuffs = {
    "showPlay": True,
    "showCustom": False,
    "errorMessage": "",
}
window = pygame.display.set_mode((gameScreenStuffs["width"],gameScreenStuffs["height"]))
pygame.display.set_caption("Bug Ravage")


# game sprites properties
groundStuffs = {
    "width": 900,
    "height": 100,
    "x": 0,
    "y": gameScreenStuffs["height"] - 100,
}


playerStuffs = {
    "width": 64,
    "height": 64,
    "x": 5,
    "y": (gameScreenStuffs["height"] / 2) - 32,
    "number_of_bullets": 70,
}


gunStuffs = {
    "width": 48,
    "height": 48,
    "x": (playerStuffs["x"] + playerStuffs["width"]) - 10,
    "y": (playerStuffs["height"] / 2) - 24,
    "sprite_name": "gun1",
}


bulletStuffs = {
    "width": 48,
    "height": 13,
    "speed": 2,
}


enemyStuffs = {
    "width": 50,
    "height": 50,
    "woodPower": 100,
    "weakEnemyPower": 20,
    "strongEnemyPower": 70,
    "metalPower": 200,
}


levelBorderStuffs = {
    "x": 10,
    "y": groundStuffs["y"] + 20,
    "fontx": 30,
    "fonty": (groundStuffs["y"] + 20) + 15,
}


bulletsBorderStuffs = {
    "x": levelBorderStuffs["x"] + 20 + 250,
    "y": groundStuffs["y"] + 20,
    "fontx": (levelBorderStuffs["x"] + 20 + 250) + 90,
    "fonty": (groundStuffs["y"] + 20) + 17,
}


coinsBorderStuffs = {
    "x": 10,
    "y": groundStuffs["y"] + 20,
    "fontx": 75,
    "fonty": (groundStuffs["y"] + 20) + 17,
}


loadingStuffs = {
    "width": 400,
    "height": 25,
    "x": (gameScreenStuffs["width"] / 2) - 200,
    "y": 400,
}


playerUsedStuffs = {
    "x": (buyGhostButton["x"] + 300 + 200) - 100 - 32,
    "y": (buyGhostButton["y"] + 200) - 100 - 32,
}


gunUsedStuffs = {
    "x": (useGun4["x"] + 300 + 200) - 100 - 24,
    "y": ((useGun4["y"] - 50) + 150) - 90 - 24,
}


gameplayCollects = {
    "wood_destroyed": 0,
    "metal_destroyed": 0,
    "bugs_destroyed": 0,
    "total_coins": 0,
}

metalPoints = 40
woodPoints = 20
enemyPoints = 80


bullets = []
obsAndEnemies = []
loading = 0

playerData = NULL

animationCoins = 0


# draw splash screen sprites
def drawSplashScreenWindow(loadingRectangle):
    window.fill(colors["skyBlue"])
    window.blit(sprites["splashScreenTitle"], (450-300, 100))
    pygame.draw.rect(window, colors["black"], loadingRectangle)
    loadingText = fonts["font35"].render_to(window, (390, (loadingStuffs["y"] + 50)), f"LOADING...", colors["black"])
    window.blit(sprites["ground"], (groundStuffs["x"], groundStuffs["y"]))
    pygame.display.update()



# draw home screen sprites
def drawHomeScreenWindow():
    window.fill(colors["skyBlue"])
    window.blit(sprites["palmtree"], (500,0))
    
    if homeScreenStuffs["showCustom"]:
        window.blit(buttonSprites["butterguy"], (buyButterGuyButton["x"], buyButterGuyButton["y"]))
        window.blit(buttonSprites["bread"], (buyBreadButton["x"], buyBreadButton["y"]))
        window.blit(buttonSprites["ghost"], (buyGhostButton["x"], buyGhostButton["y"]))
        window.blit(buttonSprites["grandpa"], (buyGrandpaButton["x"], buyGrandpaButton["y"]))
        window.blit(buttonSprites["default"], (buyDefaultButton["x"], buyDefaultButton["y"]))
        
        window.blit(buttonSprites["usegun1"], (useGun1["x"], useGun1["y"]))
        window.blit(buttonSprites["usegun2"], (useGun2["x"], useGun2["y"]))
        window.blit(buttonSprites["usegun3"], (useGun3["x"], useGun3["y"]))
        window.blit(buttonSprites["usegun4"], (useGun4["x"], useGun4["y"]))

        window.blit(sprites["playerUsed"], ((buyGhostButton["x"] + 300), buyGhostButton["y"]))
        window.blit(sprites["gunUsed"], ((useGun4["x"] + 300), useGun4["y"] - 50))

        window.blit(playerSprites[playerData["playerSpriteName"]], (playerUsedStuffs["x"], playerUsedStuffs["y"]))
        window.blit(gunSprites[playerData["gunSpriteName"]], (gunUsedStuffs["x"], gunUsedStuffs["y"]))
        errorText = fonts["font25"].render_to(window, ((useGun1["x"]), (useGun4["y"] + 110)), f"{homeScreenStuffs['errorMessage']}", colors["darkRed"])
    elif homeScreenStuffs["showPlay"]:
        window.blit(buttonSprites["bigPlayButton"], (bigPlayButton["x"], bigPlayButton["y"]))


    window.blit(buttonSprites["playButton"], (playButton["x"], playButton["y"]))
    window.blit(buttonSprites["customButton"], (customButton["x"], customButton["y"]))
    window.blit(sprites["ground"], (groundStuffs["x"], groundStuffs["y"]))
    window.blit(sprites["coinsborder"], (coinsBorderStuffs["x"], coinsBorderStuffs["y"]))
    bulletsLeftText = fonts["font45"].render_to(window, (coinsBorderStuffs["fontx"], coinsBorderStuffs["fonty"]), f"{playerData['coins']}", colors["black"])
    pygame.display.update()



# draw end screen window
def drawEndScreenWindow():
    global animationCoins
    if gameScreenStuffs["gameLevel"] == levelLimitedNumber:
        if levelBugs[f"{gameScreenStuffs['gameLevel']}"] == gameplayCollects["bugs_destroyed"]:
            window.blit(sprites["levelcompleted"], (0,0))
            window.blit(buttonSprites["playAgain"], (levelFailPlayAgainButton["x"], levelFailPlayAgainButton["y"]))
        else:
            window.blit(sprites["levelfailed"], (0,0))
            window.blit(buttonSprites["playAgain"], (levelFailPlayAgainButton["x"], levelFailPlayAgainButton["y"]))
    else:
        if levelBugs[f"{gameScreenStuffs['gameLevel']}"] == gameplayCollects["bugs_destroyed"]:
            window.blit(sprites["levelcompleted"], (0,0))
            window.blit(buttonSprites["playAgain"], (playAgainButton["x"], playAgainButton["y"]))
            window.blit(buttonSprites["nextLevel"], (nextLevelButton["x"], nextLevelButton["y"]))
        else:
            window.blit(sprites["levelfailed"], (0,0))
            window.blit(buttonSprites["playAgain"], (levelFailPlayAgainButton["x"], levelFailPlayAgainButton["y"]))
    if animationCoins < gameplayCollects["total_coins"]:
            animationCoins += 1
    myFont = pygame.font.Font(None, 80)
    width  = myFont.size(f"{animationCoins}")[0]
    scoreText = scoreFonts["font80"].render_to(window, ((450 - (width / 2)), 350), f"{animationCoins}", colors["black"])
    pygame.display.update()



# draw in game sprites
def drawGameWindow(player, gun):
    window.fill(colors["skyBlue"])
    # draw bullets to the screen
    for bullet in bullets:
        window.blit(sprites["bullet"], (bullet[0].x, bullet[0].y))
    window.blit(gunSprites[playerData["gunSpriteName"]], (gun.x, gun.y))
    window.blit(playerSprites[playerData["playerSpriteName"]], (player.x, player.y))
    for obs in obsAndEnemies:
        window.blit(enemySprites[obs[1]], (obs[0].x, obs[0].y))
    window.blit(sprites["ground"], (groundStuffs["x"], groundStuffs["y"]))
    window.blit(sprites["levelborder"], (levelBorderStuffs["x"], levelBorderStuffs["y"]))
    window.blit(sprites["bulletsborder"], (bulletsBorderStuffs["x"], bulletsBorderStuffs["y"]))
    levelText = fonts["font50"].render_to(window, (levelBorderStuffs["fontx"], levelBorderStuffs["fonty"]), f"LEVEL {gameScreenStuffs['gameLevel']}", colors["black"])
    bulletsLeftText = fonts["font45"].render_to(window, (bulletsBorderStuffs["fontx"], bulletsBorderStuffs["fonty"]), f"{playerStuffs['number_of_bullets']}", colors["black"])
    pygame.display.update()



# move player with mouse
def playerMovement(mouse_y, player):
    if mouse_y > (playerStuffs["height"] / 2) and mouse_y < (groundStuffs["y"] - (playerStuffs["height"] / 2)):
        player.y = mouse_y - (playerStuffs["height"] / 2)



# add bullet
def createBullet(gun):
    global playerStuffs
    if len(bullets) < 2:
        playSound("gunshot")
        playerStuffs["number_of_bullets"] -= 1
        bullet = Bullet(gun.x, gun.y, bulletStuffs["width"], bulletStuffs["height"], 50)
        bulletRectDamage = bullet.createBullet()
        bullets.append(bulletRectDamage)



# move bullet
def moveBullet():
    for bullet in bullets:
        if bullet[0].x > gameScreenStuffs["width"]:
            bullets.remove(bullet)
        else:
            bullet[0].x += bulletStuffs["speed"]



# load game level
def loadLevel(level):
    global obsAndEnemies
    playerStuffs["number_of_bullets"] = levelBullets[f"level{level}"]
    obsAndEnemies = load_level(level, enemyStuffs["width"], enemyStuffs["height"], enemyStuffs["woodPower"], enemyStuffs["metalPower"], enemyStuffs["weakEnemyPower"], enemyStuffs["strongEnemyPower"])



# game collisions
def checkCollisions():
    for bullet in bullets:
        for obs in obsAndEnemies:
            if bullet[0].colliderect(obs[0]):
                if obs[1] == "wood":
                    playSound("hitwood")
                elif obs[1] == "woodbroken":
                    playSound("hitwood")
                elif obs[1] == "metal":
                    playSound("hitmetal")
                elif obs[1] == "metalbroken":
                    playSound("hitmetal")
                elif obs[1] == "strongenemy":
                    playSound("hitenemy")
                elif obs[1] == "strongenemybroken":
                    playSound("hitenemy")
                elif obs[1] == "weakenemy":
                    playSound("hitenemy")
                obs[2] = obs[2] - bullet[1]
                bullets.remove(bullet)



# update obstacles and enemylooks
def updateObsAndEnemy():
    for obs in obsAndEnemies:
        if obs[2] <= 0:
            if obs[1] == "woodbroken":
                gameplayCollects["wood_destroyed"] += 1
            elif obs[1] == "metalbroken":
                gameplayCollects["metal_destroyed"] += 1
            elif obs[1] == "strongenemybroken":
                gameplayCollects["bugs_destroyed"] += 1
            elif obs[1] == "weakenemy":
                gameplayCollects["bugs_destroyed"] += 1
            obsAndEnemies.remove(obs)
        else:
            if obs[1] == "wood":
                if obs[2] <= 50:
                    obs[1] = "woodbroken"
            elif obs[1] == "metal":
                if obs[2] <= 50:
                    obs[1] = "metalbroken"
            elif obs[1] == "strongenemy":
                if obs[2] <= 50:
                    obs[1] = "strongenemybroken"



# goto home screen by pressing [ESC] button
def gotoHomeMenu(keyPressed):
    if keyPressed[pygame.K_ESCAPE]:
        gameScreenStuffs["gameOverScreen"] = False
        gameScreenStuffs["homeScreen"] = True
        gameScreenStuffs["inGameScreen"] = False
        gameScreenStuffs["splashScreen"] = False
        homeScreenMain()



# loading
def loadingGame(loading_rect):
    global loading
    if loading_rect.width < loadingStuffs["width"]:
        loading_rect.width += 5
        pygame.time.delay(50)
    else:
        gameScreenStuffs["splashScreen"] = False
        gameScreenStuffs["inGameScreen"] = False
        gameScreenStuffs["homeScreen"] = True
        gameScreenStuffs["gameOverScreen"] = False
        homeScreenMain()



# splash screen loop
def splashScreenMain():
    loading_rect = pygame.Rect(loadingStuffs["x"], loadingStuffs["y"], 0, loadingStuffs["height"])
    while gameScreenStuffs["splashScreen"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        loadingGame(loading_rect)
        drawSplashScreenWindow(loading_rect)
    pygame.quit()



# buy player 
def buyPlayer(player_sprite_name):
    if player_sprite_name in playerData["player_characters"]:
        playerData["playerSpriteName"] = player_sprite_name
        playSound("select")
    else:
        if playerData["coins"] > playerCosts[player_sprite_name]:
            playerData["coins"] = playerData["coins"] - playerCosts[player_sprite_name]
            playerData["playerSpriteName"] = player_sprite_name
            playerData["player_characters"].append(player_sprite_name)
            save_data(playerData["playerSpriteName"], playerData["gunSpriteName"], playerData["coins"], playerData["player_characters"])
            playSound("cha-ching")
        else:
            playSound("wrongselect")
            homeScreenStuffs["errorMessage"] = f"SORRY YOU NEED {textCosts[player_sprite_name]} COINS TO USE THIS PLAYER"



# check if all enemies are destroyed or if bullets are finished
def checkForGameOver(level):
    if playerStuffs["number_of_bullets"] < 0 and gameplayCollects["bugs_destroyed"] < levelBugs[f"{level}"]:
        gameScreenStuffs["gameOverScreen"] = True
        gameScreenStuffs["homeScreen"] = False
        gameScreenStuffs["inGameScreen"] = False
        gameScreenStuffs["splashScreen"] = False
        endScreenMain()
    elif gameplayCollects["bugs_destroyed"] == levelBugs[f"{level}"]:
        gameScreenStuffs["gameOverScreen"] = True
        gameScreenStuffs["homeScreen"] = False
        gameScreenStuffs["inGameScreen"] = False
        gameScreenStuffs["splashScreen"] = False
        endScreenMain()



# home screen loop
def homeScreenMain():
    playSound("gamestart")
    while gameScreenStuffs["homeScreen"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                check_click = buttonsClick(mousex, mousey, homeScreenStuffs["showPlay"], homeScreenStuffs["showCustom"])
                if check_click == "GotoPlay":
                    homeScreenStuffs["showCustom"] = False
                    homeScreenStuffs["showPlay"] = True
                    playSound("select")
                elif check_click == "GotoCustom":
                    homeScreenStuffs["showCustom"] = True
                    homeScreenStuffs["showPlay"] = False
                    playSound("select")
                elif check_click == "PlayGame":
                    gameScreenStuffs["inGameScreen"] = True
                    gameScreenStuffs["gameOverScreen"] = False
                    gameScreenStuffs["homeScreen"] = False
                    gameScreenStuffs["splashScreen"] = False
                    inGameMain()
                elif check_click == "UseGun1":
                    playerData["gunSpriteName"] = "gun1"
                    playSound("select")
                elif check_click == "UseGun2":
                    playerData["gunSpriteName"] = "gun2"
                    playSound("select")
                elif check_click == "UseGun3":
                    playerData["gunSpriteName"] = "gun3"
                    playSound("select")
                elif check_click == "UseGun4":
                    playerData["gunSpriteName"] = "gun4"
                    playSound("select")
                elif check_click == "BuyGhost":
                    buyPlayer("ghost") # buy or use ghost
                elif check_click == "BuyBread":
                    buyPlayer("bread") # buy or use bread
                elif check_click == "BuyButterGuy":
                    buyPlayer("butterguy") # buy or use butter guy
                elif check_click == "BuyGrandpa":
                    buyPlayer("grandpa") # buy or use grandpa
                elif check_click == "BuyDefault":
                    buyPlayer("default") # buy or use default player
        
        drawHomeScreenWindow()
    pygame.quit()



# calculate coins every level
def calculate_coins():
    total = (gameplayCollects["bugs_destroyed"] * enemyPoints) + (gameplayCollects["metal_destroyed"] * metalPoints) + (gameplayCollects["wood_destroyed"] * woodPoints)
    gameplayCollects["total_coins"] = total
    return total



# end screen loop
def endScreenMain():
    coins = calculate_coins()
    playerData["coins"] = playerData["coins"] + coins
    save_data(playerData["playerSpriteName"], playerData["gunSpriteName"], playerData["coins"], playerData["player_characters"])
    if levelBugs[f"{gameScreenStuffs['gameLevel']}"] == gameplayCollects["bugs_destroyed"]:
        playSound("levelcompleted")
    else:
        playSound("levelfailed")
    while gameScreenStuffs["gameOverScreen"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if levelBugs[f"{gameScreenStuffs['gameLevel']}"] == gameplayCollects["bugs_destroyed"]:
                    check_click = endButtonClick(mousex, mousey, False)
                    if check_click == "PlayAgain":
                        gameScreenStuffs["inGameScreen"] = True
                        gameScreenStuffs["gameOverScreen"] = False
                        gameScreenStuffs["homeScreen"] = False
                        gameScreenStuffs["splashScreen"] = False
                        inGameMain()
                    elif check_click == "NextLevel":
                        gameScreenStuffs["gameLevel"] += 1
                        gameScreenStuffs["inGameScreen"] = True
                        gameScreenStuffs["gameOverScreen"] = False
                        gameScreenStuffs["homeScreen"] = False
                        gameScreenStuffs["splashScreen"] = False
                        inGameMain()
                else:
                    check_click = endButtonClick(mousex, mousey, True)
                    if check_click == "PlayAgain":
                        gameScreenStuffs["inGameScreen"] = True
                        gameScreenStuffs["gameOverScreen"] = False
                        gameScreenStuffs["homeScreen"] = False
                        gameScreenStuffs["splashScreen"] = False
                        inGameMain()
        
        keyPressed = pygame.key.get_pressed()
        gotoHomeMenu(keyPressed)
        drawEndScreenWindow()
    pygame.quit()



# reset game
def reset():
    global animationCoins
    animationCoins = 0
    obsAndEnemies.clear()
    bullets.clear()
    loadLevel(gameScreenStuffs["gameLevel"])
    gameplayCollects["bugs_destroyed"] = 0
    gameplayCollects["metal_destroyed"] = 0
    gameplayCollects["total_coins"] = 0
    gameplayCollects["wood_destroyed"] = 0



# in game loop
def inGameMain():
    reset()
    playSound("gameloaded")
    loadPlayer = Player(playerStuffs["x"], playerStuffs["y"], playerStuffs["width"], playerStuffs["height"])
    player = loadPlayer.createPlayerRect()
    while gameScreenStuffs["inGameScreen"]:
        gun = updateGunPosition(gunStuffs["width"], gunStuffs["height"], player.x, player.y, playerStuffs["width"], playerStuffs["height"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                playerMovement(mouse_y, player)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                left = pygame.mouse.get_pressed()[0]
                if left:
                    createBullet(gun)
        
        keyPressed = pygame.key.get_pressed()
        gotoHomeMenu(keyPressed)

        moveBullet()
        checkCollisions()
        updateObsAndEnemy()
        checkForGameOver(gameScreenStuffs["gameLevel"])
        drawGameWindow(player, gun)
    pygame.quit()



if __name__ == "__main__":
    if os.path.exists(os.path.join('data', 'saves', 'saved_data.dat')):
        playerData = load_data()
    else:
        set_default()
        playerData = load_data()
    splashScreenMain()