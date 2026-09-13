from zombie import Zombie
from ogre import Ogre
from enemy import Enemy
from hero import Hero
from weapon import Weapon

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
    while e1.health_point > 0 and e2.health_point > 0:
        print("-"*10)
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.enemy_name}: {e1.health_point} HP left")
        print(f"{e2.enemy_name}: {e2.health_point} HP left")
        e2.attack()
        e1.health_point -= e2.attack_damage
        e1.attack()
        e2.health_point -= e1.attack_damage
        
    print("-"*10)
    
    if e1.health_point > 0:
        print(f"{e1.enemy_name} wins!")
    else:
        print(f"{e2.enemy_name} wins! ")
    

def hero_battle(hero: Hero, enemy: Enemy):
    enemy.talk()
    enemy.special_attack()
    while hero.health_point > 0 and enemy.health_point > 0:
        print("-"*10)
        print(f"Hero: {hero.health_point} HP left")
        print(f"{enemy.enemy_name}: {enemy.health_point} HP left")
        enemy.attack()
        hero.health_point -= enemy.attack_damage
        hero.attack()
        enemy.health_point -= hero.attack_damage
        
    print("-"*10)
    
    if hero.health_point > 0:
        print(f"Hero wins!")
    else:
        print(f"{enemy.enemy_name} wins! ")
 



zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

hero = Hero(10, 1)
weapon = Weapon("Sword", 6)
hero.weapon = weapon
hero.equip_weapon()

# battle(zombie, ogre)
hero_battle(hero, ogre)
