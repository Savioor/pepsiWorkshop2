import rocket_pather as rp
from rocket_data import RocketData


def f(dt, theta, x_dest, rocket_data: RocketData):
    rocket_data.theta = theta
    return x_dest - rp.get_hit_loc(dt, rocket_data)  # = 0 in dream


def find_next_theta(dt, theta0, theta1, x_dest, rocket_data: RocketData):
    next_theta = theta1 - f(dt, theta1, x_dest, rocket_data) * (theta1 - theta0) / (
                f(dt, theta1, x_dest, rocket_data) - f(dt, theta0, x_dest, rocket_data))
    return next_theta
