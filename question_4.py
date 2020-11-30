from rocket_pather import *
from constants import *
import math
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = RocketData(0, 0, ROCKET_VEL, 0, 0)
    theta_50_rocket = RocketData(0, 0, ROCKET_VEL, math.radians(50), 0)
    theta_70_rocket = RocketData(0, 0, ROCKET_VEL, math.radians(70), 0)
    x_for_50 = get_hit_loc(0.001, theta_50_rocket)
    x_for_70 = get_hit_loc(0.001, theta_70_rocket)
    x_dest = [i for i in range(int(x_for_70), int(x_for_50), 100)]
    dt = 0.001
    thetas = [find_theta(dt, data, i) for i in x_dest]
    fig, ax = plt.subplots()
    ax.plot(x_dest, thetas)
    ax.set_xlabel("dest (m)")
    ax.set_ylabel("theta (rad)")
    ax.legend(["theta for desired dest"])
    fig.show()
