from rocket_data import *
import math
import matplotlib.pyplot as plt
from constants import *


def approx_rocket_ode(dt, t, x0, y0, vx0, vy0, drag_coef, m):
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
    vx1 = vx0 - drag_coef * v_size * vx0 * dt/m
    vy1 = vy0 - (drag_coef * v_size * vy0/m + G) * dt
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
        data = approx_rocket_ode(dt, data[0], data[1], data[2], data[3], data[4], rocket_data.drag, ROCKET_MASS)
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
    div = f(dt, theta1, x_dest, rocket_data) - f(dt, theta0, x_dest, rocket_data)
    return theta1 \
                 - f(dt, theta1, x_dest, rocket_data) * (theta1 - theta0) / div


def find_theta(dt, rocket_data, desired_hit_loc):
    theta0 = math.radians(10)  # need to check for good starting theta's
    theta1 = math.radians(30)
    while math.fabs(theta1 - theta0) > 0.001:
        tmp = theta1
        theta1 = find_next_theta(dt, theta0, theta1, desired_hit_loc, rocket_data)
        theta0 = tmp
    return theta1


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


def find_minimal_distance_t(dt, rocket_data_first, rocket_data_second, theta_second):
    temp = rocket_data_second.theta
    rocket_data_second.theta = theta_second
    ret = find_minimal_distance(dt, rocket_data_first, rocket_data_second)
    rocket_data_second.theta = temp
    return ret


def find_next_theta_intercept(dt, theta0, theta1, rocket_data_enemy: RocketData,
                                                    rocket_data_us: RocketData):
    rocket_data_us.theta = theta1
    div = \
        find_minimal_distance_t(dt, rocket_data_enemy, rocket_data_us, theta1) \
        - find_minimal_distance_t(dt, rocket_data_enemy, rocket_data_us, theta0)
    return theta1 \
                 - \
           find_minimal_distance_t(dt, rocket_data_enemy, rocket_data_us, theta1) * (theta1 - theta0) / div


def find_theta_intercept(dt, rocket_data_enemy, rocket_data_us):
    theta0 = math.pi  # need to check for good starting theta's
    theta1 = 3
    count = 0
    while count < 3:
        if abs(theta1 - theta0) <= 0.001:
            count += 1
        else:
            count = 0
        tmp = theta1
        theta1 = find_next_theta_intercept(dt, theta0, theta1, rocket_data_enemy, rocket_data_us)
        theta0 = tmp
    return theta1


if __name__ == "__main__":

    data1 = RocketData(0, 0, ROCKET_VEL, math.radians(50), DRAG_TOTAL_COEF)
    data2 = RocketData(get_hit_loc(0.001, data1)*0.75, 0, ROCKET_VEL, 2.2691859291924388, DRAG_TOTAL_COEF)

    # x = np.linspace(math.pi/2, math.pi, 50)
    # y = [find_minimal_distance_t(0.001, data1, data2, t) for t in x]
    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # fig.show()

    print(find_minimal_distance(0.001, data1, data2))
    print(find_theta_intercept(0.001, data1, data2))

