import pygame


tabButtons = {
    "width": 150,
    "height": 70,
    "defaultY": 10,
}

playButton = {
    "x": 450 - 200,
    "y": tabButtons["defaultY"],
}

customButton = {
    "x": 450 + 50,
    "y": tabButtons["defaultY"],
}

bigPlayButton = {
    "x": 450 - 150,
    "y": 300,
    "width": 300,
    "height": 70,
}

buyGrandpaButton = {
    "width": 100,
    "height": 100,
    "x": 20,
    "y": 100,
}

buyButterGuyButton = {
    "width": 100,
    "height": 100,
    "x": 140,
    "y": 100,
}

buyBreadButton = {
    "width": 100,
    "height": 100,
    "x": 260,
    "y": 100,
}

buyGhostButton = {
    "width": 100,
    "height": 100,
    "x": 380,
    "y": 100,
}

buyDefaultButton = {
    "width": 100,
    "height": 100,
    "x": 20,
    "y": 220,
}


useGun1 = {
    "width": 100,
    "height": 100,
    "x": 20,
    "y": 360,
}

useGun2 = {
    "width": 100,
    "height": 100,
    "x": 140,
    "y": 360,
}

useGun3 = {
    "width": 100,
    "height": 100,
    "x": 260,
    "y": 360,
}

useGun4 = {
    "width": 100,
    "height": 100,
    "x": 380,
    "y": 360,
}


playAgainButton = {
    "x": 350 - 200,
    "y": 450,
    "width": 200,
    "height": 70,
}

nextLevelButton = {
    "x": 550,
    "y": 450,
    "width": 200,
    "height": 70,
}


levelFailPlayAgainButton = {
    "x": 350,
    "y": 450,
    "width": 200,
    "height": 70,
}



def buttonsClick(mouse_x, mouse_y, play, custom):
    if mouse_x > bigPlayButton["x"] and mouse_x <= (bigPlayButton["x"] + bigPlayButton["width"]) and mouse_y >= bigPlayButton["y"] and mouse_y < (bigPlayButton["y"] + bigPlayButton["height"]) and play is True:
        # if the big play button is pressed
        return "PlayGame"

    elif mouse_x > playButton["x"] and mouse_x <= (playButton["x"] + tabButtons["width"]) and mouse_y >= playButton["y"] and mouse_y < (playButton["y"] + tabButtons["height"]):
        # if the play button is pressed
        return "GotoPlay"

    elif mouse_x > customButton["x"] and mouse_x <= (customButton["x"] + tabButtons["width"]) and mouse_y >= customButton["y"] and mouse_y < (customButton["y"] + tabButtons["height"]):
        # if the custom buttton is pressed
        return "GotoCustom"

    elif mouse_x > buyGhostButton["x"] and mouse_x <= (buyGhostButton["x"] + buyGhostButton["width"]) and mouse_y >= buyGhostButton["y"] and mouse_y < (buyGhostButton["y"] + buyGhostButton["height"]) and custom is True:
        # if the buy ghost button is pressed
        return "BuyGhost"
        
    elif mouse_x > buyBreadButton["x"] and mouse_x <= (buyBreadButton["x"] + buyBreadButton["width"]) and mouse_y >= buyBreadButton["y"] and mouse_y < (buyBreadButton["y"] + buyBreadButton["height"]) and custom is True:
        # if the buy bread buttton is pressed
        return "BuyBread"

    elif mouse_x > buyButterGuyButton["x"] and mouse_x <= (buyButterGuyButton["x"] + buyButterGuyButton["width"]) and mouse_y >= buyButterGuyButton["y"] and mouse_y < (buyButterGuyButton["y"] + buyButterGuyButton["height"]) and custom is True:
        # if the buy butter guy buttton is pressed
        return "BuyButterGuy"

    elif mouse_x > buyGrandpaButton["x"] and mouse_x <= (buyGrandpaButton["x"] + buyGrandpaButton["width"]) and mouse_y >= buyGrandpaButton["y"] and mouse_y < (buyGrandpaButton["y"] + buyGrandpaButton["height"]) and custom is True:
        # if the buy grandpa button is pressed
        return "BuyGrandpa"

    elif mouse_x > buyDefaultButton["x"] and mouse_x <= (buyDefaultButton["x"] + buyDefaultButton["width"]) and mouse_y >= buyDefaultButton["y"] and mouse_y < (buyDefaultButton["y"] + buyDefaultButton["height"]) and custom is True:
        # if the buy default button is pressed
        return "BuyDefault"
        
    elif mouse_x > useGun1["x"] and mouse_x <= (useGun1["x"] + useGun1["width"]) and mouse_y >= useGun1["y"] and mouse_y < (useGun1["y"] + useGun1["height"]) and custom is True:
        # if the use gun 1 buttton is pressed
        return "UseGun1"

    elif mouse_x > useGun2["x"] and mouse_x <= (useGun2["x"] + useGun2["width"]) and mouse_y >= useGun2["y"] and mouse_y < (useGun2["y"] + useGun2["height"]) and custom is True:
        # if the use gun 2 guy buttton is pressed
        return "UseGun2"

    elif mouse_x > useGun3["x"] and mouse_x <= (useGun3["x"] + useGun3["width"]) and mouse_y >= useGun3["y"] and mouse_y < (useGun3["y"] + useGun3["height"]) and custom is True:
        # if the use gun 3 button is pressed
        return "UseGun3"

    elif mouse_x > useGun4["x"] and mouse_x <= (useGun4["x"] + useGun4["width"]) and mouse_y >= useGun4["y"] and mouse_y < (useGun4["y"] + useGun4["height"]) and custom is True:
        # if the use gun 4 button is pressed
        return "UseGun4"



def endButtonClick(mouse_x, mouse_y, fail):
    if mouse_x > levelFailPlayAgainButton["x"] and mouse_x <= (levelFailPlayAgainButton["x"] + levelFailPlayAgainButton["width"]) and mouse_y >= levelFailPlayAgainButton["y"] and mouse_y < (levelFailPlayAgainButton["y"] + levelFailPlayAgainButton["height"]) and fail is True:
        # if the play again button is pressed
        return "PlayAgain"

    elif mouse_x > playAgainButton["x"] and mouse_x <= (playAgainButton["x"] + playAgainButton["width"]) and mouse_y >= playAgainButton["y"] and mouse_y < (playAgainButton["y"] + playAgainButton["height"]) and fail is False:
        # if the play again button is pressed
        return "PlayAgain"
    
    elif mouse_x > nextLevelButton["x"] and mouse_x <= (nextLevelButton["x"] + nextLevelButton["width"]) and mouse_y >= nextLevelButton["y"] and mouse_y < (nextLevelButton["y"] + nextLevelButton["height"]) and fail is False:
        # if the next level button is pressed
        return "NextLevel"