import numpy as np

import thomson_scattering as ts

from mayavi import mlab
from traits.api import HasTraits, Range, Instance, on_trait_change, Enum
from traitsui.api import View, Item, Group
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel

class FieldModel(HasTraits):
    slider = Range(0, 100, 0.2)
    scene = Instance(MlabSceneModel, ())

    mode_select = Enum('amplitude', 'phase')

    def __init__(self, plot_size:tuple, wavevector_origin:tuple, wave_amplitude:float, time:float=0) -> None:
        super().__init__()

        self.current_mode = "amplitude"

        self.plot_size = plot_size
        self.wavevector_orgin = wavevector_origin
        self.time = 0
        self.wave_amplitude = 5

        self.scene.mayavi_scene #For some reason if we don't access this attribute before using it as a figure it wont work
        self.s = mlab.pipeline.volume(mlab.pipeline.scalar_field(self.get_electric_scalar_field(), figure=self.scene.mayavi_scene))
    
    def get_electric_scalar_field(self):
        atom_point = tuple(length/2 for length in self.plot_size) #The middle of the plot

        cloud = np.zeros(self.plot_size)    

        for x in range(self.plot_size[0]):
            for y in range(self.plot_size[1]):
                for z in range(self.plot_size[2]):
                    cloud[x, y, z] = ts.scattering_by_space(atom_point, (x, y, z), self.wavevector_orgin, self.time, self.wave_amplitude, returned_value=self.mode_select)
        
        return cloud
        
    def update_plot(self):
        self.s.mlab_source.scalars = self.get_electric_scalar_field()
    
    @on_trait_change('slider')
    def slider_changed(self):
        self.time = self.slider
        self.update_plot()
    
    @on_trait_change('mode_select')
    def mode_selected(self):
        if self.mode_select != self.current_mode:
            self.current_mode = self.mode_select
            self.update_plot()

    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene)), Group('slider', 'mode_select'), resizable=True)

if __name__ == "__main__":
    model = FieldModel((20, 20, 20), (10, 0, 10), 1)
    model.configure_traits()