import numpy as np

"""---Inputs---"""
SM = 0.05           # stability margin

M_cruise = 0.413022 # cruise mach number
V_slow = 150        # slow speed in kts

b = 27.05           # span in m
A = 12              # Aspect ratio

C_bar = 2.303       # mean aerodynamic chord in m
Cr = 2.57           # root chord in m
Ct = 1.59           # tip chord in m

xi = 13.4           #length from ac of wing to ac of horizontal tail in m
zeta = 3.6          # height of the horizontal tail in m from the wing

Cr_h = 1.99         # root chord of the horizontal tail in m 
Ct_h = 1.45         # tip chord of the horizontal tail in m

Vh_V = 1            # Vh/V

b_f = 2.77          # span of the fuselage in m
h_f = 2.6           # height of the fuselage in m
l_f = 27.166        # length of the fuselage in m

l_fn = 11.1         # length of the nose untill the leading edge of the wing in m

S_h = 11.73         # horizontal tail area in m^2
b_h = 7.31          # span of the horizontal tail in m

eta = 0.95          #airfoil efficiency factor

b_n = 1.26          # span of the nacelle in m
l_n = 2.7           # distance from start of nacelle to 1/4 chord length in m


"""---Bunch of random calculations---"""
M_slow = V_slow / 661.47 # slow speed in mach number
A_h = b_h**2/S_h # aspect ratio of the horizontal tail

S = b**2/A # wing area in m^2
c_g = S/b # geometric mean chord in mS

half_b = b/2 # half span in m

sweep_quart = np.arctan((Cr - Ct)/(2*b)) # sweep angle of the wing in radians
sweep_h = np.arctan((Cr_h - Ct_h)/(b_h)) # sweep angle of the horizontal tail in radians

taper_ratio = Ct / Cr

xi_dash = xi/half_b
zeta_dash = zeta/half_b

S_net = S - Cr*b_f


A_h = b_h**2/S_h # aspect ratio of the horizontal tail
CL_h = -0.35*(A_h**(1/3))  # Lift coefficient of the horizontal tail



"""---Calculating the lift slope---"""

def CL_alpha(M, A, eta, sweep):
    beta = np.sqrt(1 - M**2)
    CL_alpha_wing = (2*np.pi*A)/(2 + np.sqrt(4+(((A * beta)/eta)**2)*(1 + ((np.tan(sweep))**2)/(beta**2))))
    CL_alpha_tail = 2*np.pi*A_h/(2 + np.sqrt(4+(((A_h * beta)/eta)**2)*(1 + ((np.tan(sweep))**2)/(beta**2))))
    CL_alpha_A_h = CL_alpha_wing*(1+2.15*b_f/b)*S_net/S+np.pi/2*(b_f**2)/S
    sweep_beta = np.arctan(np.tan(sweep) / beta)
    return CL_alpha_wing, CL_alpha_tail, CL_alpha_A_h, beta, sweep_beta

CL_alpha_w_cruise, CL_alpha_h_cruise, CL_alpha_A_h_cruise, beta_cruise, sweep_beta_cruise = CL_alpha(M_cruise, A, eta, sweep_quart)
CL_alpha_w_slow, CL_alpha_h_slow, CL_alpha_A_h_slow, beta_slow, sweep_beta_slow = CL_alpha(M_slow, A, eta, sweep_quart)


"""---Calculating d_epsilon_d_alpha---"""
# Used the USAF-DATCOM method to calculate d_epsilon_d_alpha
K_A = 1/A - 1/(1+A**1.7)
K_lambda = (10-3*taper_ratio)/7
K_H = (1- 0.5*zeta_dash)/(xi_dash**(1/3))
d_epsilon_d_alpha = 4.44*(K_A * K_lambda * K_H * np.sqrt(np.cos(sweep_quart)))


"""print statements to determine values of X_ac_w"""

print("\n-----Cruise Conditions-----")
print("Beta x A: ", beta_cruise*A)
print("sweep beta", sweep_beta_cruise)
print("Taper Ratio: ", taper_ratio)

print("\n-----Slow Speed Conditions-----")
print("Beta x A: ", beta_slow*A)
print("sweep beta", sweep_beta_slow)
print("Taper Ratio: ", taper_ratio)
print("\n")

# the following values are obtained using a plot from Torenbeek with the print statements above
X_ac_w_cruise = 0.24
X_ac_w_min = 0.24


def X_ac(X_ac_w, CL_alpha_A_h):
    fus1 = -1.8/CL_alpha_A_h * ((b_f*h_f*l_fn)/(S * C_bar))
    fus2 = 0.273/(1+taper_ratio)* ((b_f * c_g*(b-b_f))/(C_bar**2*(b + 2.15*b_f)))*np.tan(sweep_quart)
    AC_nac = -4 * (b_n**2 * l_n)/(S * C_bar * CL_alpha_A_h) * 2 #times 2 for 2 engines
    return X_ac_w + fus1 + fus2 + AC_nac

x_ac_cruise = X_ac(X_ac_w_cruise, CL_alpha_A_h_cruise)
x_ac_min = X_ac(X_ac_w_min, CL_alpha_A_h_slow)

l_h = xi

'''---To do, change the next values---'''

CL_0 = 0.65 # Maybe change

Cmac_w = -0.02*((A * (np.cos(sweep_quart))**2)/(A+2*np.cos(sweep_quart)))  # Moment coefficient about the aerodynamic center of the wing
D_fus = -1.8*(1+(2.5*b_f)/l_f)*(np.pi * b_f * h_f * l_f)/(4*S * C_bar)*(CL_0/CL_alpha_A_h_slow)
D_f = -0.4
D_nac = 0
Cmac = Cmac_w + D_f + D_fus + D_nac

# Print all variables
print("\n--- Variables ---")
print(f"CL_0: {CL_0}")
print(f"Cmac_w: {Cmac_w}")
print(f"D_fus: {D_fus}")
print(f"D_f: {D_f}")
print(f"D_nac: {D_nac}")
print(f"Cmac: {Cmac}")


alpha = 6
CL_A_h = CL_0 + CL_alpha_A_h_slow * np.pi/180 * alpha


