import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Creature {self.name} of level {self.level}"

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print(f"The wizard {self.name} attacks {creature.name}!")

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(f"You roll {my_roll}.")
        print(f"{creature.name} rolls {creature_roll}.")

        if my_roll >= creature_roll:
            print(f"The wizard has triumphed over {creature.name}")
            return True
        else:
            print("The wizard has been defeated...")
            return False


class Dragon(Creature):

    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # fire_modifier = None
        # if self.breathes_fire:
        #     fire_modifer = 5
        # else:
        #     fire_modifier = 1
        # fire_modifer = VALUE_IF_TRUE if SOME_TEST else VALUE_IF_FALSE
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier = self.scaliness / 10

        return int(base_roll * fire_modifier * scale_modifier)

class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return int(base_roll / 2)
