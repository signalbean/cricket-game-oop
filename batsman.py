class Batsman :
    def __init__ (self):
        self.score =0

    def play_shot(self):
        while True :
            try:
                shot = int(input("Enter your shot (1-6) : "))

                if 1 <= shot <= 6 :
                    return shot 
                print("That's not valid shot, please give a shot in between 1-6") # if any errer chect ones hear

            except ValueError:
                print("Enter a valid  integer.")
