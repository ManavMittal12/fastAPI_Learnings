from zombie import Zombie
from ogre import Ogre


zombie = Zombie()
print(f"The enemy is a {zombie.enemy_name}, It has a total health of {zombie.health_point} and \
total damage it does is {zombie.attack_damage}")


zombie.walk_forward()
zombie.talk()
zombie.spread_disease()

ogre = Ogre(health_point=20, attack_damage=3)
print(f"The enemy is a {ogre.enemy_name}, It has total healt of {ogre.health_point} and \
total damage it does is {ogre.attack_damage}")

ogre.talk()


