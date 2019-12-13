import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

test = ctrl.Antecedent(np.arange(0,11,1),'quality')