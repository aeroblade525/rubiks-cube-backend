import copy
from Path_Find_Algorithm.Resuable.PieceFinder import home_position_corner, corner_adjacents
from Path_Find_Algorithm.Resuable.BFSAlgorithm import moves_corresponder_bfs, shortest_path
from Path_Find_Algorithm.Corners_Pathfind.CornerBFSMoveCorresponder import corner_map
from Path_Find_Algorithm.Corners_Pathfind.CornerPath import corner_cube_path, coordinate_to_label_corners
from Cube_Algorithms.Yperm import Yperm_notation

all_paths_corner = ['AC', 'BC', 'CC', 'DC', 'EC', 'FC', 'GC', 'HC', 'IC', 'JC', 'KC', 'LC', 'MC', 'NC', 'OC', 'PC', 'QC', 'RC', 'SC', 'TC', 'UC', 'VC', 'WC', 'XC']

def corner_solver(cube):
    print("cornerSolver ran")
    CurrentState = copy.deepcopy(cube)
    all_paths_corner_set = set(all_paths_corner)
    visited = set()
    paths = []
    i = 0
    visited.add('AC')
    visited.add('RC')
    visited.add('UC')
    
    def corner_checker():
        for k in corner_positions:
            solved_pos = home_position_corner(k, CurrentState)
            if solved_pos == k:
                visited.add(coordinate_to_label_corners[k])

    corner_checker()

    while visited != all_paths_corner_set:
        i += 1
        if i >= 20:
            return paths
    
        if (home_position_corner((0, 0, 0), CurrentState) == (0, 0, 0) or home_position_corner((0, 0, 0), CurrentState) == corner_adjacents[(0, 0, 0)][0]
            or home_position_corner((0, 0, 0), CurrentState) == corner_adjacents[(0, 0, 0)][1]) and i != 0:
            for j in all_paths_corner:
                if j == 'AC' or j == 'RC' or j == 'UC':
                    visited.add('AC')
                    visited.add('RC')
                    visited.add('UC')
                if j not in visited:
                    corner_checker()
                    
                    # Move new piece to buffer
                    corner_change_path = shortest_path(corner_cube_path, j, 'DC')
                    move_sequence = moves_corresponder_bfs(corner_change_path, corner_map)
                    paths.append(move_sequence)
                    for move in move_sequence:
                        CurrentState = move(CurrentState)
                    
                    # Apply Y-perm
                    paths.append(Yperm_notation)
                    for move in Yperm_notation:
                        CurrentState = move(CurrentState)
                    
                    # Move back
                    corner_change_back = corner_change_path[::-1]
                    move_sequence = moves_corresponder_bfs(corner_change_back, corner_map)
                    paths.append(move_sequence)
                    for move in move_sequence:
                        CurrentState = move(CurrentState)
                    break
        
        corner_path = shortest_path(corner_cube_path, coordinate_to_label_corners[home_position_corner((0, 0, 0), CurrentState)], coordinate_to_label_corners[(0, 2, 2)])

        for l in visited:
            if l == coordinate_to_label_corners[home_position_corner((0, 0, 0), CurrentState)]:
                corner_path = None

        if corner_path != None:
            visited.add(coordinate_to_label_corners[home_position_corner((0, 0, 0), CurrentState)])
            visited.add(coordinate_to_label_corners[home_position_corner(corner_adjacents[(0, 0, 0)][0], CurrentState)])
            visited.add(coordinate_to_label_corners[home_position_corner(corner_adjacents[(0, 0, 0)][1], CurrentState)])
            
            # Move piece to buffer
            corner_path_functions = moves_corresponder_bfs(corner_path, corner_map)
            paths.append(corner_path_functions)
            for move in corner_path_functions:
                CurrentState = move(CurrentState)
            
            # Apply T-perm
            paths.append(Yperm_notation)
            for move in Yperm_notation:
                CurrentState = move(CurrentState)
            
            # Move piece back
            corner_path_reversed = corner_path[::-1]
            corner_path_functions = moves_corresponder_bfs(corner_path_reversed, corner_map)
            paths.append(corner_path_functions)
            for move in corner_path_functions:
                CurrentState = move(CurrentState)
        else:
            print("cornerpath is None")
            visited.add(coordinate_to_label_corners[home_position_corner((0, 0, 0), CurrentState)])
            visited.add(coordinate_to_label_corners[home_position_corner(corner_adjacents[(0, 0, 0)][0], CurrentState)])
            visited.add(coordinate_to_label_corners[home_position_corner(corner_adjacents[(0, 0, 0)][1], CurrentState)])

    return paths

corner_positions = {
    (0, 0, 0),
    (0, 0, 2),
    (0, 2, 0),
    (0, 2, 2),
    (3, 0, 0),
    (3, 0, 2),
    (3, 2, 0),
    (3, 2, 2),
    (2, 0, 0),
    (2, 0, 2),
    (2, 2, 0),
    (2, 2, 2),
    (4, 0, 0),
    (4, 0, 2),
    (4, 2, 0),
    (4, 2, 2),
    (5, 0, 0),
    (5, 0, 2),
    (5, 2, 0),
    (5, 2, 2),
    (1, 0, 0),
    (1, 0, 2),
    (1, 2, 0),
    (1, 2, 2),
}