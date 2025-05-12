import cv2 as cv

from nav.path_planning.dijkstra import Dijkstra
from nav._tools.map import Map


if __name__ == '__main__':
    data = cv.imread('map.pgm', cv.IMREAD_GRAYSCALE)
    
    map = Map.from_array(array=data)
    
    start_pose = (30, 90)
    goal_pose = (120, 90)
    
    planner = Dijkstra(map)
    
    path, iters = planner.find_path(start_pose, goal_pose, show_animation=False)
    if path is None:
        print('cannot find path')
    else:    
        print('path length =', len(path), 'iterations =', iters)
    
    map.draw(path=path, start_pose=start_pose, goal_pose=goal_pose)
    