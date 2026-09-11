class Enemy:
    def __init__(self, type_of_enemy, health_point:int=10, attack_damage:int=1):
        self.__type_of_enemy: str = type_of_enemy
        self.health_point: int = health_point
        self.attack_damage: int = attack_damage
        print("New Enemy Created.}")
         
    # using getters and setters
    @property
    def type_of_enemy(self):
        return self.__type_of_enemy
        
        
    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight.")
        
        
    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")
        
    
    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")