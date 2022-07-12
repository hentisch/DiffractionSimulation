import numpy as np

from raw_unit_cells import simple_cubic
from unit_cell import UnitCell

class CrystalLattice:
    
    def __init__(self, shape:tuple[int, int, int], unit_cell:UnitCell) -> None:
        self.points = np.zeros((np.prod(shape), unit_cell.num_points, 3))

        current_lattice_index = 0

        for x in range(1, shape[0]+1):
            for y in range(1, shape[1]+1):
                for z in range(1, shape[2]+1):
                    adjusted_unit_cell = unit_cell.get_point_copy()
                    adjusted_unit_cell[:,0] += x*unit_cell.x_size
                    adjusted_unit_cell[:,1] += y*unit_cell.y_size
                    adjusted_unit_cell[:,2] += z*unit_cell.z_size
                    self.points[current_lattice_index] = adjusted_unit_cell
                    current_lattice_index += 1
        
    def get_raw_points(self):
        return self.points.reshape((self.points.shape[1]*self.points.shape[0], 3))