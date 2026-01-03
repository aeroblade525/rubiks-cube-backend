from Cube_Turning.Cube_Turning_CCW import CubeArrayDCCW, CubeArrayDCCW, CubeArrayFCCW, CubeArrayLCCW, CubeArrayRCCW, CubeArrayUCCW
from Cube_Turning.Cube_Turning_CW import CubeArrayDCW, CubeArrayDCW, CubeArrayFCW, CubeArrayLCW, CubeArrayRCW, CubeArrayUCW

corner_map = {
    ('BC', 'FC'): CubeArrayRCCW,
    ('BC', 'SC'): CubeArrayRCW,
    
    ('CC', 'MC'): CubeArrayFCW,
    ('CC', 'XC'): CubeArrayFCCW,
    
    ('DC', 'OC'): CubeArrayFCW,
    ('DC', 'UC'): CubeArrayFCCW,
    ('DC', 'QC'): CubeArrayRCW,
    ('DC', 'HC'): CubeArrayRCCW,
    
    ('EC', 'FC'): CubeArrayFCW,
    ('EC', 'GC'): CubeArrayFCCW,
    
    ('FC', 'EC'): CubeArrayFCCW,
    ('FC', 'HC'): CubeArrayFCW,
    ('FC', 'JC'): CubeArrayRCCW,
    ('FC', 'BC'): CubeArrayRCW,
    
    ('GC', 'HC'): CubeArrayFCCW,
    ('GC', 'EC'): CubeArrayFCW,
    ('GC', 'WC'): CubeArrayDCCW,
    ('GC', 'OC'): CubeArrayDCW,
    
    ('HC', 'FC'): CubeArrayFCCW,
    ('HC', 'GC'): CubeArrayFCW,
    ('HC', 'LC'): CubeArrayRCCW,
    ('HC', 'DC'): CubeArrayRCW,
    ('HC', 'XC'): CubeArrayDCCW,
    ('HC', 'PC'): CubeArrayDCW,
    
    ('IC', 'OC'): CubeArrayFCCW,
    ('IC', 'VC'): CubeArrayFCW,
    ('IC', 'KC'): CubeArrayDCW,
    ('IC', 'JC'): CubeArrayDCCW,
    
    ('JC', 'MC'): CubeArrayFCCW,
    ('JC', 'XC'): CubeArrayFCW,
    ('JC', 'SC'): CubeArrayRCCW,
    ('JC', 'FC'): CubeArrayRCW,
    ('JC', 'IC'): CubeArrayDCCW,
    ('JC', 'LC'): CubeArrayDCW,
    
    ('KC', 'LC'): CubeArrayDCCW,
    ('KC', 'IC'): CubeArrayDCW,
    
    ('LC', 'QC'): CubeArrayRCCW,
    ('LC', 'HC'): CubeArrayRCW,
    ('LC', 'JC'): CubeArrayDCCW,
    ('LC', 'KC'): CubeArrayDCW,
    
    ('MC', 'CC'): CubeArrayFCCW,
    ('MC', 'JC'): CubeArrayFCW,
    ('MC', 'OC'): CubeArrayRCCW,
    ('MC', 'NC'): CubeArrayRCW,
    
    ('NC', 'MC'): CubeArrayRCCW,
    ('NC', 'PC'): CubeArrayRCW,
    
    ('OC', 'DC'): CubeArrayFCCW,
    ('OC', 'IC'): CubeArrayFCW,
    ('OC', 'PC'): CubeArrayRCCW,
    ('OC', 'MC'): CubeArrayRCW,
    ('OC', 'GC'): CubeArrayDCCW,
    ('OC', 'SC'): CubeArrayDCW,
    
    ('PC', 'NC'): CubeArrayRCCW,
    ('PC', 'OC'): CubeArrayRCW,
    ('PC', 'HC'): CubeArrayDCCW,
    ('PC', 'TC'): CubeArrayDCW,
    
    ('QC', 'DC'): CubeArrayRCCW,
    ('QC', 'LC'): CubeArrayRCW,
    
    ('SC', 'BC'): CubeArrayRCCW,
    ('SC', 'JC'): CubeArrayRCW,
    ('SC', 'OC'): CubeArrayDCCW,
    ('SC', 'WC'): CubeArrayDCW,
    
    ('TC', 'PC'): CubeArrayDCCW,
    ('TC', 'XC'): CubeArrayDCW,
    
    ('VC', 'DC'): CubeArrayFCW,
    ('VC', 'IC'): CubeArrayFCCW,
    
    ('WC', 'SC'): CubeArrayDCCW,
    ('WC', 'GC'): CubeArrayDCW,
    
    ('XC', 'JC'): CubeArrayFCCW,
    ('XC', 'CC'): CubeArrayFCW,
    ('XC', 'TC'): CubeArrayDCCW,
    ('XC', 'HC'): CubeArrayDCW,
}