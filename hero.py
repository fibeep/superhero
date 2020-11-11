from random import choice
from ability import Ability
from armor import Armor

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
       
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
    

    def fight(self, opponent):
        fighters = [opponent.name, self.name]
        winner = choice(fighters)
        print(f'{winner} is the winner!')

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        total_block = 0
        if self.armors != []:
            for armor in self.armors:
                total_block += armor.block()
        return total_block - damage_amt

    def take_damage(self, damage):
        injury = damage - self.defend(damage)
        self.current_health -= injury


# ---------------------------- Testing ---------------------------
# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     hero1.fight(hero2)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     ability = Ability("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(ability)
#     print(hero.abilities)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Smarty Pants", 90)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     print(hero.attack())


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    hero.take_damage(50)
    hero.take_damage(50)
    hero.take_damage(50)


    print(hero.current_health)
