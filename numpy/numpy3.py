# -*- coding: utf-8 -*-

import numpy as np

filename = "np_example_3.npy"

a1 = np.array([1, 2, 3])

np.save(filename, a1)

del a1

a2 = np.load(filename)

print(a2)