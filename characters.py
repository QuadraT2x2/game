import random
from inventory import Inventory, Health_potion
from images import unknown


def calculate_agi_diff_bonus(self, other, max_bonus, agi_to_bonus_coefficient):
    agility_scores = [x.agility if isinstance(x, Hero) else 0
                      for x in [self, other]]

    agi_diff = (agility_scores[0] - agility_scores[1]) / agi_to_bonus_coefficient

    agi_diff_limited = min(max(agi_diff, -max_bonus), max_bonus)

    return agi_diff_limited


def attack_first(self, other):
    # возможные значения: [-0.05, 1.05)
    chance = random.random() - calculate_agi_diff_bonus(self, other, max_bonus=0.05, agi_to_bonus_coefficient=1000)
    if chance <= 0.5:
        return True
    else:
        return False
    return (chance <= 0.5)


class Character():
    def __init__(self, name, max_health, attack_damage, image=None):
        self.name = name
        self.max_health = max_health
        self.__attack_damage = attack_damage
        if image is None:
            self.image = unknown
        self.__current_health = max_health
        self.is_alive = True

    def __repr__(self):
        return f'''Character "{self.name}". {self.get_attack_damage()} attack
{self.__current_health} out of {self.max_health} health'''

    def get_attack_damage(self):
        return self.__attack_damage

    def attack(self, other):
        if self.is_alive:
            if other.is_alive:
                damage = self.get_attack_damage()
                print(f'{self.name} viciously attacks {other.name} for {damage} damage')
                other.take_damage(damage)
            else:
                print(f'{self.name} will not attack an unconscious {other.name}')
        else:
            print(f'{self.name} is unconscious and can\'t attack {other.name}')

    def take_damage(self, damage):
        self.__current_health = self.__current_health - damage
        if self.__current_health <= 0:
            self.__current_health = 0
            self.is_alive = False
            print(f'{self.name} can\'t take it any longer and faints')

    def take_healing(self, heal):
        self.__current_health = min(self.__current_health + heal, self.max_health)
        if self.is_alive is False and heal > 0:
            self.is_alive = True
            print(f'{self.name} recovered and is now capable of fighting')

    def fight(self, other):
        print(f'{self.__repr__()}\n is fighting \n{other.__repr__()}')
        print('\n*** FIGHT! ***\n')

        while self.is_alive and other.is_alive:
            if attack_first(self, other):
                self.attack(other)
            else:
                other.attack(self)

        winner = self if self.is_alive else other

        print(f'The winner in battle is {winner.name} with {winner.__current_health} health points left !')


class Hero(Character):
    def __init__(self, name, max_health, attack_damage, image, main_att, strength, agility, intelligence):
        if main_att not in ['strength', 'agility', 'intelligence']:
            raise ValueError(
                f"Main attribute must be one of 'strength', 'agility', 'intelligence'. Main_att parameter was *'{main_att}'* ")
        self.main_att = main_att
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.inventory = Inventory()
        hp_bonus = 20 * strength
        super().__init__(name, max_health + hp_bonus, attack_damage, image)

    def try_to_drink_health_potion(self):
        for x in self.inventory.items:
            if isinstance(x, Health_potion):
                self.take_healing(x.heal)
                self.inventory.drop_first_item_by_name(x.name)
                break

    def get_attack_damage(self):
        return super().get_attack_damage() + getattr(self, self.main_att)
