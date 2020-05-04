import numpy as np
import h5py

hf = h5py.File('Autopilot.h5', 'r')

print(hf.keys())
hf.close()

print("clsed")