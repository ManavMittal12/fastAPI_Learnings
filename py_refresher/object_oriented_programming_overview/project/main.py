from enemy import Enemy


zombie = Enemy("Zombie")
print(f"{zombie.type_of_enemy} has {zombie.health_point} health points and can do an attack \
of {zombie.attack_damage}")

zombie.talk()
zombie.walk_forward()
zombie.attack()

stronger_zombie = Enemy("Ultra Zombie", 15, 3)
print(f"{stronger_zombie.type_of_enemy} has {stronger_zombie.health_point} health points and can do an attack \
of {stronger_zombie.attack_damage}")