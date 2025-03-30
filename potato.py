import numpy as np
import matplotlib.pyplot as plt
from aircraft import Aircraft 

# Initialize Aircraft object
ac = Aircraft()

# Constants (passengers)
seat_pitch = 29  # in inches
seat_pitch_m = seat_pitch * 0.0254  # convert to meters
x_cg_oew = 14.5  # CG location for OEW (meters)
x_seat = 5.83101  # First passenger seat location (meters)
rows, columns = 18, 4  # Define cabin layout
m_passenger = 75  # Average passenger weight (kg)
m_totpassengers = rows * columns * m_passenger  # Total passenger weight (kg)
print(f"Total passenger weight: {m_totpassengers} kg")

# Constants (cargo)
m_cargo = ac.payload - m_totpassengers  # Total cargo weight (kg)
m_cargo1 = 0.6 * m_cargo  # Cargo 1 weight (kg)
m_cargo2 = 0.4 * m_cargo  # Cargo 2 weight (kg)
print(f"Total cargo weight: {m_cargo} kg")
x_cg_cargo1 = 4.33013  # CG location for cargo 1 (meters)
x_cg_cargo2 = 20.89227 # CG location for cargo 2 (meters)

# Constant(fuel)
m_fuel = ac.mtow - ac.oew - m_cargo - m_totpassengers  # Total fuel weight (kg)
x_fuel = 14.5  # CG location for fuel (meters)
print(f"Total fuel weight: {m_fuel} kg")

# Function to calculate seat CG
def cg_seat(i):
    return x_seat + 0.5 * seat_pitch_m + i * seat_pitch_m  # CG at middle of seat pitch

# Function to calculate new CG
def cg_formula(old_cg, new_cg, new_weight, old_weight):
    return (old_cg * old_weight + new_cg * new_weight) / (old_weight + new_weight)

# Initialize CG and weight
x_cg = x_cg_oew
m = ac.oew

cabin_layout = np.zeros((rows, columns))
columns_1, columns_2 = [0, 3], [1, 2]  # Window and aisle seats

line1x, line1y = [], []
line2x, line2y = [], []
line3x, line3y = [], []
line4x, line4y = [], []
line5x, line5y = [], []
line6x, line6y = [], []
line7x, line7y = [], []

'''Cargo loading'''
# Front to back loaded
for i in range(int(m_cargo1)+1):
    line1x.append(x_cg)
    line1y.append(m)
    x_cg = cg_formula(x_cg, x_cg_cargo1, 1, m)
    m += 1 # Increment mass 1kg

for i in range(int(m_cargo2)+1):
    line1x.append(x_cg)
    line1y.append(m)
    x_cg = cg_formula(x_cg, x_cg_cargo2, 1, m)
    m += 1 # Increment mass 1kg

plt.plot(line1x,line1y)

# Zero to oew again

x_cg = x_cg_oew
m = ac.oew
# Back to front loaded
for i in range(int(m_cargo2)+1):
    line2x.append(x_cg)
    line2y.append(m)
    x_cg = cg_formula(x_cg, x_cg_cargo2, 1, m)
    m += 1 # Increment mass 1kg

for i in range(int(m_cargo1)+1):
    line2x.append(x_cg)
    line2y.append(m)
    x_cg = cg_formula(x_cg, x_cg_cargo1, 1, m)
    m += 1 # Increment mass 1kg

plt.plot(line2x,line2y)

x_cg_cargoloaded = x_cg
m_cargoloaded = m

print(f'Cargo loaded cg = {x_cg_cargoloaded} m, and cargoloaded mass is {m_cargoloaded} kg')

'''Passenger loading'''

# Fill window seats first (front to back)
for i in range(rows):
    for j in columns_1:
        cabin_layout[i, j] = 1
        x_cg = cg_formula(x_cg, cg_seat(i), m_passenger, total_weight)
        total_weight += m_passenger
        line3x.append(x_cg)

# Fill aisle seats next (back to front)
for i in range(rows-1, -1, -1):
    for j in columns_2:
        cabin_layout[i, j] = 1
        new_cg = cg_formula(new_cg, cg_seat(i), passenger_weight, total_weight)
        total_weight += passenger_weight
        cg_history.append(new_cg)

plt.show()


# Display the final CG
print(f"Final CG Location: {x_cg:.2f} meters")









