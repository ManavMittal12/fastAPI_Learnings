# Enemy is the parent class, also known as super class
class Enemy:
    def __init__(self, enemy_name: str, health_point: int = 10, attack_damage: int = 1):
        self.__enemy_name: str = enemy_name
        self.health_point: int = health_point
        self.attack_damage: int = attack_damage
        
         
    # using getters and setters
    @property
    def enemy_name(self):
        return self.__enemy_name
        
    
    @staticmethod
    def talk():
        print("I am an Enemy")
        
        
    def walk_forward(self):
        print(f"{self.__enemy_name} moves closer to you")
        
    
    def attack(self):
        print(f"{self.__enemy_name} attacks for {self.attack_damage} damage")
        
    
    def special_attack(self):
        print("Enemy has no special attack")
        
