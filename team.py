import random
from hero import Hero

class Team:
    def __init__(self, name):
        
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
    
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f'{hero.name} Kill/Deaths: {kd}')

    def revive_heroes(self, starting_health=100):
        for hero in self.heroes:
            hero.current_health = starting_health

    def attack(self, other_team):
        
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)
        
        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero1 = random.choice(living_heroes)
            hero2 = random.choice(living_opponents)
            hero1.fight(hero2)
            if hero1.is_alive():
                living_opponents.remove(hero2)
            else:
                living_heroes.remove(hero1)


if __name__ == "__main__":
    team = Team("Team One")
    team.add_hero("hero1")
    team.add_hero("hero2")
    team.add_hero("hero3")
    team.view_all_heroes()


            
