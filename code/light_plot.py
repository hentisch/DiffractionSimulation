import math
from time import time
import mayavi
from mayavi import mlab
from utils import rgb_to_mayavi
from geometry_utils import get_3d_cos_wave_between_points

import numpy as np

from PIL import Image


def plot_cylinder_line(
    point_a: tuple,
    point_b: tuple,
    scale_factor: float,
    resolution: float,
    figure: mlab.figure,
):
    total_length = math.dist(point_a, point_b)
    num_subsections = math.ceil(total_length)
    # subsection_length = total_length/num_subsections

    all_points = np.linspace(point_a, point_b, num_subsections + 1)
    # start_points = all_points[:-1]
    # end_points = all_points[1:] + 0.01

    for i, point in enumerate(all_points[:-1]):
        mlab.quiver3d(
            *point,
            *all_points[i + 1],
            mode="arrow",
            resolution=resolution,
            color=rgb_to_mayavi(0, 0, 255),
            figure=figure
        )


def main(image_path=None, size=(300, 300)):
    endpoints = np.array([[0, 0, 0], [0, 4, 0]])
    electric_field = get_3d_cos_wave_between_points(endpoints, 10000, 1, 1, 0)
    magnetic_field = get_3d_cos_wave_between_points(endpoints, 10000, 1, 1, 0.5 * np.pi)

    fig = mlab.figure(bgcolor=(1, 1, 1), fgcolor=(0.0, 0.0, 0.0), size=size)

    plot_cylinder_line(*endpoints, 1, 100, fig)

    mlab.orientation_axes(figure=fig)

    ranges = (0, 1, 0, endpoints[1][1], 0, 1)
    ranges = (0, 1, 0, 1, -1, 1)

    mlab.plot3d(
        magnetic_field[:, 0],
        magnetic_field[:, 1],
        magnetic_field[:, 2],
        color=rgb_to_mayavi(255, 0, 0),
        figure=fig,
    )

    """ ax = mlab.axes(
        nb_labels=1,
        xlabel="Strength of magnetic field",
        x_axis_visibility=False,
        y_axis_visibility=False,
        figure=fig,
    )
    ax.axes.font_factor = 1 """

    mlab.plot3d(
        electric_field[:, 0],
        electric_field[:, 1],
        electric_field[:, 2],
        color=rgb_to_mayavi(255, 255, 0),
        figure=fig,
    )

    """ ranges = (endpoints[0][0], endpoints[1][0], endpoints[0][1], endpoints[1][1], -1, 1)
    ax = mlab.axes(
        nb_labels=1,
        ranges=ranges,
        zlabel="Strength of Electric Field",
        ylabel="Distance",
        figure=fig,
    )
    ax.axes.font_factor = 1 """

    if image_path == None:
        mlab.show()
    else:
        mlab.savefig(image_path, figure=fig, size=(size[0]/10, size[1]/10))

if __name__ == "__main__":
    main()