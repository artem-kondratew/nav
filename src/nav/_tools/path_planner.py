import numpy as np

from abc import ABC, abstractmethod

from .map import Map


class Node:
    
    def __init__(self, x, y, cost, parent):
        self.x, self.y = x, y
        self.cost = cost
        self.parent = parent
        
    def __str__(self):
        return f'node: x = {self.x}, y = {self.y}, cost = {self.cost}, parent = {self.parent if self.parent is None else self.parent.x, self.parent.y}'
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    @property
    def coords(self):
        return self.x, self.y


class PathPlanner(ABC):
    
    @abstractmethod
    def __init__(self, map : Map):
        self.map = map
        self.motions = ((1, 0, 1),
                        (1, 1, np.sqrt(2)),
                        (0, 1, 1),
                        (-1, 1, np.sqrt(2)),
                        (-1, 0, 1),
                        (-1, -1, np.sqrt(2)),
                        (0, -1, 1),
                        (1, -1, np.sqrt(2)),
 
        )

    @abstractmethod
    def find_path(self, start_pose : tuple, goal_pose : tuple, show_animation : bool):
        self.start_node = Node(start_pose[0], start_pose[1], 0, None)
        self.goal_node = Node(goal_pose[0], goal_pose[1], 0, None)
        
        if show_animation:
            self.map.draw(None, start_pose, goal_pose, False)
        
    def calc_node_idx(self, node : Node):
        return self.map.shape[1] * node.y + node.x
    
    def in_bounds(self, x, y):
        return 0 <= x < self.map.map.shape[1] and 0 <= y < self.map.map.shape[0]
    