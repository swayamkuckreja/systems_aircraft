import matplotlib.pyplot as plt
import numpy as np

# Define constants for OEW
constants1 = {
    'Vs0': 1.221,
    'Vs1': 1.221,
    'Va': 1.221,
    'Vc': 12,
    'Vd': 17,
    'Vf': 1.221,
    'Sflaps': 0.42,
    'Sclean': 0.42,
    'W': 0.667,
    'Clmax': 1.738,
    'Clmax_HLD': 1.738,
    'rho': 1.225
}



# Define constants for 2kg
constants2 = {
    'Vs0': 2.367,
    'Vs1': 2.367,
    'Va': 2.367,
    'Vc': 13.53,
    'Vd': 17,
    'Vf': 2.367,
    'Sflaps': 0.67,
    'Sclean': 0.67,
    'W': 3.067,
    'Clmax': 1.436,
    'Clmax_HLD': 1.436,
    'rho': 1.225 
}



# Define constants for 4kg
constants3 = {
    'Vs0': 3.041,
    'Vs1': 3.041,
    'Va': 3.041,
    'Vc': 15.78,
    'Vd': 17,
    'Vf': 3.041,
    'Sflaps': 0.67,
    'Sclean': 0.67,
    'W': 5.067,
    'Clmax': 1.436,
    'Clmax_HLD': 1.436,
    'rho': 1.225 
}


# Function to calculate lines
def calculate_lines(constants):

    x2 = np.linspace(0, constants['Vs1'])
    y2 = -0.5 * constants['rho'] * x2**2 * constants['Clmax'] / constants['W'] * constants['Sclean']
    x3 = np.linspace(constants['Va'], constants['Vd'])
    y3 = (2 + 0 * x3)
    y4 = np.linspace(0, 2)
    x4 = (constants['Vd'] + 0 * y4)
    x5 = np.linspace(constants['Vc'], constants['Vd'])
    y5 = 1 / (constants['Vd'] - constants['Vc']) * x5 - 3.4 #Change this
    x6 = np.linspace(constants['Vs1'], constants['Vc'])
    y6 = (x6 * 0 - 1)
    y7 = np.linspace(0, 2)
    x7 = np.sqrt(y7 * 2 / constants['rho'] * constants['W'] / constants['Sclean'] / constants['Clmax_HLD'])
    x8 = np.linspace(0, constants['Vd'] + 2)
    y8 = (x8 * 0 + 0)
    x9 = np.linspace(x7[-1], constants['Vf'])
    y9 = (x9 * 0 +2)
    x10 = np.linspace(0, constants['Vd'] + 2) #Top
    y10 = (x10 * 0)

    return [(x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9), (x10, y10)]




# Calculate lines for all sets of data
lines1 = calculate_lines(constants1)
lines2 = calculate_lines(constants2)
lines3 = calculate_lines(constants3)


# Create a new figure with a specified size
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Function to calculate velocity lines
def calculate_velocity_lines(constants):
    Vsy = np.linspace(-1, 1)
    Vsx = (constants['Vs1'] + Vsy * 0)
    Vay = np.linspace(0, 2)
    Vax = (constants['Va'] + Vay * 0)
    Vcy = np.linspace(-1, 2)
    Vcx = (constants['Vc'] + Vcy * 0)
    Vdy = np.linspace(0, 2)
    Vdx = (constants['Vd'] + 0 * Vdy)
    Vfy = np.linspace(0,2)
    Vfx = (constants['Vf'] + 0*Vdy)
    return Vsx, Vsy, Vax, Vay, Vcx, Vcy, Vdx, Vdy, Vfx, Vfy

# Function to add velocity lines to a subplot
def add_velocity_lines(ax, constants):
    Vsx, Vsy, Vax, Vay, Vcx, Vcy, Vdx, Vdy, Vfx, Vfy = calculate_velocity_lines(constants)
    ax.plot(Vsx, Vsy, color='black', linestyle='dotted')
    ax.text(constants['Vs1'] + 1, 0.5, 'V_S', verticalalignment='bottom', horizontalalignment='left', color='black')
    ax.plot(Vax, Vay, color='black', linestyle='dotted')
    ax.text(constants['Va'] - 1, 1.5, 'V_A', verticalalignment='bottom', horizontalalignment='right', color='black')
    ax.plot(Vcx, Vcy, color='black', linestyle='dotted')
    ax.text(constants['Vc'] - 8, 1.5, 'V_C', verticalalignment='bottom', horizontalalignment='left', color='black')
    ax.plot(Vdx, Vdy, color='black', linestyle='dotted')
    ax.text(constants['Vd'] + 1.5, 1.5, 'V_D', verticalalignment='bottom', horizontalalignment='left', color='black')
    ax.plot(Vfx, Vfy, color='black', linestyle='dotted')
    ax.text(constants['Vf'] + 1.5, 1, 'V_F', verticalalignment='bottom', horizontalalignment='left', color='black')

# Plot lines for first set of data (OEW)
for i, (x, y) in enumerate(lines1):
    if i == 0:
        axs[0, 0].plot(x, y, color='black', label='OEW without Payload bay')
    else:
        axs[0, 0].plot(x, y, color='black')
add_velocity_lines(axs[0, 0], constants1)

# Plot lines for second set of data (MTOW)
for i, (x, y) in enumerate(lines2):
    if i == 0:
        axs[0, 1].plot(x, y, color='red', label='OEW with 2kg Payload')
    else:
        axs[0, 1].plot(x, y, color='red')
add_velocity_lines(axs[0, 1], constants2)

# Plot lines for third set of data (OEW + MPL)
for i, (x, y) in enumerate(lines3):
    if i == 0:
        axs[1, 0].plot(x, y, color='blue', label='OEW with 4kg Payload')
    else:
        axs[1, 0].plot(x, y, color='blue')
add_velocity_lines(axs[1, 0], constants3)

# Plot lines for all sets of data
for i, (x, y) in enumerate(lines1):
    if i == 0:
        axs[1, 1].plot(x, y, color='black', label='OEW without Payload bay')
    else:
        axs[1, 1].plot(x, y, color='black')
for i, (x, y) in enumerate(lines2):
    if i == 0:
        axs[1, 1].plot(x, y, color='red', label='OEW with 2kg Payload')
    else:
        axs[1, 1].plot(x, y, color='red')
for i, (x, y) in enumerate(lines3):
    if i == 0:
        axs[1, 1].plot(x, y, color='blue', label='OEW with 4kg Payload')
    else:
        axs[1, 1].plot(x, y, color='blue')

# Plot modifications
for ax in axs.flat:
    ax.set_title('V-n Diagram')
    ax.set_xlabel('Equivalent Airspeed (m/s)')
    ax.set_ylabel('Load Factor')
    ax.grid()
    ax.legend(loc='lower right')

plt.tight_layout()
plt.show()