# -*- coding: utf-8 -*-

import numpy as np

a1 = np.array([[0.1, 0.4, 0.4],
                [0.0, 1.0, -1.0]], dtype = np.float64)

print("Vasen yläkulma on", a1[0, 0])
print("Oikea alakulma on", a1[1, 2])
print("Ensimmäinen sarake", a1[:, 0])
print("Toinen rivi", a1[1, :])