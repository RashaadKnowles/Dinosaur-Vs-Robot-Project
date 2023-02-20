from dinosaur import Dinosaur
from robot import Robot
class Battlefield():
    def __init__(self) -> None:
        self.robot = Robot()
        self.dinosaur = Dinosaur(70)
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print("Welcome to the game!!!")
    
    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.attack(self.dinosaur) 
            self.dinosaur.attack(self.robot)
        if  self.dinosaur.health <= 0:
                print("The Battle Has Concluded Robot Won!!")
        elif self.robot.health <= 0:
                print("The Battle Has Concluded Dinosaur Won!!")



    def display_winner(self):
        pass