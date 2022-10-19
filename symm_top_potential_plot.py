import numpy as np
import matplotlib.pyplot as plt

E = -1.0
p_phi = 0.2
p_psi = 0.5
theta_arr = np.arange(0.2, np.pi - 0.2, 0.005)
cos_theta = np.cos(theta_arr)
I1 = 1.0
M = 1.0
g = 9.81
h = 0.1

def V(theta):
    return (p_phi - p_psi*np.cos(theta))**2/(2*I1*(np.sin(theta))**2) + M*g*h*np.cos(theta)

V_eff = V(theta_arr)

print(np.min(V_eff))

plt.plot(theta_arr, V_eff)
plt.show()