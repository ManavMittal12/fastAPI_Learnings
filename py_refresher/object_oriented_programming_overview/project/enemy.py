class Enemy:
    def __init__(self, type_of_enemy, health_point:int=10, attack_damage:int=1):
        self.type_of_enemy: str = type_of_enemy
        self.health_point: int = health_point
        self.attack_damage: int = attack_damage
        print("New Enemy Created.")
         
        
    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight.")
        
        
    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you")
        
    
    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")