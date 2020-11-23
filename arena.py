from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")
        return Ability(name, max_damage)

    def create_weapon(self):
        # This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        name = input("Name your weapon soldier!\n")
        max_damage = int(input("What's the max damage, big shot?\n"))
        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor object.
        #  return the new armor object with values set by user.
        name = input("What's the shield's name soldier?\n")
        max_block = input("What's the max block, big shot?\n")
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               #add an ability to the hero
               ability = self.create_ability()
               hero.add_ability(ability)
           elif add_item == "2":
               #add a weapon to the hero
               weapon = self.create_weapon()
               hero.add_weapon(weapon)
           elif add_item == "3":
               #add an armor to the hero
               armor = self.create_armor()
               hero.add_armor(armor)

        return hero
    
    # build_team is provided to you
    def build_team(self):
        name = input("What would you like to call this team?\n")
        team = Team(name)
        member_index = int(input(f"How many members would you like on {name}?\n"))
        for i in range(member_index):
            hero = self.create_hero()
            team.add_hero(hero)
        return team

    def build_team_one(self):
        self.team_one = self.build_team()

    def build_team_two(self):
        self.team_one = self.build_team()
    
    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self): 
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

    # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))


        # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()



