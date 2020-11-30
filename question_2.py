from rocket_pather import *
from constants import *
import math
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = RocketData(0, 0, math.radians(50), ROCKET_VEL, DRAG_TOTAL_COEF)
    path = rocket_in_air(0.01, data)

    x_list = []
    y_list = []
    for i in range(10000):
        curr = next(path)
        x_list.append(curr[0])
        y_list.append(curr[1])

    fig, ax = plt.subplots()
    ax.plot(x_list, y_list)
    fig.show()
