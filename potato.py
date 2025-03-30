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

# Constant (fuel)
m_fuel = ac.mtow - ac.oew - m_cargo - m_totpassengers  # Total fuel weight (kg)
x_cg_fuel = 14.5  # CG location for fuel (meters)
print(f"Total fuel weight: {m_fuel} kg")

# Constants (MAC)
x_mac = 12.0
l_mac = 4

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
line1x.append(x_cg)
line1y.append(m)
for i in range(int(m_cargo1)):
    x_cg = cg_formula(x_cg, x_cg_cargo1, 1, m)
    m += 1 # Increment mass 1kg
    line1x.append(x_cg)
    line1y.append(m)

line1x.append(x_cg)
line1y.append(m)
for i in range(int(m_cargo2)):
    x_cg = cg_formula(x_cg, x_cg_cargo2, 1, m)
    m += 1 # Increment mass 1kg
    line1x.append(x_cg)
    line1y.append(m)

plt.plot(line1x,line1y)

# Zero to oew again

x_cg = x_cg_oew
m = ac.oew
# Back to front loaded
line2x.append(x_cg)
line2y.append(m)
for i in range(int(m_cargo2)):
    x_cg = cg_formula(x_cg, x_cg_cargo2, 1, m)
    m += 1 # Increment mass 1kg
    line2x.append(x_cg)
    line2y.append(m)

line2x.append(x_cg)
line2y.append(m)
for i in range(int(m_cargo1)):
    x_cg = cg_formula(x_cg, x_cg_cargo1, 1, m)
    m += 1 # Increment mass 1kg
    line2x.append(x_cg)
    line2y.append(m)

plt.plot(line2x,line2y)

x_cg_cargoloaded = x_cg
m_cargoloaded = m

print(f'Cargo loaded cg = {x_cg_cargoloaded} m, and cargoloaded mass is {m_cargoloaded} kg')

'''Passenger loading'''

'''Window seats'''
line3x.append(x_cg)
line3y.append(m)
# Fill window seats first (front to back)
for i in range(rows):
    for j in columns_1:
        x_cg = cg_formula(x_cg, cg_seat(i), m_passenger, m)
        m += m_passenger
        line3x.append(x_cg)
        line3y.append(m)
        print(f'seat {i,j}, weight is {m}')

plt.plot(line3x,line3y)

x_cg = x_cg_cargoloaded 
m = m_cargoloaded

# Fill window seats next (back to front)
line4x.append(x_cg)
line4y.append(m)
for i in range(rows-1, -1, -1):
    for j in columns_2:
        x_cg = cg_formula(x_cg, cg_seat(i), m_passenger, m)
        m += m_passenger
        line4x.append(x_cg)
        line4y.append(m)

plt.plot(line4x,line4y)

x_cg_windowloaded = x_cg
m_windowloaded = m

print(f'cg after window loaded = {x_cg_windowloaded}, m after window loaded = {m_windowloaded}')

'''Aisle seats'''

line5x.append(x_cg)
line5y.append(m)
# Fill window seats first (front to back)
for i in range(rows):
    for j in columns_1:
        x_cg = cg_formula(x_cg, cg_seat(i), m_passenger, m)
        m += m_passenger
        line5x.append(x_cg)
        line5y.append(m)

plt.plot(line5x,line5y)

x_cg = x_cg_windowloaded
m = m_windowloaded

# Fill window seats next (back to front)
line6x.append(x_cg)
line6y.append(m)
for i in range(rows-1, -1, -1):
    for j in columns_2:
        x_cg = cg_formula(x_cg, cg_seat(i), m_passenger, m)
        m += m_passenger
        line6x.append(x_cg)
        line6y.append(m)

plt.plot(line6x,line6y)

print(f'cg after aisle loaded = {x_cg}, m after window loaded = {m}')

'''Fuel loading'''

line7x.append(x_cg)
line7y.append(m)
for i in range(int(m_fuel)):
    x_cg = cg_formula(x_cg, x_cg_fuel, 1, m)
    m += 1 # Increment mass 1kg
    line7x.append(x_cg)
    line7y.append(m)

plt.plot(line7x,line7y)

# Plot formatting
plt.ylabel('mass [kg]')
plt.xlabel('xcg [m]')
plt.title('CG Location to Tip of Nose Cone vs Mass')
plt.grid()

plt.show()
# Display the final CG
print(f"Final CG Location: {x_cg:.2f} meters and final mass: {m:.2f} kg")

'''Do it with respect to MAC'''

line1x = np.array(line1x)
line1y = np.array(line1y)
line2x = np.array(line2x)
line2y = np.array(line2y)
line3x = np.array(line3x)
line3y = np.array(line3y)
line4x = np.array(line4x)
line4y = np.array(line4y)
line5x = np.array(line5x)
line5y = np.array(line5y)
line6x = np.array(line6x)
line6y = np.array(line6y)
line7x = np.array(line7x)
line7y = np.array(line7y)







