
# Stability and Control Parameters
import numpy as np
import matplotlib.pyplot as plt
C_L_h = -0.573524889              # [-]
C_L_A_h = 2.307981879             # [-]
l_h = 13.30663981                 # [m]
MAC = 2.03                        # [m]
V_h_V = 0.95              # (Vh/V)^2
C_m_ac = -1.199494598             # [-]
x_ac = 0.036593223                # [ratio]
d_epsilon_d_alpha = 0.302437287  # [-]
x_LEMAC = 11.56874647            # [m]
C_L_alpha_h = 4.176756141        # [1/rad]
C_L_alpha_A_h = 6.403080015      # [1/rad]
safety_margin_stability = 0.0    # [m]


m_controllability = 1/((C_L_h/C_L_A_h)*(l_h/MAC)*V_h_V)
c_controllability = ((C_m_ac/C_L_A_h)-x_ac)/m_controllability
m_stability = 1/(C_L_alpha_h/C_L_alpha_A_h*(1-d_epsilon_d_alpha)*l_h/MAC*V_h_V)
c_stability = -(x_ac-safety_margin_stability)/m_stability

# Define x range for X_cg/MAC up to 1
x_cg_range = np.linspace(0, 1, 50)

# Calculate y values (Sh/S) for both lines
y_stability = m_stability * x_cg_range + c_stability
y_controllability = m_controllability * x_cg_range + c_controllability

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_cg_range, y_stability, 'b-', label='Stability')
plt.plot(x_cg_range, y_controllability, 'r-', label='Controllability')

# Set labels and title
plt.xlabel('X_cg/MAC')
plt.ylabel('Sh/S')
plt.title('Scissor Plot for Aircraft Stability and Control')
plt.grid(True)
plt.legend()

# Adjust x-axis to plot up to x = 1
plt.xlim(0, 1)
plt.ylim(0, max(max(y_stability), max(y_controllability)))

plt.show()
