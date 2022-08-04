import matplotlib.pyplot as plt
import numpy as np
from array_utils import fill_skipping

from geometry_utils import index_by_dimension
from thomson_scattering import scattering_by_space

from tqdm import tqdm

def get_thomson_scattering_slice(side_length:float, num_samples:int, axis:str, slice_ind:int, point_of_electrion:tuple, point_of_atom:tuple, value="amplitude"):
    coordinates = np.linspace(0, side_length, round(np.sqrt(num_samples)))
    x_grid, y_grid = np.meshgrid(coordinates, coordinates)

    slice_dim_ind = index_by_dimension[axis]

    scattering_grid = np.zeros(x_grid.shape)

    for x_i, row in enumerate(tqdm(scattering_grid)):
        for y_i, column in enumerate(row):
            x = x_grid[x_i][y_i]
            y = y_grid[x_i][x_i]

            current_pos = [0, 0, 0]
            current_pos = fill_skipping(current_pos, (x, y), (slice_dim_ind,))
            current_pos[slice_dim_ind] = slice_ind

            scattering_grid[x_i][y_i] = scattering_by_space(point_of_electrion, current_pos, point_of_atom, 1, 1, 'z', value)

    plt.imshow(scattering_grid)
    plt.show()

if __name__ == "__main__":
    get_thomson_scattering_slice(100, 100000, 'x', 0, (50, 50, 0), (50, -10, 0))