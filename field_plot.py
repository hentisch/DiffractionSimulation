from math import dist
import numpy as np

import thomson_scattering as ts

from mayavi import mlab
from traits.api import HasTraits, Range, Instance, on_trait_change, Enum
from traitsui.api import View, Item, Group
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel

import array_utils as au

class FieldModel(HasTraits):
    time = Range(0, 100, 0.2)
    scale = Range(0, 100, 0.2)
    scene = Instance(MlabSceneModel, ())

    mode_select = Enum('amplitude', 'phase')

    def __init__(self, plot_size:tuple, wavevector_origin:tuple, wave_amplitude:float, time:float=0) -> None:

        self.current_mode = "amplitude"

        self.plot_size = plot_size
        self.wavevector_origin = np.array(wavevector_origin)
        self.time = 0
        self.wave_amplitude = 5

        self.unit_size = 5

        super().__init__()
        self.scene.mayavi_scene #For some reason if we don't access this attribute before using it as a figure it wont work
        self.s = mlab.pipeline.volume(mlab.pipeline.scalar_field(self.get_electric_scalar_field(), figure=self.scene.mayavi_scene))
    
    def get_electric_scalar_field(self):
        atom_point = tuple((length/2)*self.unit_size for length in self.plot_size) #The middle of the plot

        cloud = np.zeros(self.plot_size)

        for x in range(self.plot_size[0]):
            for y in range(self.plot_size[1]):
                for z in range(self.plot_size[2]):
                    if not np.array_equal(au.multiply_by_scalar((x, y, z), self.unit_size), atom_point):
                        scaled_point = au.multiply_by_scalar((x, y, z), self.unit_size)
                        assert dist(scaled_point, atom_point) != 0
                        cloud[x, y, z] = ts.scattering_by_space(atom_point, au.multiply_by_scalar((x, y, z), self.unit_size), self.wavevector_origin*self.unit_size, self.time, self.wave_amplitude, returned_value=self.mode_select)
        
        return cloud
        
    def update_plot(self):
        self.s.mlab_source.scalars = self.get_electric_scalar_field()
    
    @on_trait_change('time')
    def slider_changed(self):
        self.time = self.time
        self.update_plot()

    @on_trait_change('scale')
    def scale_change(self):
        self.unit_size = self.scale
        self.update_plot()
    
    @on_trait_change('mode_select')
    def mode_selected(self):
        if self.mode_select != self.current_mode:
            self.current_mode = self.mode_select
            self.update_plot()

    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene)), Group('time', 'scale', 'mode_select'), resizable=True)

if __name__ == "__main__":
    model = FieldModel((20, 20, 20), (10, 0, 10), 1)
    model.configure_traits()