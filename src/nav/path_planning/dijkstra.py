import heapq
import numpy as np

from nav._tools.path_planner import PathPlanner


class Dijkstra(PathPlanner):
    
    def __init__(self, map):
        super().__init__(map)
        
    def in_bounds(self, x, y):
        return 0 <= x < self.map.shape[1] and 0 <= y < self.map.shape[0]
        
    def find_path(self, start_pose, goal_pose):
        super().find_path(start_pose, goal_pose)
        
        sx, sy = start_pose
        gx, gy = goal_pose
        
        costmap = np.full(self.map.shape, fill_value=np.inf)
        costmap[sy, sx] = 0
        
        priority_queue = []
        heapq.heappush(priority_queue, (0, start_pose))
        
        parents = dict({start_pose: start_pose})
        
        while priority_queue:
            dist, pose = heapq.heappop(priority_queue)

            for dir in self.directions:
                nbx = int(pose[0] + dir[0])
                nby = int(pose[1] + dir[1])
            
                if not self.in_bounds(nbx, nby) or self.map[nby, nbx] == 1:
                    continue
                
                if costmap[nby, nbx] > dist + 1:
                    costmap[nby, nbx] = dist + 1
                    parents[(nbx, nby)] = pose
                    heapq.heappush(priority_queue, (dist + 1, (nbx, nby)))
                    
        if costmap[gy, gx] == np.inf:
            return None

        px, py = parents[(gx, gy)]
        path = [np.array(goal_pose)]
        while (px, py) != start_pose:
            path.append((px, py))
            px, py = parents[(px, py)]
            
        path.append((px, py))
            
        return path[::-1]
    