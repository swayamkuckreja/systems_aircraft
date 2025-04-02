from Inputs import *
import numpy as np
import matplotlib.pyplot as plt

def Stability(Xcg_mac):
    Sh_S = 1 / (
        (CL_alpha_h_cruise / CL_alpha_A_h_cruise) 
        * (1 - d_epsilon_d_alpha) 
        * (l_h / C_bar) 
        * (Vh_V)**2
    ) * Xcg_mac - (
        (x_ac_cruise - SM) / (
            (CL_alpha_h_cruise / CL_alpha_A_h_cruise) 
            * (1 - d_epsilon_d_alpha) 
            * (l_h / C_bar) 
            * (Vh_V)**2
        )
    )
    return Sh_S

def Stability_no_SM(Xcg_mac):
    Sh_S = 1 / (
        (CL_alpha_h_cruise / CL_alpha_A_h_cruise) 
        * (1 - d_epsilon_d_alpha) 
        * (l_h / C_bar) 
        * (Vh_V)**2
    ) * Xcg_mac - (
        (x_ac_cruise) / (
            (CL_alpha_h_cruise / CL_alpha_A_h_cruise) 
            * (1 - d_epsilon_d_alpha) 
            * (l_h / C_bar) 
            * (Vh_V)**2
        )
    )
    return Sh_S

def Controllability(Xcg_mac):
    Sh_S = 1 / (
        (CL_h / CL_A_h)  
        * (l_h / C_bar) 
        * (Vh_V)**2
    ) * Xcg_mac + (
        ((Cmac)/(CL_A_h) - x_ac_min) / (
            (CL_h / CL_A_h)  
            * (l_h / C_bar) 
            * (Vh_V)**2
        )
    )
    return Sh_S

def Plot_Stability_Controllability():
    x_cg_mac = np.linspace(0, 1, 100)  # Xcg/MAC values from 0 to 1
    Sh_S_stability = []
    Sh_S_controllability = []
    Sh_S_stability_no_SM = []

    for x_cg in x_cg_mac:
        stability = Stability(x_cg)
        stability_no_SM = Stability_no_SM(x_cg)
        controllability = Controllability(x_cg)

        Sh_S_stability.append(stability if stability > -0.025 else np.nan)
        Sh_S_stability_no_SM.append(stability_no_SM if stability_no_SM > -0.04 else np.nan)
        Sh_S_controllability.append(controllability if controllability > -0.04 else np.nan)

    plt.figure(figsize=(10, 6))
    plt.plot(x_cg_mac, Sh_S_stability, label='Stability')
    plt.plot(x_cg_mac, Sh_S_stability_no_SM, label='Stability (no SM)')
    plt.plot(x_cg_mac, Sh_S_controllability, label='Controllability')
    
    # Add vertical lines for CG locations
    max_cg_location = 0.5365  # 53.65% MAC
    min_cg_location = 0.1129  # 11.29% MAC
    plt.axvline(max_cg_location, color='red', linestyle='--', label='Max CG Location (53.65% MAC)')
    plt.axvline(min_cg_location, color='blue', linestyle='--', label='Min CG Location (11.29% MAC)')
    
    plt.title('Scissor Plot')
    plt.xlabel('Xcg/MAC')
    plt.ylabel('Sh/S')
    plt.axhline(0, color='black', lw=0.5, ls='-')
    plt.ylim(-0.08, None)  # Set y-axis lower limit to -0.05
    plt.legend()
    #plt.grid()
    plt.show()

Plot_Stability_Controllability()