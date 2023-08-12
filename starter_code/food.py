from turtle import  Turtle

class Food(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

    # move food to random location on screen
    def move_around(self):
        pass
    