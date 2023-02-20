from weapon import Weapon 
class Robot():
    def __init__(self) -> None:
        self.name = "Clyde"
        self.health = 150
        self.active_weapon = Weapon(70)

    def attack(self,dinosaur):
        self.health -= self.active_weapon.attack_power 
              

            