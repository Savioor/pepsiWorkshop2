from rocket_pather import *
from constants import *
import math
import matplotlib.pyplot as plt


def sanity_check():

    data = RocketData(0, 0, ROCKET_VEL, math.radians(50), 10000*DRAG_TOTAL_COEF)
    path = rocket_in_air(0.0001, data)

    x_list = []
    y_list = []
    while True:
        curr = next(path)
        if curr[1] < 0:
            break
        x_list.append(curr[0])
        y_list.append(curr[1])

    fig, ax = plt.subplots()
    ax.plot(x_list, y_list)

    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.legend(["drag = infinite"])

    fig.show()

    fig, ax = plt.subplots()

    data = RocketData(0, 0, ROCKET_VEL, math.radians(50), -.1 * DRAG_TOTAL_COEF)
    path = rocket_in_air(0.0001, data)

    x_list = []
    y_list = []
    for i in range(100000):
        curr = next(path)
        if curr[1] < 0:
            break
        x_list.append(curr[0])
        y_list.append(curr[1])

    ax.plot(x_list, y_list)

    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.legend(["drag = negative"])
    fig.show()


def visualization():
    data = RocketData(0, 0, ROCKET_VEL, math.radians(50), DRAG_TOTAL_COEF)
    path = rocket_in_air(0.0001, data)
    x_list = []
    y_list = []
    while True:
        curr = next(path)
        if curr[1] < 0:
            break
        x_list.append(curr[0])
        y_list.append(curr[1])

    fig, ax = plt.subplots()
    ax.plot(x_list, y_list)

    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.legend(["rocket path with drag"])
    fig.show()


def hit_lock_by_dt():
    data = RocketData(0, 0, ROCKET_VEL, math.radians(50), DRAG_TOTAL_COEF)

    dt_range = 10 ** (np.linspace(-3.5, -1, 200))
    hit_locs = [get_hit_loc(dt, data) for dt in dt_range]

    fig, ax = plt.subplots()
    ax.plot(dt_range, hit_locs)

    ax.set_xscale("log")

    ax.set_xlabel("dt (seconds)")
    ax.set_ylabel("hit loc (m)")
    fig.show()


if __name__ == "__main__":
    sanity_check()
    visualization()
    hit_lock_by_dt()


