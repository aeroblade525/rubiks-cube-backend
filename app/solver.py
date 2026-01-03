from algorithms.Path_Find_Algorithm.Path_Find_Main import solve_cube_internal

def solve_cube(input_cube: list[list[list[int]]]) -> list:
    #convert input in 
    sequence = solve_cube_internal(input_cube)
    # solve_algorithm(input)
    return sequence
