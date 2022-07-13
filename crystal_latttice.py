import numpy as np

from raw_unit_cells import simple_cubic
from unit_cell import UnitCell

class CrystalLattice:
    
    def __init__(self, shape:tuple[int, int, int], unit_cell:UnitCell) -> None:
        self.all_points = np.zeros((np.prod(shape), unit_cell.num_points, 3))
        self.edge_points = np.zeros((np.prod(shape), unit_cell.num_edge_points, 3))

        current_lattice_index = 0

        for x in range(1, shape[0]+1):
            for y in range(1, shape[1]+1):
                for z in range(1, shape[2]+1):
                    adjusted_unit_cell = unit_cell.get_shifted_points(x, y, z)
                    adjusted_edge_points = unit_cell.get_shifted_points(x, y, z, points="edge")
                    self.all_points[current_lattice_index] = adjusted_unit_cell
                    self.edge_points[current_lattice_index] = adjusted_edge_points
                    current_lattice_index += 1
        
    def get_raw_points(self):
        return self.all_points.reshape((self.all_points.shape[1]*self.all_points.shape[0], 3))