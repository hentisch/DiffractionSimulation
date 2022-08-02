from mayavi import mlab
from geometry_utils import get_3d_cos_wave_between_points

import numpy as np

sin_points = get_3d_cos_wave_between_points(((0, 0, 0), (10, 0, 0)), 10000, 1, 1)
endpoints = np.array([(0, 0, 0), (10, 0, 0)])

mlab.plot3d(sin_points[:,0], sin_points[:,1], sin_points[:,2])
mlab.points3d(endpoints[:,0], endpoints[:,1], endpoints[:,2])
mlab.axes()

mlab.show()