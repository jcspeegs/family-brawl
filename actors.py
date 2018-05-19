import collections
import random


class Creature:
    def __init__(self, name: str, level: int, attack_type: str):
        self.name = name
        self.level = level
        self.attack_type = attack_type

    def __repr__(self):
        return "Creature: {} of level {} with attack_type: {}" \
            .format(self.name, self.level, self.attack_type)

    def get_defensive_roll(self):
        return self.level * random.randint(1, 12)


class Hero(Creature):
    def defeat(self, target):
        attack_strength = self.get_defensive_roll()
        target_strength = target.get_defensive_roll()
        print('You attack with {} damage...'.format(attack_strength))
        print('{} {}s with {} damage...'.format(target.name, target.attack_type, target_strength))
        return attack_strength >= target_strength


class Dog(Creature):
    def __init__(self, name: str, level: int, attack_type: str, crazy: bool):
        name_desc = 'crazy {}'.format(name) if crazy else name
        self.name = name_desc
        self.level = level
        self.attack_type = attack_type
        self.crazy = crazy

    def get_defensive_roll(self):
        crazy_mod = 10 if self.crazy else 1
        return super().get_defensive_roll() * crazy_mod


class Parent(Creature):
    def __init__(self, name: str, level: int, attack_type: str, mood):
        self.mood = mood
        self.mood_val = collections.namedtuple('moods', ['angry', 'tired', 'happy'])(5, 3, 1)
        # self.mood must be int
        self.name = '{} {}'.format(self.mood_val._fields[self.mood], name)
        self.level = level
        self.attack_type = attack_type

    def get_defensive_roll(self):
        # Use this assignment if you pass mood string in initializer
        # moody_mod = getattr(self.mood_val, self.mood)

        # Use this assignment if you pass index in initializer
        moody_mod = self.mood_val[self.mood]
        return super().get_defensive_roll() * moody_mod
