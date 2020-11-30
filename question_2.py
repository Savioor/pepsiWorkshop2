from rocket_pather import *
from constants import *
import math
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = RocketData(0, 0, 150, math.radians(50), 0)
    path = rocket_in_air(0.001, data)

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
    ax.legend(["Rocket Path"])
    fig.show()
