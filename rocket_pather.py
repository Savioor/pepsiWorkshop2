from rocket_data import *
import math


def approx_rocket_ode(dt, t, x0, y0, vx0, vy0, drag_coef, m, g):
    """

    :param dt: time of sim step
    :param t: the start time
    :param x0: start x
    :param y0: start y
    :param v0: start v (size of velocity vector)
    :param theta0: start angle (argument of velocity vector)
    :param drag_coef: the drag
    :return a list (t1, x1, y1, vx1, vy1) describing the state of the rocket after dt time
    """
    v_size = math.sqrt(math.pow(vx0, 2) + math.pow(vy0, 2))
    t1 = t + dt
    x1 = x0 + vx0 * dt
    y1 = y0 + vy0 * dt
    vx1 = vx0 - drag_coef * v_size * vx0 * dt
    vy1 = vy0 - (drag_coef * v_size * vy0 + m * g) * dt
    return t1, x1, y1, vx1, vy1


def rocket_in_vaccum(dt, x0, y0, v0, theta0):
    """

    :param dt: time of sim step
    :param x0: start x
    :param y0: start y
    :param v0: start v (size of velocity vector)
    :param theta0: start angle (argument of velocity vector)
    :return: generator returing the next point each time
    """
    return rocket_in_air(dt, RocketData(x0, y0, v0, theta0, 0))


def rocket_in_air(dt, rocket_data: RocketData):
    """

    :param dt: time of sim step
    :param x0: start x
    :param y0: start y
    :param v0: start v (size of velocity vector)
    :param theta0: start angle (argument of velocity vector)
    :param drag_coef: the drag (C * rho * A)
    :return: generator returing the next point each time
    """
    vel_vect = rocket_data.get_vel_vector()
    t = 0
    data = (t, rocket_data.x, rocket_data.y, vel_vect[0], vel_vect[1])

    yield data[1], data[2]
    while True:
        data = approx_rocket_ode(dt, data[0], data[1], data[2], data[3], data[4], rocket_data.drag)
        yield data[1], data[2]


def get_hit_loc(dt, rocket_data: RocketData):
    rocket_path = rocket_in_air(dt, rocket_data)
    while True:
        point = next(rocket_path)
        if point[1] < 0:
            return point[0]


def f(dt, theta, x_dest, rocket_data: RocketData):
    rocket_data.theta = theta
    return x_dest - get_hit_loc(dt, rocket_data)  # = 0 in dream


def find_next_theta(dt, theta0, theta1, x_dest, rocket_data: RocketData):
    next_theta = theta1 - f(dt, theta1, x_dest, rocket_data) * (theta1 - theta0) / (
            f(dt, theta1, x_dest, rocket_data) - f(dt, theta0, x_dest, rocket_data))
    return next_theta


def find_theta(dt, rocket_data, desired_hit_loc):
    theta0 = math.radians(45)  # need to check for good starting theta's
    theta1 = math.radians(50)
    while math.fabs(theta1 - theta0) > 0.001:
        tmp = theta1
        theta1 = find_next_theta(dt, theta0, theta1, desired_hit_loc, rocket_data)
        theta0 = tmp
    return theta1


r = RocketData(0, 0, 10, 0, 0)
print(find_theta(0.0001, r, 30))


def find_minimal_distance(dt, rocket_data_first, rocket_data_second):
    first_path = rocket_in_air(dt, rocket_data_first)
    second_path = rocket_in_air(dt, rocket_data_second)
    first = next(first_path)
    second = next(second_path)
    lowest_dist = (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2
    while True:
        first = next(first_path)
        second = next(second_path)
        if first[1] < 0 or second[1] < 0:
            return lowest_dist
        dist = (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2
        if dist < lowest_dist:
            lowest_dist = dist
