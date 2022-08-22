from asyncio.windows_events import NULL
import pygame


levelLimitedNumber = 20

levelBullets = {
    "level1": 10,
    "level2": 20,
    "level3": 20,
    "level4": 20,
    "level5": 30,
    "level6": 20,
    "level7": 35,
    "level8": 30,
    "level9": 45,
    "level10": 35,
    "level11": 75,
    "level12": 70,
    "level13": 75,
}

levelBugs = {
    "1": 1,
    "2": 3,
    "3": 4,
    "4": 5,
    "5": 4,
    "6": 3,
    "7": 5,
    "8": 4,
    "9": 8,
    "10": 7,
    "11": 15,
    "12": 10,
    "13": 18,
}


obsSize = 50
rowYPositions = {
    "firstRowY": 450,
    "secondRowY": 400,
    "thirdRowY": 350,
    "fourthRowY": 300,
    "fifthRowY": 250,
    "sixthRowY": 200,
    "seventhRowY": 150,
    "eighthRowY": 100,
}

empty_row = [0,0,0,0,0,0,0,0]
wood = 1
metal = 2
weakenemy = 3
strongenemy = 4

level1 = {
    "firstRow": [0,0,0,wood,metal,wood],
    "secondRow": [0,0,0,wood,wood,weakenemy],
    "thirdRow": [0,0,0,wood],
    "fourthRow": empty_row,
    "fifthRow": empty_row,
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level2 = {
    "firstRow": [0,0,0,wood,wood,strongenemy,metal,0],
    "secondRow": [0,0,0,wood,wood,wood,weakenemy,0],
    "thirdRow": [0,0,0,0,wood,weakenemy,0,0],
    "fourthRow": empty_row,
    "fifthRow": empty_row,
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level3 = {
    "firstRow": [0,0,metal,weakenemy,weakenemy,wood,0,0],
    "secondRow": [0,0,0,wood,wood,weakenemy,0,0],
    "thirdRow": [0,0,0,metal,weakenemy,0,0,0],
    "fourthRow": empty_row,
    "fifthRow": empty_row,
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level4 = {
    "firstRow": [0,0,wood,strongenemy,strongenemy,weakenemy,metal,0],
    "secondRow": [0,0,0,wood,wood,metal,weakenemy,0],
    "thirdRow": [0,0,0,0,weakenemy,0,0,0],
    "fourthRow": empty_row,
    "fifthRow": empty_row,
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level5 = {
    "firstRow": [0,0,metal,weakenemy,wood,wood,weakenemy,0],
    "secondRow": [0,0,wood,metal,weakenemy,metal,0,0],
    "thirdRow": [0,0,0,0,wood,metal,0,0],
    "fourthRow": [0,0,0,0,metal,weakenemy,0,0],
    "fifthRow": empty_row,
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level6 = {
    "firstRow": [0,0,0,metal,weakenemy,0,0,0],
    "secondRow": [0,0,0,metal,wood,0,0,0],
    "thirdRow": [0,0,0,metal,weakenemy,0,0,0],
    "fourthRow": [0,0,0,metal,wood,0,0,0],
    "fifthRow": [0,0,0,0,strongenemy,0,0,0],
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level7 = {
    "firstRow": [wood,weakenemy,wood,weakenemy,wood,0,0,0],
    "secondRow": [0,metal,wood,wood,strongenemy,metal,0,0],
    "thirdRow": [0,0,wood,weakenemy,wood,0,0,0],
    "fourthRow": [0,0,0,metal,strongenemy,0,0,0],
    "fifthRow": [0,0,0,0,wood,0,0,0],
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level8 = {
    "firstRow": [metal,metal,strongenemy,strongenemy,metal,wood,0,0],
    "secondRow": [metal,strongenemy,metal,wood,metal,0,0,0],
    "thirdRow": [metal,wood,metal,strongenemy,metal,0,0,0],
    "fourthRow": [0,0,0,metal,wood,0,0,0],
    "fifthRow": empty_row,
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level9 = {
    "firstRow": [metal,wood,weakenemy,wood,wood,strongenemy,weakenemy],
    "secondRow": [metal,strongenemy,wood,strongenemy,weakenemy,wood],
    "thirdRow": [metal,wood,weakenemy,wood],
    "fourthRow": [metal,strongenemy,wood],
    "fifthRow": empty_row,
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level10 = {
    "firstRow": [wood,weakenemy,wood,strongenemy,wood,wood,weakenemy],
    "secondRow": [0,wood,strongenemy,wood,wood,strongenemy],
    "thirdRow": [0,0,metal,weakenemy,wood],
    "fourthRow": [0,0,0,strongenemy],
    "fifthRow": empty_row,
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level11 = {
    "firstRow": [wood,strongenemy,strongenemy,strongenemy,weakenemy,metal,weakenemy],
    "secondRow": [wood,strongenemy,wood,wood,weakenemy,wood,wood],
    "thirdRow": [wood,wood,weakenemy,strongenemy,metal,weakenemy,wood],
    "fourthRow": [wood,wood,wood,strongenemy,metal,weakenemy,wood],
    "fifthRow": [metal,strongenemy,weakenemy,metal,wood,strongenemy],
    "sixthRow": empty_row,
    "seventhRow": empty_row,
    "eighthRow": empty_row,
}

level12 = {
    "firstRow": [metal,weakenemy,metal,strongenemy,metal,wood,strongenemy,wood],
    "secondRow": [0,metal,weakenemy,metal,metal,wood,wood],
    "thirdRow": [0,0,metal,0,metal,wood,strongenemy,wood],
    "fourthRow": [0,0,metal],
    "fifthRow": [0,wood,wood,wood],
    "sixthRow": [wood,weakenemy,weakenemy,weakenemy,wood],
    "seventhRow": [wood,weakenemy,0,weakenemy,wood],
    "eighthRow": empty_row,
}

level13 = {
    "firstRow": [wood,wood,weakenemy,weakenemy,strongenemy,weakenemy,metal,metal],
    "secondRow": [wood,weakenemy,metal,wood,wood,wood,wood,weakenemy],
    "thirdRow": [wood,wood,strongenemy,weakenemy,metal,wood,wood,weakenemy],
    "fourthRow": [wood,wood,strongenemy,metal,weakenemy,weakenemy,weakenemy],
    "fifthRow": [0,wood,wood,strongenemy,wood,wood,weakenemy],
    "sixthRow": [0,0,weakenemy,metal,strongenemy,wood],
    "seventhRow": [0,0,0,metal,weakenemy],
    "eighthRow": empty_row,
}

obsAndEnemies = []


def createWood(x_position, y_position, width, height, power):
    woodRect = pygame.Rect(x_position, y_position, width, height)
    total_pack = [woodRect, "wood", power]
    return total_pack


def createMetal(x_position, y_position, width, height, power):
    metalRect = pygame.Rect(x_position, y_position, width, height)
    total_pack = [metalRect, "metal", power]
    return total_pack


def createWeakEnemy(x_position, y_position, width, height, power):
    weakEnemyRect = pygame.Rect(x_position, y_position, width, height)
    total_pack = [weakEnemyRect, "weakenemy", power]
    return total_pack


def createStrongEnemy(x_position, y_position, width, height, power):
    strongEnemyRect = pygame.Rect(x_position, y_position, width, height)
    total_pack = [strongEnemyRect, "strongenemy", power]
    return total_pack





def load_level(level, enemy_width, enemy_height, wood_power, metal_power, weak_enemy_power, strong_enemy_power):
    level_loading = NULL
    if level == 1:
        level_loading = level1
    elif level == 2:
        level_loading = level2
    elif level == 3:
        level_loading = level3
    elif level == 4:
        level_loading = level4
    elif level == 5:
        level_loading = level5
    elif level == 6:
        level_loading = level6
    elif level == 7:
        level_loading = level7
    elif level == 8:
        level_loading = level8
    elif level == 9:
        level_loading = level9
    elif level == 10:
        level_loading = level10
    elif level == 11:
        level_loading = level11
    elif level == 12:
        level_loading = level12
    elif level == 13:
        level_loading = level13

    index = -1
    index2 = -1
    index3 = -1
    index4 = -1
    index5 = -1
    index6 = -1
    index7 = -1
    index8 = -1
    for blocks in level_loading["firstRow"]:
        index += 1
        if blocks == 1:
            x = (index * enemy_width) + 500
            wood = createWood(x, rowYPositions["firstRowY"], enemy_width, enemy_height, wood_power)
            obsAndEnemies.append(wood)
        elif blocks == 2:
            x = (index * enemy_width) + 500
            metal = createMetal(x, rowYPositions["firstRowY"], enemy_width, enemy_height, metal_power)
            obsAndEnemies.append(metal)
        elif blocks == 3:
            x = (index * enemy_width) + 500
            weakEnemy = createWeakEnemy(x, rowYPositions["firstRowY"], enemy_width, enemy_height, weak_enemy_power)
            obsAndEnemies.append(weakEnemy)
        elif blocks == 4:
            x = (index * enemy_width) + 500
            strongEnemy = createStrongEnemy(x, rowYPositions["firstRowY"], enemy_width, enemy_height, strong_enemy_power)
            obsAndEnemies.append(strongEnemy)
    
    for blocks in level_loading["secondRow"]:
        index2 += 1
        if blocks == 1:
            x = (index2 * enemy_width) + 500
            wood = createWood(x, rowYPositions["secondRowY"], enemy_width, enemy_height, wood_power)
            obsAndEnemies.append(wood)
        elif blocks == 2:
            x = (index2 * enemy_width) + 500
            metal = createMetal(x, rowYPositions["secondRowY"], enemy_width, enemy_height, metal_power)
            obsAndEnemies.append(metal)
        elif blocks == 3:
            x = (index2 * enemy_width) + 500
            weakEnemy = createWeakEnemy(x, rowYPositions["secondRowY"], enemy_width, enemy_height, weak_enemy_power)
            obsAndEnemies.append(weakEnemy)
        elif blocks == 4:
            x = (index2 * enemy_width) + 500
            strongEnemy = createStrongEnemy(x, rowYPositions["secondRowY"], enemy_width, enemy_height, strong_enemy_power)
            obsAndEnemies.append(strongEnemy)
    
    for blocks in level_loading["thirdRow"]:
        index3 += 1
        if blocks == 1:
            x = (index3 * enemy_width) + 500
            wood = createWood(x, rowYPositions["thirdRowY"], enemy_width, enemy_height, wood_power)
            obsAndEnemies.append(wood)
        elif blocks == 2:
            x = (index3 * enemy_width) + 500
            metal = createMetal(x, rowYPositions["thirdRowY"], enemy_width, enemy_height, metal_power)
            obsAndEnemies.append(metal)
        elif blocks == 3:
            x = (index3 * enemy_width) + 500
            weakEnemy = createWeakEnemy(x, rowYPositions["thirdRowY"], enemy_width, enemy_height, weak_enemy_power)
            obsAndEnemies.append(weakEnemy)
        elif blocks == 4:
            x = (index3 * enemy_width) + 500
            strongEnemy = createStrongEnemy(x, rowYPositions["thirdRowY"], enemy_width, enemy_height, strong_enemy_power)
            obsAndEnemies.append(strongEnemy)
    
    for blocks in level_loading["fourthRow"]:
        index4 += 1
        if blocks == 1:
            x = (index4 * enemy_width) + 500
            wood = createWood(x, rowYPositions["fourthRowY"], enemy_width, enemy_height, wood_power)
            obsAndEnemies.append(wood)
        elif blocks == 2:
            x = (index4 * enemy_width) + 500
            metal = createMetal(x, rowYPositions["fourthRowY"], enemy_width, enemy_height, metal_power)
            obsAndEnemies.append(metal)
        elif blocks == 3:
            x = (index4 * enemy_width) + 500
            weakEnemy = createWeakEnemy(x, rowYPositions["fourthRowY"], enemy_width, enemy_height, weak_enemy_power)
            obsAndEnemies.append(weakEnemy)
        elif blocks == 4:
            x = (index4 * enemy_width) + 500
            strongEnemy = createStrongEnemy(x, rowYPositions["fourthRowY"], enemy_width, enemy_height, strong_enemy_power)
            obsAndEnemies.append(strongEnemy)
        
    for blocks in level_loading["fifthRow"]:
        index5 += 1
        if blocks == 1:
            x = (index5 * enemy_width) + 500
            wood = createWood(x, rowYPositions["fifthRowY"], enemy_width, enemy_height, wood_power)
            obsAndEnemies.append(wood)
        elif blocks == 2:
            x = (index5 * enemy_width) + 500
            metal = createMetal(x, rowYPositions["fifthRowY"], enemy_width, enemy_height, metal_power)
            obsAndEnemies.append(metal)
        elif blocks == 3:
            x = (index5 * enemy_width) + 500
            weakEnemy = createWeakEnemy(x, rowYPositions["fifthRowY"], enemy_width, enemy_height, weak_enemy_power)
            obsAndEnemies.append(weakEnemy)
        elif blocks == 4:
            x = (index5 * enemy_width) + 500
            strongEnemy = createStrongEnemy(x, rowYPositions["fifthRowY"], enemy_width, enemy_height, strong_enemy_power)
            obsAndEnemies.append(strongEnemy)
    
    for blocks in level_loading["sixthRow"]:
        index6 += 1
        if blocks == 1:
            x = (index6 * enemy_width) + 500
            wood = createWood(x, rowYPositions["sixthRowY"], enemy_width, enemy_height, wood_power)
            obsAndEnemies.append(wood)
        elif blocks == 2:
            x = (index6 * enemy_width) + 500
            metal = createMetal(x, rowYPositions["sixthRowY"], enemy_width, enemy_height, metal_power)
            obsAndEnemies.append(metal)
        elif blocks == 3:
            x = (index6 * enemy_width) + 500
            weakEnemy = createWeakEnemy(x, rowYPositions["sixthRowY"], enemy_width, enemy_height, weak_enemy_power)
            obsAndEnemies.append(weakEnemy)
        elif blocks == 4:
            x = (index6 * enemy_width) + 500
            strongEnemy = createStrongEnemy(x, rowYPositions["sixthRowY"], enemy_width, enemy_height, strong_enemy_power)
            obsAndEnemies.append(strongEnemy)
    
    for blocks in level_loading["seventhRow"]:
        index7 += 1
        if blocks == 1:
            x = (index7 * enemy_width) + 500
            wood = createWood(x, rowYPositions["seventhRowY"], enemy_width, enemy_height, wood_power)
            obsAndEnemies.append(wood)
        elif blocks == 2:
            x = (index7 * enemy_width) + 500
            metal = createMetal(x, rowYPositions["seventhRowY"], enemy_width, enemy_height, metal_power)
            obsAndEnemies.append(metal)
        elif blocks == 3:
            x = (index7 * enemy_width) + 500
            weakEnemy = createWeakEnemy(x, rowYPositions["seventhRowY"], enemy_width, enemy_height, weak_enemy_power)
            obsAndEnemies.append(weakEnemy)
        elif blocks == 4:
            x = (index7 * enemy_width) + 500
            strongEnemy = createStrongEnemy(x, rowYPositions["seventhRowY"], enemy_width, enemy_height, strong_enemy_power)
            obsAndEnemies.append(strongEnemy)
    
    for blocks in level_loading["eighthRow"]:
        index8 += 1
        if blocks == 1:
            x = (index8 * enemy_width) + 500
            wood = createWood(x, rowYPositions["eighthRowY"], enemy_width, enemy_height, wood_power)
            obsAndEnemies.append(wood)
        elif blocks == 2:
            x = (index8 * enemy_width) + 500
            metal = createMetal(x, rowYPositions["eighthRowY"], enemy_width, enemy_height, metal_power)
            obsAndEnemies.append(metal)
        elif blocks == 3:
            x = (index8 * enemy_width) + 500
            weakEnemy = createWeakEnemy(x, rowYPositions["eighthRowY"], enemy_width, enemy_height, weak_enemy_power)
            obsAndEnemies.append(weakEnemy)
        elif blocks == 4:
            x = (index8 * enemy_width) + 500
            strongEnemy = createStrongEnemy(x, rowYPositions["eighthRowY"], enemy_width, enemy_height, strong_enemy_power)
            obsAndEnemies.append(strongEnemy)


    return obsAndEnemies