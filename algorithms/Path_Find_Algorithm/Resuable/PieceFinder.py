edge_adjacents = {
    (0, 1, 0): (1, 0, 1),
    (0, 0, 1): (5, 0, 1),
    (0, 1, 2): (4, 0, 1),
    (0, 2, 1): (3, 0, 1),
    (1, 1, 0): (5, 1, 2),
    (1, 0, 1): (0, 1, 0),
    (1, 1, 2): (3, 1, 0),
    (1, 2, 1): (2, 1, 0),
    (2, 1, 0): (1, 2, 1),
    (2, 0, 1): (3, 2, 1),
    (2, 1, 2): (4, 2, 1),
    (2, 2, 1): (5, 2, 1),
    (3, 1, 0): (1, 1, 2),
    (3, 0, 1): (0, 2, 1),
    (3, 1, 2): (4, 1, 0),
    (3, 2, 1): (2, 0, 1),
    (4, 1, 0): (3, 1, 2),
    (4, 0, 1): (0, 1, 2),
    (4, 1, 2): (5, 1, 0),
    (4, 2, 1): (2, 1, 2),
    (5, 1, 0): (4, 1, 2),
    (5, 0, 1): (0, 0, 1),
    (5, 1, 2): (1, 1, 0),
    (5, 2, 1): (2, 2, 1),
}

# Corner adjacents - each corner position maps to its two adjacent positions
corner_adjacents = {
    (0, 0, 0): [(5, 0, 2), (1, 0, 0)],  # AC
    (0, 0, 2): [(5, 0, 0), (4, 0, 2)],  # BC
    (0, 2, 0): [(3, 0, 0), (1, 0, 2)],  # CC
    (0, 2, 2): [(3, 0, 2), (4, 0, 0)],  # DC

    (3, 0, 0): [(0, 2, 0), (1, 0, 2)],  # EC
    (3, 0, 2): [(0, 2, 2), (4, 0, 0)],  # FC
    (3, 2, 0): [(1, 2, 2), (2, 0, 0)],  # GC
    (3, 2, 2): [(4, 2, 0), (2, 0, 2)],  # HC

    (2, 0, 0): [(3, 2, 0), (1, 2, 2)],  # IC
    (2, 0, 2): [(3, 2, 2), (4, 2, 0)],  # JC
    (2, 2, 0): [(1, 2, 0), (5, 2, 2)],  # KC
    (2, 2, 2): [(4, 2, 2), (5, 2, 0)],  # LC

    (4, 0, 0): [(0, 2, 2), (3, 0, 2)],  # MC
    (4, 0, 2): [(0, 0, 2), (5, 0, 0)],  # NC
    (4, 2, 0): [(2, 0, 2), (3, 2, 2)],  # OC
    (4, 2, 2): [(2, 2, 2), (5, 2, 0)],  # PC

    (5, 0, 0): [(0, 0, 2), (4, 0, 2)],  # QC
    (5, 0, 2): [(0, 0, 0), (1, 0, 0)],  # RC
    (5, 2, 0): [(2, 2, 2), (4, 2, 2)],  # SC
    (5, 2, 2): [(2, 2, 0), (1, 2, 0)],  # TC

    (1, 0, 0): [(0, 0, 0), (5, 0, 2)],  # UC
    (1, 0, 2): [(0, 2, 0), (3, 0, 0)],  # VC
    (1, 2, 0): [(2, 2, 0), (5, 2, 2)],  # WC
    (1, 2, 2): [(2, 0, 0), (3, 2, 0)],  # XC
}

def center_find_peice(color, cube):
    for i in range(len(cube)):
        if cube[i][1][1] == color:
            return i

def home_position_edge(edge_position, cube_array):

    if edge_position not in edge_adjacents:
        return f"Edge position {edge_position} not recognized."

    face1, row1, col1 = edge_position
    face2, row2, col2 = edge_adjacents[edge_position]

    color1 = cube_array[face1][row1][col1]
    color2 = cube_array[face2][row2][col2]

    for pos, adj in edge_adjacents.items():
        f1, r1, c1 = pos
        f2, r2, c2 = adj
        center1 = cube_array[f1][1][1]
        center2 = cube_array[f2][1][1]

        if set([color1, color2]) == set([center1, center2]):
            if center1 == color1:
                return pos
            elif center2 == color1:
                return adj
    return "Home position not found."

def home_position_corner(corner_position, cube_array):
    if corner_position not in corner_adjacents:
        return f"Corner position {corner_position} not recognized."

    face1, row1, col1 = corner_position
    face2, row2, col2 = corner_adjacents[corner_position][0]
    face3, row3, col3 = corner_adjacents[corner_position][1]

    color1 = cube_array[face1][row1][col1]
    color2 = cube_array[face2][row2][col2]
    color3 = cube_array[face3][row3][col3]

    for pos, adjs in corner_adjacents.items():
        f1, r1, c1 = pos
        f2, r2, c2 = adjs[0]
        f3, r3, c3 = adjs[1]
        
        center1 = cube_array[f1][1][1]
        center2 = cube_array[f2][1][1]
        center3 = cube_array[f3][1][1]

        if set([color1, color2, color3]) == set([center1, center2, center3]):
            # Find which position has the matching center color
            if center1 == color1:
                return pos
            elif center2 == color1:
                return adjs[0]
            elif center3 == color1:
                return adjs[1]
    
    return "Home position not found."