# -*- coding: utf-8 -*-

import numpy as np

filename = "np_example_04.npz"

a1 = np.array([0.1, 0.4, 0.4], dtype=np.float64)
a2 = np.array(["a","b","c","d"])
z = np.array([0, 3, 8])

np.savez(filename, a1 = a1, a2 = a2, z = z)

del a1, a2, z

npz_file = np.load(filename)

a1_load =  npz_file["a1"]
a2_load =  npz_file["a2"]
z_load =  npz_file["z"]

print(npz_file)
print(a1_load)
print(a2_load)
print(z_load)