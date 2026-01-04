from algorithms.Path_Find_Algorithm.Path_Find_Main import solve_algorithm, solve_cube_internal
from algorithms.PythonCubeArray import cube_array_python

def main():
    # print(edge_solver(cube_array_python, (0, 1, 2)))

    print("this is the start", cube_array_python)
    print("this is the change", solve_algorithm(cube_array_python, solve_cube_internal(cube_array_python)))
    # print(home_position_corner((0, 0, 0), cube_array_python))


if __name__ == '__main__':
    main()

# # Overall Scamble partern F2 R' L2 D' B' R' F' B U' F (red front, yellow top)
