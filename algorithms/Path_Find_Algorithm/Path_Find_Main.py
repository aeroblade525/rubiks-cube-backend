import copy
from ..PythonCubeArray import cube_array_python
from .Pochmann_Method.Centers import center_solver
from .Pochmann_Method.Edges import edge_solver
from .Pochmann_Method.Corners import corner_solver
from ..Cube_Turning.Cube_Turning_CCW import CubeArrayLCCW, CubeArrayBCCW, CubeArrayDCCW, CubeArrayFCCW, CubeArrayRCCW, CubeArrayUCCW, CubeArrayMCCW, CubeArraySCCW, CubeArrayECCW
from ..Cube_Turning.Cube_Turning_CW import CubeArrayLCW, CubeArrayBCW, CubeArrayDCW, CubeArrayFCW, CubeArrayRCW, CubeArrayUCW, CubeArrayMCW, CubeArraySCW, CubeArrayECW
from ..Cube_Algorithms.Common_Moves.Sexy_Move import sexy_move_algorithm
from ..Cube_Algorithms.Common_Moves.Sledge_Hammer import sledge_hammer_algorithm

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
#               CubeArrayFCW, CubeArrayFCCW, CubeArrayMCCW, CubeArrayMCW, CubeArraySCCW, CubeArraySCW, CubeArrayECCW, CubeArrayECW]

def solve_algorithm(cube, seqeunce):
    CurrentState = copy.deepcopy(cube)
    for move in seqeunce:
        CurrentState = move(CurrentState)
    return CurrentState

def solve_cube_internal(cube):
    moves_for_center = center_solver(cube)
    cube_after_center = solve_algorithm(cube, flatten(moves_for_center))

    moves_for_edges = edge_solver(cube_after_center)
    cube_after_edges = solve_algorithm(cube_after_center, flatten(moves_for_edges))

    moves_for_corners = corner_solver(cube_after_edges)

    sequence = flatten([
        moves_for_center,
        moves_for_edges,
        moves_for_corners
    ])

    return sequence

solve_cube_internal(cube_array_python)

moves_to_strings = {
    CubeArrayLCCW: "LCCW",
    CubeArrayLCW: "LCW",
    CubeArrayBCCW: "BCCW",
    CubeArrayBCW: "BCW",
    CubeArrayDCCW: "DCCW",
    CubeArrayDCW: "DCW",
    CubeArrayFCCW: "FCCW",
    CubeArrayFCW: "FCW",
    CubeArrayRCCW: "RCCW",
    CubeArrayRCW: "RCW",
    CubeArrayUCCW: "UCCW",
    CubeArrayUCW: "UCW",
    sexy_move_algorithm: "Sexy_Move",
    sledge_hammer_algorithm: "Sledge_Hammer",
    CubeArrayMCCW: "MCCW",
    CubeArrayMCW: "MCW",
    CubeArraySCCW: "SCCW",
    CubeArraySCW: "SCW",
    CubeArrayECCW: "ECCW",
    CubeArrayECW: "ECW"
}