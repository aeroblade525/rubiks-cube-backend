import copy
from Path_Find_Algorithm.Resuable.PieceFinder import home_position_edge, edge_adjacents
from Path_Find_Algorithm.Resuable.BFSAlgorithm import moves_corresponder_bfs, shortest_path
from Path_Find_Algorithm.Edge_Pathfind.EdgeBFSMoveCorresponder import edge_map
from Path_Find_Algorithm.Edge_Pathfind.EdgePath import edge_cube_path, coordinate_to_label
from Cube_Algorithms.Tperm import Tperm_notation
from Cube_Algorithms.Parity import parity_notation

all_paths_edge = ['AE', 'BE', 'CE', 'DE', 'EE', 'FE', 'GE', 'HE', 'IE', 'JE', 'KE', 'LE', 'ME', 'NE', 'OE', 'PE', 'QE', 'RE', 'SE', 'TE', 'UE', 'VE', 'WE', 'XE']

def edge_solver(cube):
    print("edgeSolver ran")
    CurrentState = copy.deepcopy(cube)
    all_paths_edge_set = set(all_paths_edge)
    visited = set()
    paths = []
    i = 0
    visited.add('CE')
    visited.add('NE')
    
    def edge_checker():
        for k in edge_positions:
            solved_pos = home_position_edge(k, CurrentState)
            if solved_pos == k:
                visited.add(coordinate_to_label[k])

    edge_checker()

    while visited != all_paths_edge_set:
        i += 1
        if i >= 20:
            return paths
        
        if (home_position_edge((0, 1, 2), CurrentState) == (0, 1, 2) or home_position_edge((0, 1, 2), CurrentState) == edge_adjacents[(0, 1, 2)]) and i != 0:
            for j in all_paths_edge:
                if j == 'CE' or j == 'NE':
                    visited.add('CE')
                    visited.add('NE')
                if j not in visited:
                    edge_checker()
                    
                    # Move new piece to buffer
                    edge_change_path = shortest_path(edge_cube_path, j, 'AE')
                    move_sequence = moves_corresponder_bfs(edge_change_path, edge_map)
                    paths.append(move_sequence)
                    for move in move_sequence:
                        CurrentState = move(CurrentState)
                    
                    # Apply T-perm
                    paths.append(Tperm_notation)
                    for move in Tperm_notation:
                        CurrentState = move(CurrentState)
                    
                    # Move back
                    edge_change_back = shortest_path(edge_cube_path, 'AE', j)
                    move_sequence = moves_corresponder_bfs(edge_change_back, edge_map)
                    paths.append(move_sequence)
                    for move in move_sequence:
                        CurrentState = move(CurrentState)
                    break
        
        edge_path = shortest_path(edge_cube_path, coordinate_to_label[home_position_edge((0, 1, 2), CurrentState)], coordinate_to_label[(0, 1, 0)])

        for l in visited:
            if l == coordinate_to_label[home_position_edge((0, 1, 2), CurrentState)]:
                edge_path = None

        if edge_path != None:
            visited.add(coordinate_to_label[home_position_edge((0, 1, 2), CurrentState)])
            visited.add(coordinate_to_label[home_position_edge(edge_adjacents[(0, 1, 2)], CurrentState)])
            
            # Move piece to buffer
            edge_path_functions = moves_corresponder_bfs(edge_path, edge_map)
            paths.append(edge_path_functions)
            for move in edge_path_functions:
                CurrentState = move(CurrentState)
            
            # Apply T-perm
            paths.append(Tperm_notation)
            for move in Tperm_notation:
                CurrentState = move(CurrentState)
            
            # Move piece back
            edge_path_reversed = edge_path[::-1]
            edge_path_functions = moves_corresponder_bfs(edge_path_reversed, edge_map)
            paths.append(edge_path_functions)
            for move in edge_path_functions:
                CurrentState = move(CurrentState)
        else:
            visited.add(coordinate_to_label[home_position_edge((0, 1, 2), CurrentState)])
            visited.add(coordinate_to_label[home_position_edge(edge_adjacents[(0, 1, 2)], CurrentState)])
    
    if (i % 2) == 1:
        paths.append(parity_notation)
        for move in parity_notation:
            CurrentState = move(CurrentState)

    print(i)

    return paths

edge_positions = [
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 2),
    (0, 2, 1),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 2),
    (1, 2, 1),
    (2, 0, 1),
    (2, 1, 0),
    (2, 1, 2),
    (2, 2, 1),
    (3, 0, 1),
    (3, 1, 0),
    (3, 1, 2),
    (3, 2, 1),
    (4, 0, 1),
    (4, 1, 0),
    (4, 1, 2),
    (4, 2, 1),
    (5, 0, 1),
    (5, 1, 0),
    (5, 1, 2),
    (5, 2, 1),
]