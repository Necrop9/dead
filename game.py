import math
import random
class Hero:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self, opponent):
        opponent.health -= self.damage
    def power_attack(self, opponent):
        opponent.health -= self.damage + self.damage

    def special_attack(self, opponent):
        opponent.health -= self.damage*3
        self.health -= self.damage

    hero_count = 0
    attack_limit = 5

class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self, opponent):
        opponent.health -= self.damage

    def power_attack(self, opponent):
        opponent.health -= self.damage + self.damage

    def special_attack(self, opponent):
        opponent.health -= self.damage * 3
        self.health -= self.damage

    enemy_count = 0
    enemy_limit = 5


hero = Hero(100, 20)
enemy = Enemy(100, 20)


def question(hero,enemy):
    answer = input("Who do u want to attack?\n(a) Hero\n(b) Villain\n(c) both \n\n")
    if answer == "b":
        if hero.hero_count < hero.attack_limit:
            answer2 = input("chose type of attack\n(a) normal attack\n(b) power attack\n(c) special attack\n\n")
            if answer2 == "a":
                print("Attacks used " + str(hero.hero_count) + "/" + str(hero.attack_limit))
                hero.attack(enemy)
                hero.hero_count += 1
            elif answer2 == "b":
                if hero.hero_count  <= hero.attack_limit -2:
                    hero.power_attack(enemy)
                    hero.hero_count += 2
                    print("Used  " + str(hero.hero_count) + " / " + str(hero.attack_limit) + " turns")
                else:
                    print("Out of stamina")
                    hero.hero_count -= 2
            elif answer2 == "c":
                if hero.hero_count <= hero.attack_limit -3:
                    hero.special_attack(enemy)
                    hero.hero_count += 3
                    print("Used  " + str(hero.hero_count) + " / " + str(hero.attack_limit) + " turns")
                    print("Hero health " + str(hero.health))
                else:
                    print("Out of stamina")
                    hero.hero_count -= 3


        else:
            print("Out of mana")
        print("Villain health " + str(enemy.health))

        if enemy.health <= 0:
            print("Villain is dead :) ")
            if enemy.health <=0 and hero.health >=1:
                answer3 = input("Do you want to kill Hero too?\n(a) Yes\n(b) No\n\n ")
                if answer3 == "a":
                    while hero.health >=1:
                        question(hero , enemy)
                        enemy.enemy_count -= 5
                        hero.hero_count -= 5
                elif answer3 == "b":
                    print("Hero lives , you are a great man")          #HG


    elif answer == "a":
        if enemy.enemy_count <= enemy.enemy_limit:
            answer2 = input("chose type of attack\n(a) normal attack\n(b) power attack\n(c) special attack\n\n")
            if answer2 == "a":
                if enemy.enemy_count <= enemy.enemy_limit - 1:
                    enemy.attack(hero)
                    enemy.enemy_count += 1
                    print("Attacks used " + str(enemy.enemy_count) + "/" + str(enemy.enemy_limit))
                    print("Hero health " + str(hero.health))
                    print("Villain  health " + str(enemy.health))


                else:
                    print("Out of stamina")
                    enemy.enemy_count -= 1


            elif answer2 == "b":
                if enemy.enemy_count <= enemy.enemy_limit - 2:
                    enemy.power_attack(hero)
                    enemy.enemy_count += 2
                    print("Attacks used " + str(enemy.enemy_count) + "/" + str(enemy.enemy_limit))
                    print("Hero health " + str(hero.health))
                    print("Villain health " + str(enemy.health))
                else:
                   print("Out of stamina")
                   enemy.enemy_count -= 2



            elif answer2 == "c":
                if enemy.enemy_count <= enemy.enemy_limit - 3:
                    enemy.special_attack(hero)
                    enemy.enemy_count += 3
                    print("Used  " + str(enemy.enemy_count) + " / " + str(enemy.enemy_limit) + " turns")
                    print ("Hero health " + str(hero.health))
                    print("Villain health " + str(enemy.health))

                else:
                    print("Out of stamina")
                    enemy.enemy_count -= 3

        if hero.health <= 0:
            print("Hero is  is dead  ")
            if hero.health <= 0 and enemy.health >= 1:
                answer3 = input("Do you want to kill Villain too?\n(a) Yes\n(b) No  \n\n ")
                if answer3 == "a":
                    while enemy.health >= 1:
                        question(hero, enemy)
                        enemy.enemy_count -= 5
                        hero.hero_count -= 5
                elif answer3 == "b":
                    print("Ok , you chose...")

                elif answer3 == "b":
                    print("Game is over")




    elif answer == "c":

        hero.attack(enemy) or enemy.attack(hero)
        print("Villain health " + str(enemy.health))
        print("Hero health " + str(hero.health))



    if hero.health <= 0 and enemy.health <= 0:
        print("they are both dead , are u happy now?")
    if hero.health <=0:
        print("Hero is dead")
    if enemy.health <= 0:
        print("Villain is dead")


while hero.health >=1 and enemy.health>=1:
    question(hero,enemy)
if hero.health <=1 and enemy.health <=1:
    print("Game over")
