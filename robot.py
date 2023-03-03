from weapon import Weapon 
class Robot():
    def __init__(self) -> None:
        self.name = "Clyde"
        self.health = 150
        self.active_weapon = Weapon(70)
        # Instead of setting robot weapon to an integer I set it to the class weapon itself.

    def attack(self,dinosaur):
        dinosaur.health -= self.active_weapon.attack_power 
              

            