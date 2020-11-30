import numpy as np

class RocketData:

    def __init__(self, x, y, v, theta, drag):
        self.x = x
        self.y = y
        self.v = v
        self.theta = theta
        self.drag = drag

    def get_vel_vector(self):
        return self.v * np.array([np.cos(self.theta), np.sin(self.theta)])

