# Defining Paths
# the letter E stands for the edge peice while letter C stands for corner peice
# the 'AE' node is the endpoint for all nodes
corner_cube_path = {
    'AC': [], #Yellow Face
    'BC': ['FC', 'SC'], #Yellow Face
    'CC': ['MC', 'XC'], #Yellow Face
    'DC': ['OC', 'UC', 'QC', 'HC'], #Yellow Face
    'EC': ['FC', 'GC'],#Red Face
    'FC': ['EC', 'HC', 'JC', 'BC'], #Red Face
    'GC': ['HC', 'EC', 'WC', 'OC'], #Red Face
    'HC': ['FC', 'GC', 'LC', 'DC', 'XC', 'PC'], #Red Face
    'IC': ['OC', 'VC', 'KC', 'JC'], #White Face
    'JC': ['MC', 'XC', 'SC', 'FC', 'IC', 'LC'], #White Face
    'KC': ['LC', 'IC'], #White Face
    'LC': ['QC', 'HC', 'JC', 'KC'], #White Face
    'MC': ['CC', 'JC', 'OC', 'NC'], #Green Face
    'NC': ['MC', 'PC'], #Green Face
    'OC': ['DC', 'IC', 'PC', 'MC', 'GC', 'SC'], #Green Face
    'PC': ['NC', 'OC', 'HC', 'TC'], #Green Face
    'QC': ['DC', 'LC'], #Orange Face
    'RC': [], #Orange Face
    'SC': ['BC', 'JC', 'OC', 'WC'], #Orange Face
    'TC': ['PC', 'XC'], #Orange Face
    'UC': [], #Blue/Purple Face
    'VC': ['DC', 'IC'], #Blue/Purple Face
    'WC': ['SC', 'GC'], #Blue/Purple Face
    'XC': ['JC', 'CC', 'TC', 'HC'], #Blue/Purple Face
}

# Since the 3D array is stored as Nums we need to convert them so we know where to pathfind to where
coordinate_to_label_corners = {
    (0, 0, 0): 'AC',
    (0, 0, 2): 'BC',
    (0, 2, 0): 'CC',
    (0, 2, 2): 'DC',
    
    (3, 0, 0): 'EC',
    (3, 0, 2): 'FC',
    (3, 2, 0): 'GC',
    (3, 2, 2): 'HC',
    
    (2, 0, 0): 'IC',
    (2, 0, 2): 'JC',
    (2, 2, 0): 'KC',
    (2, 2, 2): 'LC',
    
    (4, 0, 0): 'MC',
    (4, 0, 2): 'NC',
    (4, 2, 0): 'OC',
    (4, 2, 2): 'PC',
    
    (5, 0, 0): 'QC',
    (5, 0, 2): 'RC',
    (5, 2, 0): 'SC',
    (5, 2, 2): 'TC',
    
    (1, 0, 0): 'UC',
    (1, 0, 2): 'VC',
    (1, 2, 0): 'WC',
    (1, 2, 2): 'XC',
}

label_to_coordinate_corners = {
    'AC': (0, 0, 0),
    'BC': (0, 0, 2),
    'CC': (0, 2, 0),
    'DC': (0, 2, 2),
    
    'EC': (3, 0, 0),
    'FC': (3, 0, 2),
    'GC': (3, 2, 0),
    'HC': (3, 2, 2),
    
    'IC': (2, 0, 0),
    'JC': (2, 0, 2),
    'KC': (2, 2, 0),
    'LC': (2, 2, 2),
    
    'MC': (4, 0, 0),
    'NC': (4, 0, 2),
    'OC': (4, 2, 0),
    'PC': (4, 2, 2),
    
    'QC': (5, 0, 0),
    'RC': (5, 0, 2),
    'SC': (5, 2, 0),
    'TC': (5, 2, 2),
    
    'UC': (1, 0, 0),
    'VC': (1, 0, 2),
    'WC': (1, 2, 0),
    'XC': (1, 2, 2),
}