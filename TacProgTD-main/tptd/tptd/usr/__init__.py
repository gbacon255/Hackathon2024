# DO NOT EDIT -->
from pathlib    import Path
from typing     import Tuple
import math

THIS_FOLDER = Path(__file__).resolve().parent
TWR_POS = []
with open(THIS_FOLDER / 'twr.csv', 'r') as twr_h:
    for ln in twr_h:
        ln_parts = ln.strip().split(',') + [None]
        for idx in range(1, 3): ln_parts[idx] = int(ln_parts[idx])
        TWR_POS += [tuple(ln_parts + [None])]
    #End-for
#End-with
# <-- DO NOT EDIT

def twr_func(coord, tag : str, LoT : list, fire : bool, current_dir : float, target_dir : float) -> Tuple[float, bool, bool]:
    '''
    Add in your turret logic here
    
    Notes:
    - "2D-Vector" == pygame.math.Vector2d using pixels
    - angle == float in degrees
    
    PARAMETERS
    ----------
    coord : 2D-Vector
        Location of the subject tower relative to the home base
    
    tag : str
        An identifier defined by you
    
    LoT : list
        "List of Targets", each entry in this list has the following structure
        - Target Type : str
        - Target Position : 2D-Vector
        - Target Velocity : 2D-Vector
    
    fire : bool
        Indicates whether or not the next round will be fired when chambered
    
    current_dir : angle
        Current bearing of the gun
    
    target_dir : angle
        Target bearing of the gun
    
    RETURNS
    -------
    target_dir
        As defined in `PARAMETERS`
    
    fire
        As defined in `PARAMETERS`
    
    target_dir_is_radians : bool
        Indicates if the output target_dir is in radians
    
    '''
    '''
        print(LoT[1][1])
        x = LoT[1][1][0]
        y = LoT[1][1][1]
        tan = math.tan(x/y)
        target_dir = tan
    '''
    if(int(tag) == 1):
        #tower x and y
        tX = LoT[0][1][0]
        tY = LoT[0][1][1]
        #lead target x and y
        bX = LoT[2][1][0]
        bY = LoT[2][1][1] 
        target_dir = Transform(tX, tY, bX, bY, current_dir)
        return (target_dir, True, True)
    elif(int(tag) == 2):
        #tower x and y
        tX = LoT[1][1][0]
        tY = LoT[1][1][1]
        #lead target x and y
        bX = LoT[2][1][0]
        bY = LoT[2][1][1]
        target_dir = Transform(tX, tY, bX, bY, current_dir)
        return (target_dir, True, True)
    else:
        return (target_dir, False, True)
#End-def

#function to transform target coordinates to our turret coordinate frame
def Transform(tX, tY, bX, bY, current_dir):
    turn = False
    trX = bX - tX 
    trY = bY - tY
    if(trX ==0):
        trX -=100
    if(trX <= 0 and trX <= .1):
        turn = True
    if(trY == 0):
       trY = .0000001
    #calculates turn needed to aim at leading target
    deg = math.atan(trY/trX)
    if turn:
        deg = deg-math.pi
        
    #return the radian turn angle to be used by the turret
    return deg
