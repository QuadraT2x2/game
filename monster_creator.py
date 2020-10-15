import random
from arena_test import Character, Hero
from inventory import Health_potion
import numpy as np

class Property:
    def __init__(self, name, health_bonus, attack_bonus):
        self.name = name
        self.attack_bonus = attack_bonus
        self.health_bonus = health_bonus

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

class Monster_creater:
    def __init__(self, base_character_list, property_list):
        self.base_character_list = base_character_list
        self.property_list = property_list

    def __generate_monster(self, n_properties):
        # берем случайного персонажа из списка персонажей
        person = self.base_character_list[random.randint(0, len(self.base_character_list) - 1)]
        # количество n проперти
        prop_list = (np.random.choice(self.property_list, n_properties, replace=False).tolist())
        a = len(prop_list)
        names_prop = []
        hp_bonus = 0
        att_bonus = 0
        for i in range(a):
            names_prop.append(prop_list[i].name)
            hp_bonus += prop_list[i].health_bonus
            att_bonus += prop_list[i].attack_bonus
        sort_names_prop = sorted(names_prop)
        result_name = ' '.join(sort_names_prop)
        result_name = result_name.capitalize()
        # возвращает персонажа с проп
        new_character = Character(result_name + ' ' + person.name, hp_bonus + person.max_health,
                                  att_bonus + person.get_attack_damage())
        return new_character

    def generate_monster(self):
        n_properties = random.randint(0, len(self.property_list))
        new_character = self.__generate_monster(n_properties)
        return new_character


class RandomSampler:
    def __init__(self, spisok):
        self.spisok = spisok

    def get_sample_no_replacements(self, n):
        if n > len(self.spisok):
            raise KeyError(f'ваше число n = {n} больше длины списка')
        else:
            copy_spisok = self.spisok.copy()
            result = []
            while n > 0:
                a = random.randint(0, len(copy_spisok) - 1)
                result.append(copy_spisok[a])
                copy_spisok.pop(a)
                n -= 1
            return sorted(result)

