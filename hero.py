from random import choice
class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
    
        '''Instance properties: 
            name: String
            starting_health: Integer
            current_health: Integer
        '''        

    # we know the name of our hero, so we assign it here
        self.name = name
    # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def fight(self, opponent):
        number1 = choice([self.name, opponent.name])
        print(f"{number1} won!")


# if __name__ == "__main__":
# # If you run this file from the terminal
# # this block is executed.
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)


if __name__ == "__main__":
    hero1 = Hero("BobbySuckerpunch")
    hero2 = Hero("Superhumanman")
    hero1.fight(hero2)