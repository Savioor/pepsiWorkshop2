import math

ROCKET_SURFACE_AREA = ((0.5*0.115) ** 2) * math.pi
AIR_DENSITY = 1.225  # https://en.wikipedia.org/wiki/Density_of_air
DRAG_MYSTERY_COEF = 0.5
ROCKET_MASS = 40
ROCKET_VEL = 150
G = 9.81

DRAG_TOTAL_COEF = ROCKET_SURFACE_AREA * AIR_DENSITY * DRAG_MYSTERY_COEF  # I think

