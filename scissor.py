import numpy as np
import matplotlib.pyplot as plt

# Parameters for new and old values
C_L_h = -0.573524889              # [-]
C_L_A_h_old = 2.307981879         # [-]
l_h = 13.30663981                 # [m]
MAC = 2.03                        # [m]
V_h_V = 0.95                      # (Vh/V)^2
C_m_ac = -0.888389154  
C_m_ac_new = -1.141346535         # [-] (latest update)
x_ac = 0.036593223 
x_ac_new = 0.002149152           # [ratio]
d_epsilon_d_alpha = 0.302437287
d_epsilon_d_alpha_new =0.257801026  # [-]
x_LEMAC = 11.56874647            # [m]
C_L_alpha_h = 4.176756141        # [1/rad] (cruise)
C_L_alpha_A_h = 6.403080015      # [1/rad] (cruise)
safety_margin_stability = 0.05    # [m]

# Old values calculations
m_controllability_old = 1/((C_L_h/C_L_A_h_old)*(l_h/MAC)*V_h_V)
c_controllability_old = ((C_m_ac/C_L_A_h_old)-x_ac)*m_controllability_old
m_stability_old = 1/(C_L_alpha_h/C_L_alpha_A_h*(1-d_epsilon_d_alpha)*l_h/MAC*V_h_V)
c_stability_old = -(x_ac-safety_margin_stability)*m_stability_old

# New values calculations
m_controllability_new = 1/((C_L_h/C_L_alpha_A_h)*(l_h/MAC)*V_h_V)
c_controllability_new = ((C_m_ac_new/C_L_alpha_A_h)-x_ac_new)*m_controllability_new
m_stability_new = 1/(C_L_alpha_h/C_L_alpha_A_h*(1-d_epsilon_d_alpha_new)*l_h/MAC*V_h_V)
c_stability_new = -(x_ac_new-safety_margin_stability)*m_stability_new

# Define x range for X_cg/MAC up to 1
x_cg_range = np.linspace(0, 1, 50)

# Calculate y values (Sh/S) for both old and new lines
y_stability_old = m_stability_old * x_cg_range + c_stability_old
y_controllability_old = m_controllability_old * x_cg_range + c_controllability_old

y_stability_new = m_stability_new * x_cg_range + c_stability_new
y_controllability_new = m_controllability_new * x_cg_range + c_controllability_new

# Create the plot
plt.figure(figsize=(10, 6))

# Plot old and new stability and controllability
plt.plot(x_cg_range, y_stability_old, 'b--', label='Stability (Old)')
plt.plot(x_cg_range, y_controllability_old, 'r--', label='Controllability (Old)')

plt.plot(x_cg_range, y_stability_new, 'b-', label='Stability (New)')
plt.plot(x_cg_range, y_controllability_new, 'r-', label='Controllability (New)')

# Set labels and title
plt.xlabel('X_cg/MAC')
plt.ylabel('Sh/S')
plt.title('Scissor Plot for Aircraft Stability and Control (Old vs New)')
plt.grid(True)
plt.legend()

# Adjust x-axis to plot up to x = 1
plt.xlim(0, 1)
plt.ylim(0, max(max(y_stability_new), max(y_controllability_new), max(y_stability_old), max(y_controllability_old)))

plt.show()
