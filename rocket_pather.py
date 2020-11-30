from rocket_data import *


def approx_rocket_ode(dt, t, x0, y0, v0, theta0, drag_coef):
    """

    :param dt: time of sim step
    :param t: the start time
    :param x0: start x
    :param y0: start y
    :param v0: start v (size of velocity vector)
    :param theta0: start angle (argument of velocity vector)
    :param drag_coef: the drag
    :return a list (t1, x1, y1, v1, theta1) describing the state of the rocket after dt time
    """
    return 0, 0, 0, 0, 0


def rocket_in_vaccum(dt, x0, y0, v0, theta0):
    """

    :param dt: time of sim step
    :param x0: start x
    :param y0: start y
    :param v0: start v (size of velocity vector)
    :param theta0: start angle (argument of velocity vector)
    :return: generator returing the next point each time
    """
    return rocket_in_air(dt, RocketData(x0, y0 , b0, theta0, 0))


def rocket_in_air(dt, rocket_data):
    """

    :param dt: time of sim step
    :param x0: start x
    :param y0: start y
    :param v0: start v (size of velocity vector)
    :param theta0: start angle (argument of velocity vector)
    :param drag_coef: the drag (C * rho * A)
    :return: generator returing the next point each time
    """
    pass


def find_minimal_distance(rocket_data_first, rocket_data_second):
    pass

