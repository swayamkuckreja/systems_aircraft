# Packages and imports 
import numpy as np

from aircraft import Aircraft 

import matplotlib.pyplot as plt
ac = Aircraft()
seat_pitch = 29  # in inches
seat_pitch_m = seat_pitch * 0.0254  # convert to meters
x_cg_oew = 14.5  # center of gravity location for OEW (in meters)

x_cg_cargo1 = 12.4  # center of gravity location for cargo 1 (in meters)
x_cg_cargo2 = 15.4  # center of gravity location for cargo 2 (in meters)


'''Passengers'''
# Define rows and columns for the cabin layout

rows = 18
columns = 4
# Define the cabin layout

cabin_layout = np.zeros((rows, columns))

columns_1 = [0,3]
columns_2 = [1,2]

# Fill the cabin layout with passengers (1 for occupied, 0 for empty) windows first, from front to back
for i in range(rows):
    for j in columns_1:
        cabin_layout[i, j] = 1  

# Fill the cabin layout with passengers (1 for occupied, 0 for empty) window seats first, from back to front
for i in range(rows-1, -1, -1):
    for j in columns_1:
        cabin_layout[i, j] = 1

print(cabin_layout)







