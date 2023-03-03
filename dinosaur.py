class Dinosaur():
    def __init__(self, attack_power) -> None:
        self.name = "Bonnie"
        self.attack_power = 85
        self.health = 200

    def attack(self, robot):
        robot.health -= self.attack_power  
        
