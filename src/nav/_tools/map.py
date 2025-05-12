import matplotlib.pyplot as plt
import numpy as np


class Map:
    
    def __init__(self, array, block_start=False, block_goal=False, w=20, h=20, density=0.2, start_pose=(50, 50), goal_pose=(10, 10)):
        self.are_poses_drawn = False
        
        if array is not None:
            self.map = array
            return
        
        self.map = np.zeros((h, w))
        prob = np.random.random(self.map.shape)
        self.map[prob < density] = 1
        
        self.map[start_pose[1], start_pose[0]] = 255
        self.map[goal_pose[1], goal_pose[0]] = 255
        
        if block_start:
            self.map[start_pose[1]+1, start_pose[0]] = 1
            self.map[start_pose[1]-1, start_pose[0]] = 1
            self.map[start_pose[1], start_pose[0]+1] = 1
            self.map[start_pose[1], start_pose[0]-1] = 1
            
        if block_goal:
            self.map[goal_pose[1]+1, goal_pose[0]] = 1
            self.map[goal_pose[1]-1, goal_pose[0]] = 1
            self.map[goal_pose[1], goal_pose[0]+1] = 1
            self.map[goal_pose[1], goal_pose[0]-1] = 1
            
    def __getitem__(self, key):
        return self.map[key]
            
    @property
    def shape(self):
        return self.map.shape
           
    def draw(self, path, start_pose, goal_pose, show=True):
        plt.imshow(self.map, cmap='gray')
        
        if path is not None:
            xs = [p[0] for p in path]
            ys = [p[1] for p in path]
            plt.plot(xs, ys, c='b', linewidth=2, zorder=2)
        
        if not self.are_poses_drawn:
            plt.scatter(start_pose[0], start_pose[1], c='g', s=100, label=f'Start', zorder=3)
            plt.scatter(goal_pose[0], goal_pose[1], c='r', s=100, label=f'Goal', zorder=3)
        
        self.are_poses_drawn = True
        
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.tight_layout()
        if show:
            plt.show()

    @classmethod
    def from_array(cls, array : np.array):
        return Map(array=array)
    
    @classmethod
    def random(cls):
        return Map(array=None)
        

if __name__ == '__main__':
    map1 = Map()
    map1.draw()
    map2 = Map.from_array(map1.map)
    map2.draw()
    