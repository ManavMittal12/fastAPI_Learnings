from enemy import Enemy
import random


class Zombie(Enemy):
    def __init__(self, health_point: int = 10, attack_damage: int = 1):
        super().__init__(enemy_name="Zombie", health_point=health_point, attack_damage=attack_damage)
        
        
    @staticmethod
    def talk():
        print("*Grumbling*")        # Method Overriding
        
    
    @staticmethod
    def spread_disease():
        print("The Zombi is trying to spread infection.")
        
    
    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_point += 2
            print("Zombie Regenerated 2 HP!")