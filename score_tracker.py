from colour import RED,GREEN,BLUE,YELLOW,WHITE
class ScoreTracker:
    def __init__(self):
        self.total =0
        self.out = False

    def update_score(self,batsman_run,bowler_ball):
        if batsman_run ==bowler_ball:
            self.out = True

        else :
            self.total +=batsman_run
            print(f"{GREEN}\ntotal score : {self.total}{WHITE}")
        return self.out
