import random 
from colour import RED,GREEN,BLUE,YELLOW,RESET

class CricketGame:
    def __init__(self):
        self.score=0
        self.out=False

    def play_ball(self):
        user_run = int(input("Enter your shot (1-6) : "))
        bowled_ball = random.randint(1, 6)

        print(f"bowler delivered : {bowled_ball}\n")

        if user_run == bowled_ball :
            print(f"{RED} OUT! bowled.....{RESET}")
            self.out=True

        else:
            self.score += user_run
            print(f"{GREEN}Nice shot! Total score : {self.score}\n{RESET}")

    def start(self):
        print("Are you ready batsman \n"
              "Hit between (1-6).\n"
              "if bowler matches the shot >> you are out!\n")
        
        while not self.out:
            try:
                self.play_ball()

            except:
                print("Bro enter a valid number")

        print(f"Your final score : {self.score}\n"
              "Thanks for playing")
        
game = CricketGame()
game.start()