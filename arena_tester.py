from characters import Character, Hero
from monster_creator import Property
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
    Hero('Max', 650, 30, 'strength', 6, 3, 1)
]

#thief = Hero('Alexa', 400, 35, 'agility', 3, 5, 2)
#defender = Hero('Max', 650, 30, 'strength', 6, 3, 1)
