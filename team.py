import random
class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()


    def remove_hero(self, name):
        foundHero = False
    # loop through each hero in our list
        for hero in self.heroes:
        # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
            # set our indicator to True
                foundHero = True
    # if we looped through our list and did not find our hero,
    # the indicator would have never changed, so return 0
        if not foundHero:
            return 0
    
    def view_all_heroes(self):
    # Loop over the list of heroes and print their names to the terminal one by one.
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))
    
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    
    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            #index of all the super heroes
            player = random.randint(0, len(living_heroes)-1)
            player2 = random.randint(0, len(living_opponents)-1)

            living_heroes[player].fight(living_opponents[player2])
            if not living_heroes[player].is_alive():
                living_heroes.remove(player)
            elif not living_opponents[player2].is_alive():
                living_opponents.remove(player2)

    

