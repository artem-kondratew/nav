from abc import ABC, abstractmethod

from .map import Map

class PathPlanner(ABC):
    
    @abstractmethod
    def __init__(self, map):
        self.map = map.map if type(map) == Map else map
        self.directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    
    @abstractmethod
    def find_path(self, start_pose : tuple, goal_pose : tuple):
        pass
    