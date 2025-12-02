class OverManager:
    def __init__(self):
        self.current_ball =0
        self.max_balls=6
        self.over_completed = False

    def ball_bowled(self):
        self.current_ball +=1
        if self.current_ball >= self.max_balls:
            self.over_completed=True

    def reset_over(self):
        self.current_ball = 0
        self.over_completed=False
