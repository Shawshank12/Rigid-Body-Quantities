import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy import optimize

E = 2.0
p_phi = 0.8
p_psi = 0.2
theta_arr = np.arange(0.2, np.pi - 0.2, 0.005)
cos_theta = np.cos(theta_arr)
I1 = 1.0
M = 5.0
g = 9.81
h = 0.1

def V(theta):
    return (p_phi - p_psi*np.cos(theta))**2/(2*I1*(np.sin(theta))**2) + M*g*h*np.cos(theta)

def V_root(theta):
    return (p_phi - p_psi*np.cos(theta))**2/(2*I1*(np.sin(theta))**2) + M*g*h*np.cos(theta) - E

def t_theta(theta, t):
    return 1/np.sqrt((2/I1)*(E - V(theta)))

sol = optimize.root_scalar(V_root, bracket=[0.5, 2.0], method = 'brentq')
sol2 = optimize.root_scalar(V_root, bracket=[2.5, 2.9], method = 'brentq')
print(sol.root)
print(sol2.root)

de_range = [sol.root+0.1, sol2.root-0.1]
t_0 = [np.pi/6] 
sol1 = solve_ivp(t_theta, de_range, t_0)
y = np.transpose(np.array(sol1.y))
t = np.array(sol1.t)
V_eff = V(theta_arr)

print(np.min(V_eff))

plt.plot(cos_theta, V_eff)
f = plt.figure()
plt.plot(t, y)
plt.show()