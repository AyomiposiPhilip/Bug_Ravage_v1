import pygame, os
pygame.mixer.init()

sounds = {
    "gunshot" : os.path.join('data', 'sfx', 'gun-shot.wav'),
    "gamestart" : os.path.join('data', 'sfx', 'gun-shot.wav'),
    "select" : os.path.join('data', 'sfx', 'select.wav'),
    "wrongselect" : os.path.join('data', 'sfx', 'wrong-select.mp3'),
    "levelfailed" : os.path.join('data', 'sfx', 'level-failed.mp3'),
    "levelcompleted" : os.path.join('data', 'sfx', 'level-completed.mp3'),
    "gameloaded" : os.path.join('data', 'sfx', 'game-loading.mp3'),
    "hitenemy" : os.path.join('data', 'sfx', 'hit-enemy.mp3'),
    "hitwood" : os.path.join('data', 'sfx', 'hit-wood.mp3'),
    "hitmetal" : os.path.join('data', 'sfx', 'hit-metal.mp3'),
    "cha-ching" : os.path.join('data', 'sfx', 'cha-ching.mp3'),
}


def playSound(sound_name):
    pygame.mixer.music.load(sounds[sound_name])
    pygame.mixer.music.play()
    