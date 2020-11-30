from rocket_pather import *
from constants import *
import math
import matplotlib.pyplot as plt

if __name__ == "__main__":

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

    data = RocketData(0, 0, ROCKET_VEL, math.radians(50), -.1 * DRAG_TOTAL_COEF)
    path = rocket_in_air(0.0001, data)

    x_list = []
    y_list = []
    while True:
        curr = next(path)
        if curr[1] < 0:
            break
        x_list.append(curr[0])
        y_list.append(curr[1])

    ax.plot(x_list, y_list)

    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.legend(["drag = infinite", "drag = negative"])
    fig.show()
