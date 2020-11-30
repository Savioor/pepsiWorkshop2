import math

# https://en.wikipedia.org/wiki/Qassam_rocket
# We use qassam 2 rockets

ROCKET_SURFACE_AREA = ((0.5*0.115) ** 2) * math.pi
AIR_DENSITY = 1.225  # https://en.wikipedia.org/wiki/Density_of_air
DRAG_MYSTERY_COEF = 0.45  # http://www.rasaero.com/example-Cal.htm
ROCKET_MASS = 32
ROCKET_VEL = 343
G = 9.81

DRAG_TOTAL_COEF = ROCKET_SURFACE_AREA * AIR_DENSITY * DRAG_MYSTERY_COEF  # I think

