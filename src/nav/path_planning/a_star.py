import heapq
import matplotlib.pyplot as plt
import numpy as np

from nav._tools.path_planner import PathPlanner, Node


class AStar(PathPlanner):
    
    def __init__(self, map, heuristic_weight=1.0):
        super().__init__(map)
        self.heuristic_weight = heuristic_weight
        
    def calc_heuristic(self, node : Node):
        return self.heuristic_weight * np.sqrt((self.goal_node.x - node.x)**2 + (self.goal_node.y - node.y)**2)
    
    def calc_cost(self, node : Node):
        return node.cost + self.calc_heuristic(node)
        
    def find_path(self, start_pose, goal_pose, show_animation=True):
        super().find_path(start_pose, goal_pose, show_animation)
        
        open_set, closed_set = dict(), dict()
        open_set[self.calc_node_idx(self.start_node)] = self.start_node
        
        iters = 0
        
        while open_set.keys():
            iters += 1
            
            idx = min(open_set.keys(), key=lambda c: self.calc_cost(open_set[c]))
            node = open_set[idx]
            
            if idx not in open_set:
                continue
            
            if show_animation:
                plt.plot(node.x, node.y, "xc")
                plt.gcf().canvas.mpl_connect('key_release_event',
                                             lambda event: [exit(
                                                 0) if event.key == 'escape' else None])
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)
            
            if node.x == self.goal_node.x and node.y == self.goal_node.y:
                self.goal_node.parent = node.parent
                self.goal_node.cost = node.cost
                break
            
            open_set.pop(idx)
            closed_set[idx] = node
            
            for motion in self.motions:
                nbx = int(node.x + motion[0])
                nby = int(node.y + motion[1])
            
                if not self.in_bounds(nbx, nby) or self.map[nby, nbx] == 0:
                    continue
                
                nb_node = Node(nbx, nby, node.cost + motion[2], node)
                nb_idx = self.calc_node_idx(nb_node)
                
                if nb_idx in closed_set:
                    continue
                
                if nb_idx not in open_set or open_set[nb_idx].cost > nb_node.cost:
                    open_set[nb_idx] = nb_node

        path = [self.goal_node.coords]
        child = self.goal_node
        while child.parent is not None:
            path.append(child.parent.coords)
            child = child.parent
            
        if start_pose in path and goal_pose in path:
            return path[::-1], iters
        return None, None
    