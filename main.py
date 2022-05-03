import random
import json

from smash import Character, Battle
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)

def character_look_up(name):
    for x in characters:
        if x["name"].lower() == name.lower():
            return x
        return None

# Player picks their character
def fight():
    fighter = {}
    comp = {}
    choice = input('Choose your fighter =>')
    if not choice:
        choice = random.choice(characters)
    print('You have chosen ' + choice)
    fighter = character_look_up(choice)
    comp = random.choice(characters)

    player = Character(fighter["name"], 100, fighter["attacks"])
    pc = Character(comp["name"], 100, comp["attacks"])
    start = Battle(player, pc)
    start.fight()
    

fight()
