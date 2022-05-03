import random


class Character:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = moves 


    def lower_health(self, damage):
        self.health -= damage

    def attack(self):
        random.choice(self.moves)

class Battle:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two