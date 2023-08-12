from turtle import Turtle

# a unit of the snake
class Segment:
    def __init__(self, initial_position) -> None:
        pass

    # return position
    def get_position(self):
        pass

    # move segment to desired coordinate
    def change_position(self, new_position):
        pass

# unit of snake that represents head
class Head(Segment):
    def __init__(self, initial_position) -> None:
        super().__init__(initial_position)

    # advanced one segment length (20px)
    def move_forward(self):
        pass

    # change direction left
    def turn_left(self):
        pass

    # change direction right
    def turn_right(self):
        pass

    # check how far an object is 
    def get_distance(self, coordinates):
        pass

    # check if crashed with wall
    def collission_wall(self):
        pass

class Snake:
    def __init__(self) -> None:
        pass

    # move entire snake forward
    def move_forward(self):
        pass

    # change directiions left
    def turn_left(self):
        pass

    # change directions right 
    def turn_right(self):
        pass

    # make snake bodoy larger when a food is eaten
    def eat_food(self):
        pass

    # check whether snake head touched food
    def detect_collission_food(self, food):
        pass
    
    # check whether snake head touched the body
    def detect_collission_self(self):
        pass

    # check whether snake touched screem edges
    def detect_collission_wall(self):
        pass
    
    # make snake revert to initial size and position
    def reset(self): 
        pass