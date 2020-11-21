from characters import Character, Hero
from monster_creator import Property, Monster_creater
from inventory import Health_potion
from images import kitten, pooch, cock, viper, tigress, assasin, warrior, prophet
import numpy as np


properties = [
    Property('survivalist', 140, 0),
    Property('strong', 0, 25),
    Property('berserk', -100, 50),
    Property('elite', 200, 30),
    Property('weak', -30, -10)
]

characters = [
    Character('cat', 50, 15, kitten),
    Character('dog', 70, 10, pooch),
    Character('chicken', 60, 20, cock),
    Character('dragon', 150, 40, viper),
    Character('tiger', 100, 30, tigress)
]
'''
heroes = [
    Hero('Alexa', 400, 35, 'agility', 3, 5, 2, assasin),
    Hero('Max', 650, 30, 'strength', 6, 3, 1, warrior),
    Hero('Furion', 350, 25, 'intelligence', 2, 4, 7, prophet)
]
'''
thief = Hero('Alexa', 400, 35, 'agility', 3, 5, 2, assasin)
defender = Hero('Maximus', 650, 30, 'strength', 6, 3, 1, warrior)
prophet = Hero('Furion', 350, 25, 'intelligence', 2, 4, 7, prophet)

create_5_monsters_no_prop = (np.random.choice(characters, 5).tolist())
print(create_5_monsters_no_prop, end='\n'+'*' * 30+'\n')

monster_creater = Monster_creater(characters, properties)
create_25_monsters = [monster_creater.generate_monster() for i in range(25)]
print(create_25_monsters)

potion = Health_potion('potion of healing', 30)
thief.inventory.add_item(potion)
thief.inventory.add_item(potion)
thief.inventory.add_item(potion)
print(thief.inventory)

create_5_monsters_no_prop[0].fight(thief)

thief.try_to_drink_health_potion()
print(thief.inventory)
print(thief)
