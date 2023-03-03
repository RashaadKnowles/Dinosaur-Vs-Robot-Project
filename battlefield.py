from dinosaur import Dinosaur
from robot import Robot
class Battlefield():
    def __init__(self) -> None:
        self.robot = Robot()
        self.dinosaur = Dinosaur(70)
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to the game!!!")
    #add in extra barrier to whole loop to check if dinosaur stil has health.
    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health > 0:     
                self.dinosaur.attack(self.robot)
      
# make sure to put end of while loop in my display winner section.


    def display_winner(self):
        if  self.dinosaur.health <= 0:
                print("The Battle Has Concluded Robot Won!!")
        elif self.robot.health <= 0:
                print("The Battle Has Concluded Dinosaur Won!!")
            