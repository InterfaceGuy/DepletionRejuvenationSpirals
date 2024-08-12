import importlib
import pydeation.imports
importlib.reload(pydeation.imports)
from pydeation.imports import *



class DepletionRejuvenationSpirals(CustomObject):
    
    def specify_parts(self):
        self.depletion_spiral = Helix(
            p=-27*PI/180,
            color=BLUE,
            start_radius=0,
            start_angle=6*PI, 
            end_radius=100, 
            end_angle=-6*PI, 
            radial_bias=0.5, 
            height=200, 
            height_bias=0.5, 
            plane="xz",
            arrow_end=True,
            creation=True
            )
        self.rejuvenation_spiral = Helix(
            p=27*PI/180,
            color=RED,
            start_radius=0,
            start_angle=-6*PI, 
            end_radius=100, 
            end_angle=6*PI, 
            radial_bias=0.5, 
            height=200, 
            height_bias=0.5, 
            plane="xz",
            arrow_end=True,
            creation=True
            )

        self.parts += [self.depletion_spiral, self.rejuvenation_spiral]

depletion_rejuvenation_spirals = DepletionRejuvenationSpirals(h=PI/2, b=PI/2)