import rocket_pather as rp
from rocket_data import RocketData


def f(theta, x_dest, rocket_data: RocketData):
    rocket_data.theta = theta
    return x_dest - rp.get_hit_loc(theta, rocket_data)  # = 0 in dream
