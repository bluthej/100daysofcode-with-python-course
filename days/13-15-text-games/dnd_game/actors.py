import random
from dataclasses import dataclass


@dataclass
class Creature:
    name: str
    level: int

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level


@dataclass
class Dragon(Creature):
    scaliness: int
    breaths_fire: bool

    def defensive_roll(self):
        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breaths_fire:
            value = value * 2

        return value


@dataclass
class Wizard(Creature):
    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()

        return my_roll >= their_roll
