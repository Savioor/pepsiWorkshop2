from rocket_data import RocketData
from constants import *
import matplotlib.pyplot as plt
from rocket_pather import *


def dist(p1, p2):
    return math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2)


def visualization():
    data1 = RocketData(0, 0, ROCKET_VEL, math.radians(50), DRAG_TOTAL_COEF)
    data2 = RocketData(get_hit_loc(0.001, data1) * 0.75, 0, ROCKET_VEL, 2.3646455947658542, DRAG_TOTAL_COEF * 0.7)

    path1 = rocket_in_air(0.001, data1)
    path2 = rocket_in_air(0.001, data2)

    x_first = []
    y_first = []
    x_second = []
    y_second = []

    while True:
        first = next(path1)
        x_first.append(first[0])
        y_first.append(first[1])
        second = next(path2)
        x_second.append(second[0])
        y_second.append(second[1])
        if dist(first, second) < 2:
            break

    fig, ax = plt.subplots()
    ax.plot(x_first, y_first)
    ax.plot(x_second, y_second)

    ax.legend(["Enemy Rocket", "Our Rocket"])
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    fig.show()


if __name__ == "__main__":
    visualization()



