# Packages and imports 
import numpy as np

from aircraft import Aircraft 

ac = Aircraft()
seat_pitch = 29  # in inches
seat_pitch_m = seat_pitch * 0.0254  # convert to meters
x_cg_oew = 14.5  # center of gravity location for OEW (in meters)

'''Passengers'''
# Define rows and columns for the cabin layout

rows = 18
columns = 4
# Define the cabin layout

cabin_layout = np.zeros((rows, columns))



