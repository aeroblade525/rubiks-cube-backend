from algorithms.Path_Find_Algorithm.Path_Find_Main import solve_cube_internal, moves_to_strings

def solve_cube(input_cube: list[list[list[int]]]) -> list:
    #convert input in 
    sequence = solve_cube_internal(input_cube)
    sequence_list_str = []
    for i in sequence:
        sequence_list_str.append(moves_to_strings[i])
    # solve_algorithm(input)
    return sequence_list_str
