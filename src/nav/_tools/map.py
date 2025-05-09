import matplotlib.pyplot as plt
import numpy as np


class Map:
    
    DEFAULT_DENSITY = 0.2
    
    def __init__(self, block_start=False, block_goal=False):
        w, h = 20, 20
        
        self.start_pose = (16, 5)
        self.goal_pose = (5, 17)
        
        self.map = np.zeros((h, w))
        prob = np.random.random(self.map.shape)
        self.map[prob < Map.DEFAULT_DENSITY] = 1
        
        self.map[self.start_pose[1], self.start_pose[0]] = 0
        self.map[self.goal_pose[1], self.goal_pose[0]] = 0
        
        if block_start:
            self.map[self.start_pose[1]+1, self.start_pose[0]] = 1
            self.map[self.start_pose[1]-1, self.start_pose[0]] = 1
            self.map[self.start_pose[1], self.start_pose[0]+1] = 1
            self.map[self.start_pose[1], self.start_pose[0]-1] = 1
            
        if block_goal:
            self.map[self.goal_pose[1]+1, self.goal_pose[0]] = 1
            self.map[self.goal_pose[1]-1, self.goal_pose[0]] = 1
            self.map[self.goal_pose[1], self.goal_pose[0]+1] = 1
            self.map[self.goal_pose[1], self.goal_pose[0]-1] = 1
        
        self.path = None
        
    def set_path(self, path):
        self.path = path

    def draw(self):
        plt.imshow(self.map, cmap="gray_r")
        
        if self.path is not None:
            xs = [p[0] for p in self.path]
            ys = [p[1] for p in self.path]
            plt.plot(xs, ys, c='b', linewidth=2, zorder=1)
            
        plt.scatter(self.start_pose[0], self.start_pose[1], c='g', s=100, label='Start', zorder=2)
        plt.scatter(self.goal_pose[0], self.goal_pose[1], c='r', s=100, label='Goal', zorder=2)
        
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.tight_layout()
        plt.show()
        
    @classmethod
    def from_array(cls, array : np.array):
        obj = cls()
        obj.map = array
        return obj
        

if __name__ == '__main__':
    map1 = Map()
    map1.draw()
    map2 = Map.from_array(map1.map)
    map2.draw()
    