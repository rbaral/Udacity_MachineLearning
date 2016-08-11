__author__ = 'rbaral'

import numpy as np
import math

a = np.array(['NaN',2,3,5])
print filter(lambda val: not val=='NaN', a)
