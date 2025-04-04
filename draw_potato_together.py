from potato import mac_potato_lines_x_old, mac_potato_lines_y_old
from potato_new import mac_potato_lines_x_new, mac_potato_lines_y_new
from aircraft import Aircraft

import matplotlib.pyplot as plt
import numpy as np

# Initialize Aircraft object
ac = Aircraft()

line1x_old = mac_potato_lines_x_old[0]
line1y_old = mac_potato_lines_y_old[0]
line2x_old = mac_potato_lines_x_old[1]
line2y_old = mac_potato_lines_y_old[1]
line3x_old = mac_potato_lines_x_old[2]
line3y_old = mac_potato_lines_y_old[2]
line4x_old = mac_potato_lines_x_old[3]
line4y_old = mac_potato_lines_y_old[3]
line5x_old = mac_potato_lines_x_old[4]
line5y_old = mac_potato_lines_y_old[4]
line6x_old = mac_potato_lines_x_old[5]
line6y_old = mac_potato_lines_y_old[5]
line7x_old = mac_potato_lines_x_old[6]
line7y_old = mac_potato_lines_y_old[6]

line1x_new = mac_potato_lines_x_new[0]
line1y_new = mac_potato_lines_y_new[0]
line2x_new = mac_potato_lines_x_new[1]
line2y_new = mac_potato_lines_y_new[1]
line3x_new = mac_potato_lines_x_new[2]
line3y_new = mac_potato_lines_y_new[2]    
line4x_new = mac_potato_lines_x_new[3]
line4y_new = mac_potato_lines_y_new[3]
line5x_new = mac_potato_lines_x_new[4]
line5y_new = mac_potato_lines_y_new[4]
line6x_new = mac_potato_lines_x_new[5]
line6y_new = mac_potato_lines_y_new[5]
line7x_new = mac_potato_lines_x_new[6]
line7y_new = mac_potato_lines_y_new[6]

# TODO: Adapt code below to use new data and also make sure all the lines corresponding to new data is color red and old data is color blue 

# Define margin as 2% MAC
margin = 2  

plt.figure(figsize=(10, 8))  # Increase the figure size

# Plot OLD data in red
plt.plot(line1x_old, line1y_old, color='red', label="Old: Cargo Front to Back")
plt.plot(line2x_old, line2y_old, color='red', label="Old: Cargo Back to Front")
plt.plot(line3x_old, line3y_old, color='red', label="Old: Window Seats Front to Back")
plt.plot(line4x_old, line4y_old, color='red', label="Old: Window Seats Back to Front")
plt.plot(line5x_old, line5y_old, color='red', label="Old: Aisle Seats Front to Back")
plt.plot(line6x_old, line6y_old, color='red', label="Old: Aisle Seats Back to Front")
plt.plot(line7x_old, line7y_old, color='red', label="Old: Fuel Loading")

# Plot NEW data in blue
plt.plot(line1x_new, line1y_new, color='blue', linestyle='--', label="New: Cargo Front to Back")
plt.plot(line2x_new, line2y_new, color='blue', linestyle='--', label="New: Cargo Back to Front")
plt.plot(line3x_new, line3y_new, color='blue', linestyle='--', label="New: Window Seats Front to Back")
plt.plot(line4x_new, line4y_new, color='blue', linestyle='--', label="New: Window Seats Back to Front")
plt.plot(line5x_new, line5y_new, color='blue', linestyle='--', label="New: Aisle Seats Front to Back")
plt.plot(line6x_new, line6y_new, color='blue', linestyle='--', label="New: Aisle Seats Back to Front")
plt.plot(line7x_new, line7y_new, color='blue', linestyle='--', label="New: Fuel Loading")

# Compute CG bounds with margin (OLD)
all_cg_old = np.concatenate([line1x_old, line2x_old, line3x_old, line4x_old, line5x_old, line6x_old, line7x_old])
max_cg_old = np.max(all_cg_old) + margin
min_cg_old = np.min(all_cg_old) - margin

# Compute CG bounds with margin (NEW)
all_cg_new = np.concatenate([line1x_new, line2x_new, line3x_new, line4x_new, line5x_new, line6x_new, line7x_new])
max_cg_new = np.max(all_cg_new) + margin
min_cg_new = np.min(all_cg_new) - margin

# Adjust x and y axis
plt.xlim(-20, 100)
max_mass = max(np.max(line7y_old), np.max(line7y_new)) * 1.1
plt.ylim(ac.oew, max_mass)
plt.gca().yaxis.set_major_locator(plt.MaxNLocator(nbins=15))

# Plot CG bounds as vertical lines
plt.axvline(max_cg_old, color='red', linestyle='--', linewidth=1.2, label=f"Old Max CG + Margin ({max_cg_old:.2f} % MAC)")
plt.axvline(min_cg_old, color='red', linestyle='--', linewidth=1.2, label=f"Old Min CG - Margin ({min_cg_old:.2f} % MAC)")
plt.axvline(max_cg_new, color='blue', linestyle='--', linewidth=1.2, label=f"New Max CG + Margin ({max_cg_new:.2f} % MAC)")
plt.axvline(min_cg_new, color='blue', linestyle='--', linewidth=1.2, label=f"New Min CG - Margin ({min_cg_new:.2f} % MAC)")

# Print for reference
print(f"Old CG Range with Margin: {min_cg_old:.2f}–{max_cg_old:.2f} % MAC")
print(f"New CG Range with Margin: {min_cg_new:.2f}–{max_cg_new:.2f} % MAC")

# Labels and formatting
plt.ylabel('Mass [kg]')
plt.xlabel('CG Location [% MAC]')
plt.title('CG Location to MAC vs Mass')
plt.legend()
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.tight_layout()

plt.show()
