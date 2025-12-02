from batsman import Batsman
from bowler import Bowler
from score_tracker import ScoreTracker
from over_manager import OverManager
from colour import RED,GREEN,BLUE,YELLOW,WHITE

def main():
    print("---CRICKET PRIMER LEAGUE---")

    batsman = Batsman()
    bowler = Bowler()
    tracker = ScoreTracker()
    over = OverManager()

    while True :
        print(f"\n Ball {over.current_ball} of {over.max_balls}")

        
        user_run=batsman.play_shot()
        ball = bowler.Bowl_ball()
       

        out = tracker.update_score(user_run,ball)

        if out:
            print(f"{RED} you are out {WHITE}")
            break

        over.ball_bowled()

        if over.over_completed:
            print("\nover completed!")

if __name__=="__main__":
    main()
