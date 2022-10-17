import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

phi = 0
theta = np.pi/6
psi = 0

phi_dot = 0.0
theta_dot = 0.0
psi_dot = 0.8

I1 = 2.0
I3 = 3.0

t0 = 0
t = t0
t_end = 20
dt=0.2

omega_body = []
omega_lab = []
L = []
L_lab = []
e1pa_i = []
e2pa_i = []
e3pa_i = []
while t<t_end:
    R = np.array([[np.cos(phi)*np.cos(psi) - np.cos(theta)*np.sin(phi)*np.sin(psi), np.sin(phi)*np.cos(psi) + np.cos(theta)*np.cos(phi)*np.sin(psi), np.sin(theta)*np.sin(psi)], 
                [-1*np.cos(phi)*np.sin(psi) - np.cos(theta)*np.sin(phi)*np.cos(psi), -1*np.sin(phi)*np.sin(psi) + np.cos(theta)*np.cos(phi)*np.cos(psi), np.sin(theta)*np.cos(psi)], 
                [np.sin(theta)*np.sin(phi), -1*np.sin(theta)*np.cos(phi), np.cos(theta)]])
    e1p = np.dot(R, np.array([1,0,0]))
    e2p = np.dot(R, np.array([0,1,0]))
    e3p = np.dot(R, np.array([0,0,1]))
    e1pa_i.append(e1p)
    e2pa_i.append(e2p)
    e3pa_i.append(e3p)
    #o_body = np.array([phi_dot*np.sin(theta)*np.sin(psi) +  theta_dot*np.cos(psi), phi_dot*np.sin(theta)*np.cos(psi) -  theta_dot*np.sin(psi), phi_dot*np.cos(theta) + psi_dot])
    o_body = (phi_dot*np.sin(theta)*np.sin(psi) +  theta_dot*np.cos(psi))*e1p + (phi_dot*np.sin(theta)*np.cos(psi) -  theta_dot*np.sin(psi))*e2p + (phi_dot*np.cos(theta) + psi_dot)*e3p
    o_lab = np.dot(np.transpose(R), o_body)
    #o_lab = np.array([psi_dot*np.sin(theta)*np.sin(phi) +  theta_dot*np.cos(phi), -1*psi_dot*np.sin(theta)*np.cos(phi) +  theta_dot*np.sin(phi), psi_dot*np.cos(phi) + phi_dot])
    L_bt = np.dot(np.array([[I1, 0, 0], [0, I1, 0], [0, 0, I3]]), o_body)
    L_lt = np.dot(np.transpose(R), L_bt)
    L.append(L_bt)
    L_lab.append(L_lt)
    omega_body.append(o_body)
    omega_lab.append(o_lab)
    phi += phi_dot*dt
    theta += theta_dot*dt
    psi += psi_dot*dt
    t += dt

omega_lab_np = np.array(omega_lab)
omega_body_np = np.array(omega_body)
L_np = np.array(L)
L_lab_np = np.array(L_lab)
e1pa = np.array(e1pa_i)
e2pa = np.array(e2pa_i)
e3pa = np.array(e3pa_i)

print(np.linalg.norm(L[0]))
print(np.linalg.norm(L_lab[0]))
print(np.linalg.norm(omega_body[0]))
print(np.linalg.norm(omega_lab[0]))

fig = plt.figure()
ax = plt.axes(projection='3d')
lims = [-2, 2]
ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_zlim(lims)

def update_func(i):
    ax.cla()
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_zlim(lims)
    plt.quiver(0, 0, 0, omega_lab_np[i, 0], omega_lab_np[i, 1], omega_lab_np[i, 2])
    plt.quiver(0, 0, 0, L_lab_np[i, 0], L_lab_np[i, 1], L_lab_np[i, 2], color='black')
    plt.quiver(0, 0, 0, omega_body_np[i, 0], omega_body_np[i, 1], omega_body_np[i, 2], color='g')
    plt.quiver(0, 0, 0, L_np[i, 0], L_np[i, 1], L_np[i, 2], color='r')
    plt.quiver(0, 0, 0, e1pa[i, 0], e1pa[i, 1], e1pa[i, 2], color='y')
    plt.quiver(0, 0, 0, e2pa[i, 0], e2pa[i, 1], e2pa[i, 2], color='y')
    plt.quiver(0, 0, 0, e3pa[i, 0], e3pa[i, 1], e3pa[i, 2], color='y')

animation = anim.FuncAnimation(fig, func=update_func)
animation.save("w_alt.gif", dpi=300, fps=10)