from tulip.transys import FTS
from enum import Enum

class Direction(Enum):
    N = 1
    E = 2
    S = 3
    W = 4

class Trajectory(Enum):
    Left = 1
    Straight = 2

class CarState():
    def __init__(self, id : int):

def generate_car_FTS(start_direction : Direction, trajectory : Trajectory, positionInQueue : int) -> FTS :
    ts = FTS()
    ts.add_node()