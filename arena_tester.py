from characters import Character, Hero
from monster_creator import Property, Monster_creater
import numpy as np


properties = [
    Property('survivalist', 140, 0),
    Property('strong', 0, 25),
    Property('berserk', -100, 50),
    Property('elite', 200, 30),
    Property('weak', -30, -10)
]

characters = [
    Character('cat', 50, 15),
    Character('dog', 70, 10),
    Character('chicken', 60, 20),
    Character('dragon', 150, 40),
    Character('tiger', 100, 30)
]

heroes = [
    Hero('Alexa', 400, 35, 'agility', 3, 5, 2),
    Hero('Max', 650, 30, 'strength', 6, 3, 1),
    Hero('Furion', 350, 25, 'intelligence', 2, 4, 7)
]

#thief = Hero('Alexa', 400, 35, 'agility', 3, 5, 2)
#defender = Hero('Maximus', 650, 30, 'strength', 6, 3, 1)
#prophet = Hero('Furion', 350, 25, 'intelligence', 2, 4, 7)

create_5_monsters_no_prop = (np.random.choice(characters, 5).tolist())
print(create_5_monsters_no_prop, end='\n'+'*' * 30+'\n')

create_25_monsters = [Monster_creater(characters, properties).generate_monster() for i in range(25)]
print(create_25_monsters)
