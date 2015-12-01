import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import numpy as np


def _get_minimum_values(position_data):

    """
    Utility function that return the minimum x, y, z from position data
    :param position_data: list containing dict objects with x, y and z properties
    :return: array of size 3 with minimum values for x, y, z on positions 0, 1 and 2
    """
    x_values = []
    y_values = []
    z_values = []

    for position in position_data:
        x_values.append(position['x'])
        y_values.append(position['y'])
        z_values.append(position['z'])

    min_x = np.array(x_values).min()
    min_y = np.array(y_values).min()
    min_z = np.array(z_values).min()

    return [min_x, min_y, min_z]


def _get_maximum_values(position_data):
    """
    Utility function that return the Maximum x, y, z from position data
    :param position_data: list containing dict objects with x, y and z properties
    :return: array of size 3 with maximum values for x, y, z on positions 0, 1 and 2
    """
    x_values = []
    y_values = []
    z_values = []

    for position in position_data:
        x_values.append(position['x'])
        y_values.append(position['y'])
        z_values.append(position['z'])

    max_x = np.array(x_values).max()
    max_y = np.array(y_values).max()
    max_z = np.array(z_values).max()

    return [max_x, max_y, max_z]


class AnimatedScatter(object):

    def __init__(self, _position_data):
        self.fig_3d = plt.figure("Animation")
        self.ax_3d = plt.axes(projection='3d')
        self.sp_3d, = self.ax_3d.plot([], [], [], 'ro')
        self.position_data = _position_data

    def init(self):

        min_values = _get_minimum_values(self.position_data)
        max_values = _get_maximum_values(self.position_data)

        self.ax_3d.set_xlim(min_values[0], max_values[0])
        self.ax_3d.set_ylim(min_values[1], max_values[1])
        self.ax_3d.set_zlim(min_values[2], max_values[2])

        def update3d(i):
            frame_values = self.position_data[i]
            self.sp_3d.set_data(frame_values['x'], frame_values['y'])
            self.sp_3d.set_3d_properties(frame_values['z'])
            return self.sp_3d,

        # This needs to be assigned to a variable otherwise will not move passed the first frame
        # http://stackoverflow.com/questions/15318690/matplotlib-stops-animating-after-first-frame
        ani = animation.FuncAnimation(self.fig_3d, update3d, frames=len(self.position_data),
                                      interval=50, repeat=False)
        plt.show()


class AnimatedScatter2D(object):

    def __init__(self, _position_data):
        self.fig_2d = plt.figure("Animation")
        self.ax_2d = self.fig_2d.add_subplot(111, title='Animation')
        self.sp_2d, = self.ax_2d.plot([], [], 'ro')
        self.position_data = _position_data

    def init(self):

        min_values = _get_minimum_values(self.position_data)
        max_values = _get_maximum_values(self.position_data)

        self.ax_2d.set_xlim(min_values[0], max_values[0])
        self.ax_2d.set_ylim(min_values[1], max_values[1])

        def update2d(i):
            frame_values = self.position_data[i]
            self.sp_2d.set_data(frame_values['x'], frame_values['y'])
            return self.sp_2d,

        # This needs to be assigned to a variable otherwise will not move passed the first frame
        # http://stackoverflow.com/questions/15318690/matplotlib-stops-animating-after-first-frame
        ani = animation.FuncAnimation(self.fig_2d, update2d, frames=len(self.position_data),
                                      interval=50, repeat=False)
        plt.show()