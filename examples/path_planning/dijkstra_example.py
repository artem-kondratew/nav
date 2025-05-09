from nav.path_planning.dijkstra import Dijkstra
from nav._tools.map import Map


if __name__ == '__main__':
    
    map = Map(block_start=False, block_goal=False)
    
    planner = Dijkstra(map)
    
    path = planner.find_path(map.start_pose, map.goal_pose)
    if path is None:
        print('cannot find path')
    
    map.set_path(path)    
    map.draw()
    