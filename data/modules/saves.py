import pygame, os, pickle

    
def set_default():
    data = {
        "playerSpriteName": "default",
        "gunSpriteName": "gun1",
        "coins": 0,
        "player_characters": ["default"],
    }
    pickle.dump(data, open(os.path.join('data', 'saves', 'saved_data.dat'), "wb"))
    
def save_data(player_sprite_name, gun_sprite_name, coins, player_characters):
    data = {
        "playerSpriteName": player_sprite_name,
        "gunSpriteName": gun_sprite_name,
        "coins": coins,
        "player_characters": player_characters,
    }
    pickle.dump(data, open(os.path.join('data', 'saves', 'saved_data.dat'), "wb"))


def load_data():
    data = pickle.load(open(os.path.join('data', 'saves', 'saved_data.dat'), "rb"))
    return data
