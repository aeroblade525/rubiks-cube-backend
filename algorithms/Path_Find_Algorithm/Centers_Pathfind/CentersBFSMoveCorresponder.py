from ...Cube_Turning.Cube_Turning_CCW import CubeArrayMCCW, CubeArrayECCW, CubeArraySCCW
from ...Cube_Turning.Cube_Turning_CW import CubeArrayMCW, CubeArrayECW, CubeArraySCW

center_map = {
    (0, 1): CubeArraySCCW,
    (0, 3): CubeArrayMCW,
    (0, 4): CubeArraySCW,
    (0, 5): CubeArrayMCCW,
    (1, 0): CubeArraySCW,
    (1, 2): CubeArraySCCW,
    (1, 3): CubeArrayECW,
    (1, 5): CubeArrayECCW,
    (2, 1): CubeArraySCW,
    (2, 3): CubeArrayMCCW,
    (2, 4): CubeArraySCCW,
    (2, 5): CubeArrayMCW,
    (3, 0): CubeArrayMCCW,
    (3, 1): CubeArrayECCW,
    (3, 2): CubeArrayMCW,
    (3, 4): CubeArrayECW,
    (4, 0): CubeArraySCCW,
    (4, 2): CubeArraySCW,
    (4, 3): CubeArrayECCW,
    (4, 5): CubeArrayECW,
    (5, 0): CubeArrayMCW,
    (5, 1): CubeArrayECW,
    (5, 2): CubeArrayMCCW,
    (5, 4): CubeArrayECCW
}
