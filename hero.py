from random import choice
from weapon import Weapon
from ability import Ability
from armor import Armor


class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
    
        '''Instance properties: 
            name: String
            starting_health: Integer
            current_health: Integer
        '''        
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

        self.deaths = 0
        self.kills = 0

    # def fight(self, opponent):
    #     number1 = choice([self.name, opponent.name])
    #     print(f"{number1} won!")

    def add_ability(self, ability):
    # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)
    
    def attack(self):
      '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
      '''

      # start our total out at 0
      total_damage = 0
        # loop through all of our hero's abilities
      for ability in self.abilities:
            # add the damage of each attack to our running total
        total_damage += ability.attack()
        # return the total damage
        return total_damage


    def add_armor(self, armor):
    # Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    def fight(self, opponent):
        attacker = self
        enemy = opponent
        #check if at least one hero has abilities. If no hero has abilities, print "Draw"
        if self.abilities == 0 and opponent.abilities == 0:
            return "It's a Draw!"
        #else, start the fighting loop until a hero has won
        while self.is_alive() and opponent.is_alive():
        #the hero (self) and their opponent must attack each other and each must take damage from the other's attack
            enemy.take_damage(attacker.attack())
            attacker, enemy = enemy, attacker
        #After each attack, check if either the hero (self) or the opponent is alive
        enemy.add_kill()
        attacker.add_death()
        #if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        print(f"{enemy.name} won agains {attacker.name}!")
        return enemy, attacker

    def defend(self, damage_amt):
        # TODO: This method should run the block method on each armor in self.armors
        if damage_amt == None:
            damage_amt = 0
            for armor in self.armors:
                damage_amt += armor.max_block
            print(damage_amt)
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        if total_block > damage_amt:
            total_block = damage_amt
        return total_block
    def take_damage(self, damage):
  # Create a method that updates self.current_health to the current
  # minus the the amount returned from calling self.defend(damage).
        self.current_health -= damage - self.defend(damage)
    
    def is_alive(self):
  # Check the current_health of the hero.
  # if it is <= 0, then return False. Otherwise, they still have health
  # and are therefore alive, so return True
        return self.current_health > 0
    
    def add_kill(self, num_kills=1):
        self.kills += num_kills
    def add_death(self, num_deaths = 1):
        self.deaths += num_deaths






#Part 1 name
# if __name__ == "__main__":
# # If you run this file from the terminal
# # this block is executed.
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)

#Part 2
# if __name__ == "__main__":
#     hero1 = Hero("BobbySuckerpunch")
#     hero2 = Hero("Superhumanman")
#     hero1.fight(hero2)

#Part 3
# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     ability = Ability("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     print(hero.abilities)

#Part 4
# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Smarty Pants", 90)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     print(hero.attack())

#Part4 take damage

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.

#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(hero.current_health)

#Part4 isAlive

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero = Hero("Grace Hopper", 200)
#     hero.take_damage(150)
#     print(hero.is_alive())
#     hero.take_damage(15000)
#     print(hero.is_alive())

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)

#Part5 

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     hero = Hero("Wonder Woman")
#     weapon = Weapon("Lasso of Truth", 90)
#     hero.add_weapon(weapon)
#     print(hero.attack())

#Part 6

def __init__(self, name, health=100):
    # The code you have already written goes here.
    # ...
    self.deaths = 0
    self.kills = 0