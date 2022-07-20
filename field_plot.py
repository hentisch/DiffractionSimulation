import numpy as np

import thompson_scattering as ts

from mayavi import mlab
from traits.api import HasTraits, Range, Instance,on_trait_change
from traitsui.api import View, Item, Group
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel

def get_electric_scalar_field(size:tuple, time:float):
    atom_point = (size[0]/2, size[1]/2, size[2]/2)

    cloud = np.zeros(size)    

    for x in range(size[0]):
        for y in range(size[1]):
            for z in range(size[2]):
                cloud[x, y, z] = ts.magnitude_by_space(atom_point, (x, y, z), time, 1, 1)
    
    return cloud


def plot_electric_field(size:tuple, scalar_field:mlab.pipeline.scalar_field):
    atom_point = (size[0]/2, size[1]/2, size[2]/2)
    mlab.points3d(*atom_point)

    mlab.pipeline.volume(scalar_field)

    mlab.axes()

""" if __name__ == "__main__":
    field = mlab.pipeline.scalar_field(get_electric_scalar_field((20, 20, 20), 0))
    plot_electric_field((20, 20, 20), field)
    mlab.show() """

class FieldModel(HasTraits):
    slider = Range(0, 100, 0.2)
    scene = Instance(MlabSceneModel, ())

    def __init__(self) -> None:
        super().__init__()
        self.scene.mayavi_scene #For some reason if we don't access this attribute before using it as a figure it wont work
        self.s = mlab.pipeline.volume(mlab.pipeline.scalar_field(get_electric_scalar_field((20, 20, 20), 0)), figure=self.scene.mayavi_scene)
    
    @on_trait_change('slider')
    def slider_changed(self):
        self.s.mlab_source.scalars = get_electric_scalar_field((20, 20, 20), self.slider/10)
    
    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene)), Group('slider'))

if __name__ == "__main__":
    model = FieldModel()
    model.configure_traits()