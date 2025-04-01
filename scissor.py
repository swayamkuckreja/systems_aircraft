
# Stability and Control Parameters
import numpy as np
import matplotlib.pyplot as plt
C_L_h = -0.8                      # [-] from ADSEE 3 slides
C_L_A_h = 2.307981879             # [-] from ADSEE Relations and code
l_h = 13.30663981                 # [m] from Research
MAC = 2.318049476                 # [m] from Graphical and calculation
V_h_V = 0.95                      # [m] from ADSEE 3
C_m_ac = -1.175216106             # [-] from ADSEE relations and code
x_ac = 0.031216676                # [ratio] from Research/Calculations
d_epsilon_d_alpha = 0.302437287  # [-] from ADSEE relations (maybe code)
x_LEMAC = 11.56874647            # [m] from Calculation
C_L_alpha_h = 4.176756141        # [1/rad] from Calculation
C_L_alpha_A_h = 6.403080015      # [1/rad] from Calculation/Simulation
safety_margin_stability = 0.0    # [m] from Assumption

m_controllability = 1/(C_L_h/C_L_A_h*l_h/MAC*V_h_V**2)
c_controllability = (C_m_ac/C_L_A_h-x_ac)/m_controllability
m_stability = 1/(C_L_alpha_h/C_L_alpha_A_h*(1-d_epsilon_d_alpha)*l_h/MAC*V_h_V**2)
c_stability = -(x_ac-safety_margin_stability)/m_stability

print(f"Stability slope: {m_stability}, intercept: {c_stability}")
print(f"Controllability slope: {m_controllability}, intercept: {c_controllability}")
# Define x range for X_cg/MAC
x_cg_range = np.linspace(0, 2.5, 50)  # Adjust range as needed

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

# Set axis limits to show only positive values
plt.xlim(0, 2.5)
plt.ylim(0, max(max(y_stability), max(y_controllability)))

plt.show()