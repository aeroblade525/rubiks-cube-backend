from Path_Find_Algorithm.Resuable.PieceFinder import home_position_edge, edge_adjacents
from Path_Find_Algorithm.Resuable.BFSAlgorithm import moves_corresponder_bfs, shortest_path
from Path_Find_Algorithm.Edge_Pathfind.EdgeBFSMoveCorresponder import edge_map
from PythonCubeArray import cube_array_python
from Path_Find_Algorithm.Edge_Pathfind.EdgePath import edge_cube_path, coordinate_to_label, label_to_coordinate
from Cube_Algorithms.Tperm import Tperm_notation
from Path_Find_Algorithm.Edge_Pathfind.EdgeBFS import find_edge_path

def is_edge_solved(face):
    center = face[1][1]
    return (
        face[0][1] == center and
        face[2][1] == center and
        face[1][0] == center and
        face[1][2] == center
    )

def edge_solver(cube, start_pos):
    all_paths_set = set(all_paths)
    visited = set()
    original_pos = start_pos
    current_pos = start_pos
    future_pos = home_position_edge(current_pos, cube_array_python)
    paths = []
    i = 0
    visited.add('CE')
    visited.add('NE')
    for k in edge_positions:
        solved_pos = home_position_edge(k, cube_array_python)
        print(solved_pos, k)
        if solved_pos == k:
            visited.add(coordinate_to_label[k])
    
    print(current_pos, future_pos, original_pos, visited)

    while visited != all_paths_set:
        print(current_pos, future_pos, original_pos)
        print(visited, coordinate_to_label[home_position_edge(current_pos, cube_array_python)], 
              coordinate_to_label[home_position_edge(edge_adjacents[current_pos], cube_array_python)])
        
        i += 1
        if i >= 30:
            return paths
        
        edge_path = find_edge_path(cube_array_python, home_position_edge(current_pos, cube_array_python), (0, 1, 0), coordinate_to_label, edge_cube_path)

        for l in visited:
            if l == coordinate_to_label[home_position_edge(current_pos, cube_array_python)]:
                edge_path = None

        if edge_path == None:
            print("edgepath is None")

        if edge_path != None:
            visited.add(coordinate_to_label[home_position_edge(current_pos, cube_array_python)])
            visited.add(coordinate_to_label[home_position_edge(edge_adjacents[current_pos], cube_array_python)])
            edge_path_functions = moves_corresponder_bfs(edge_path, edge_map)
            paths.append(edge_path_functions)
            paths.append(Tperm_notation)
            edge_path = find_edge_path(cube_array_python, (0, 1, 0), home_position_edge(current_pos, cube_array_python), coordinate_to_label, edge_cube_path)
            edge_path_functions = moves_corresponder_bfs(edge_path, edge_map)
            paths.append(edge_path_functions)

        if (future_pos == original_pos or future_pos == edge_adjacents[original_pos]) and i != 0:
            print("run")
            for j in all_paths:
                if j == 'CE' or j == 'NE':
                    visited.add('CE')
                    visited.add('NE')
                if j not in visited:
                    print(j)
                    edge_change_path = shortest_path(edge_cube_path, j, 'AE')
                    paths.append(moves_corresponder_bfs(edge_change_path, edge_map))
                    paths.append(Tperm_notation)
                    paths.append(moves_corresponder_bfs(shortest_path(edge_cube_path, 'AE', j), edge_map))
                    # visited.add(j)
                    # visited.add(coordinate_to_label[edge_adjacents[label_to_coordinate[j]]])
                    current_pos = label_to_coordinate[j]
                    original_pos = current_pos
                    break

        current_pos = home_position_edge(current_pos, cube_array_python)
        future_pos = home_position_edge(current_pos, cube_array_python)
        print(visited, coordinate_to_label[home_position_edge(current_pos, cube_array_python)], 
              coordinate_to_label[home_position_edge(edge_adjacents[current_pos], cube_array_python)])

    return paths

all_paths = ['AE', 'BE', 'CE', 'DE', 'EE', 'FE', 'GE', 'HE', 'IE', 'JE', 'KE', 'LE', 'ME', 'NE', 'OE', 'PE', 'QE', 'RE', 'SE', 'TE', 'UE', 'VE', 'WE', 'XE']

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

print(all_paths)


# def edge_solver(cube):
#     for i in range(4):
#         path = shortest_path(
#             edge_cube_path,
#             'CE',
#             'XE'
#         )
#         print(f"Iteration {i + 1}: {path}")
#     return "Done"
# def edge_solver(cube):
#     i = 0
#     while not all(is_edge_solved(face) for face in cube):
#       if i > 4:
#         break

# print(edge_solver(cube_array_python))
    