import copy
from PythonCubeArray import cube_array_python
from Path_Find_Algorithm.Pochmann_Method.Centers import center_solver
from Path_Find_Algorithm.Pochmann_Method.Edges import edge_solver
from Path_Find_Algorithm.Pochmann_Method.Corners import corner_solver

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# sequence1d = [CubeArrayUCW, CubeArrayDCCW, CubeArrayRCW, CubeArrayBCW, CubeArrayBCW, CubeArrayFCW, CubeArrayLCCW, CubeArrayUCW, CubeArrayDCW, CubeArrayDCW,
#               CubeArrayLCCW, CubeArrayFCCW]
# sequence1d = [CubeArrayUCW, CubeArrayUCCW, CubeArrayRCW, CubeArrayRCCW, CubeArrayBCW, CubeArrayBCCW, CubeArrayDCW, CubeArrayDCCW, CubeArrayLCW, CubeArrayLCCW,
#               CubeArrayFCW, CubeArrayFCCW]

def solve_algorithm(cube, seqeunce):
    CurrentState = copy.deepcopy(cube)
    for move in seqeunce:
        CurrentState = move(CurrentState)
    return CurrentState

moves_for_center = center_solver(cube_array_python)
cube_after_center = solve_algorithm(cube_array_python, flatten(moves_for_center))
moves_for_edges = edge_solver(cube_after_center)
cube_after_edges = solve_algorithm(cube_after_center, flatten(moves_for_edges))
moves_for_corners = corner_solver(cube_after_edges)

cube_sequence = []
cube_sequence.append(moves_for_center)
cube_sequence.append(moves_for_edges)
cube_sequence.append(moves_for_corners)

sequence1d = flatten(cube_sequence)
print(sequence1d)