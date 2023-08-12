from turtle import Turtle 

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

    # method to write score
    def write_score(self):
       pass

    # increase the score by one and write the new score
    def increment_score(self):
        pass

    # game over screen
    def write_game_over(self):
        pass
 
    # revert to initial scoreboard 
    def reset(self):
        pass