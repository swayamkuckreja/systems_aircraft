import numpy as np
import matplotlib.pyplot as plt
from aircraft import Aircraft 

# Initialize Aircraft object
ac = Aircraft()

# Constants
seat_pitch = 29  # in inches
seat_pitch_m = seat_pitch * 0.0254  # convert to meters
x_cg_oew = 14.5  # CG location for OEW (meters)
x_seat = 12.5  # First passenger seat location (meters)

x_cg_cargo1 = 12.4  # CG location for cargo 1 (meters)
x_cg_cargo2 = 15.4  # CG location for cargo 2 (meters)

# Function to calculate seat CG
def cg_seat(i):
    return x_seat + 0.5 * seat_pitch_m + i * seat_pitch_m  # CG at middle of seat pitch

# Function to calculate new CG
def cg_formula(old_cg, new_cg, new_weight, old_weight):
    return (old_cg * old_weight + new_cg * new_weight) / (old_weight + new_weight)

# Function to distribute cargo and update CG
def cargo(current_cg, current_weight, cargo1_weight, cargo2_weight):
    total_weight = current_weight + cargo1_weight + cargo2_weight
    new_cg = cg_formula(current_cg, x_cg_cargo1, cargo1_weight, current_weight)
    new_cg = cg_formula(new_cg, x_cg_cargo2, cargo2_weight, current_weight + cargo1_weight)
    return new_cg, total_weight

# Function to distribute passengers and update CG
def passengers(current_cg, current_weight, passenger_weight=80):
    rows, columns = 18, 4  # Define cabin layout
    cabin_layout = np.zeros((rows, columns))
    columns_1, columns_2 = [0, 3], [1, 2]  # Window and aisle seats
    
    new_cg, total_weight = current_cg, current_weight
    cg_history = [current_cg]  # Store CG values for plotting
    
    # Fill window seats first (front to back)
    for i in range(rows):
        for j in columns_1:
            cabin_layout[i, j] = 1
            new_cg = cg_formula(new_cg, cg_seat(i), passenger_weight, total_weight)
            total_weight += passenger_weight
            cg_history.append(new_cg)
    
    # Fill aisle seats next (back to front)
    for i in range(rows-1, -1, -1):
        for j in columns_2:
            cabin_layout[i, j] = 1
            new_cg = cg_formula(new_cg, cg_seat(i), passenger_weight, total_weight)
            total_weight += passenger_weight
            cg_history.append(new_cg)
    
    return new_cg, total_weight, cabin_layout, cg_history

# Initialize CG and weight
x_cg = x_cg_oew
m = ac.oew
cg_values = [x_cg]  # Store CG values for plotting

# Apply cargo loading
x_cg, m = cargo(x_cg, m, 500, 700)  # Example weights for cargo
cg_values.append(x_cg)

# Apply passenger loading
x_cg, m, layout, cg_history = passengers(x_cg, m)
cg_values.extend(cg_history)

# Plot CG shift
plt.figure(figsize=(10, 5))
plt.plot(range(len(cg_values)), cg_values, marker='o', linestyle='-')
plt.xlabel("Step")
plt.ylabel("Center of Gravity (meters)")
plt.title("Aircraft CG Shift During Loading")
plt.grid()
plt.show()

# Display the final CG
print(f"Final CG Location: {x_cg:.2f} meters")









