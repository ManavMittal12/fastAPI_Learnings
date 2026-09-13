from enemy import Enemy
import random

class Ogre(Enemy):
    def __init__(self, health_point = 20, attack_damage = 2):
        super().__init__(enemy_name="Ogre",health_point=health_point, attack_damage=attack_damage)
        

    @staticmethod
    def talk():
        print("Ogre is slamming hands all around.")     # Method Overriding.
        
    
    def special_attack(self):
            did_special_attack_work = random.random() < 0.20
            if did_special_attack_work:
                self.health_point += 4
                print("Ogre attack has increased by 4")