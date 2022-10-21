import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

phi = np.pi/2
theta = np.pi/4
psi = 0

phi_dot = 1.0
theta_dot = 0.0
psi_dot = 0.1

I1 = 2.0
I3 = 3.0

t0 = 0
t = t0
t_end = 20
dt=0.2

omega_body = []
L = []
e1pa_i = []
e2pa_i = []
e3pa_i = []

L_o = np.array([0.0, 0.0, 5.0])
CoM = []
while t<t_end:
    R = np.array([[np.cos(phi)*np.cos(psi) - np.cos(theta)*np.sin(phi)*np.sin(psi), np.sin(phi)*np.cos(psi) + np.cos(theta)*np.cos(phi)*np.sin(psi), np.sin(theta)*np.sin(psi)], 
                [-1*np.cos(phi)*np.sin(psi) - np.cos(theta)*np.sin(phi)*np.cos(psi), -1*np.sin(phi)*np.sin(psi) + np.cos(theta)*np.cos(phi)*np.cos(psi), np.sin(theta)*np.cos(psi)], 
                [np.sin(theta)*np.sin(phi), -1*np.sin(theta)*np.cos(phi), np.cos(theta)]])
    CoM_new = np.dot(np.transpose(R), L_o)
    e1p = np.dot(np.transpose(R), np.array([1,0,0]))
    e2p = np.dot(np.transpose(R), np.array([0,1,0]))
    e3p = np.dot(np.transpose(R), np.array([0,0,1]))
    '''
    e1p = np.dot(R, np.array([1,0,0]))
    e2p = np.dot(R, np.array([0,1,0]))
    e3p = np.dot(R, np.array([0,0,1]))
    '''
    e1pa_i.append(e1p)
    e2pa_i.append(e2p)
    e3pa_i.append(e3p)
    #o_body = np.array([phi_dot*np.sin(theta)*np.sin(psi) +  theta_dot*np.cos(psi), phi_dot*np.sin(theta)*np.cos(psi) -  theta_dot*np.sin(psi), phi_dot*np.cos(theta) + psi_dot])
    o_body = (phi_dot*np.sin(theta)*np.sin(psi) +  theta_dot*np.cos(psi))*e1p + (phi_dot*np.sin(theta)*np.cos(psi) -  theta_dot*np.sin(psi))*e2p + (phi_dot*np.cos(theta) + psi_dot)*e3p
    #o_lab = np.array([psi_dot*np.sin(theta)*np.sin(phi) +  theta_dot*np.cos(phi), -1*psi_dot*np.sin(theta)*np.cos(phi) +  theta_dot*np.sin(phi), psi_dot*np.cos(phi) + phi_dot])
    L_bt = np.dot(np.array([[I1, 0, 0], [0, I1, 0], [0, 0, I3]]), o_body)
    L.append(L_bt)
    omega_body.append(o_body)
    CoM.append(CoM_new)
    phi += phi_dot*dt
    theta += theta_dot*dt
    psi += psi_dot*dt
    t += dt

omega_body_np = np.array(omega_body)
L_np = np.array(L)
e1pa = np.array(e1pa_i)
e2pa = np.array(e2pa_i)
e3pa = np.array(e3pa_i)

print(L[0])
print(omega_body[0])

fig = plt.figure()
ax = plt.axes(projection='3d')
lims = [-5, 5]
ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_zlim(lims)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

def update_func(i):
    ax.cla()
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_zlim(lims)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.quiver(*CoM[i], omega_body_np[i, 0], omega_body_np[i, 1], omega_body_np[i, 2], color='c')
    plt.quiver(*CoM[i], L_np[i, 0], L_np[i, 1], L_np[i, 2], color='y')
    plt.quiver(*CoM[i], e1pa[i, 0], e1pa[i, 1], e1pa[i, 2], color='r')
    plt.quiver(*CoM[i], e2pa[i, 0], e2pa[i, 1], e2pa[i, 2], color='g')
    plt.quiver(*CoM[i], e3pa[i, 0], e3pa[i, 1], e3pa[i, 2], color='b')
    plt.quiver(0, 0, 0, 10, 0, 0, color = 'black')
    plt.quiver(0, 0, 0, 0, 10, 0, color = 'black')  
    plt.quiver(0, 0, 0, 0, 0, 10, color = 'black')

    plt.quiver(0, 0, 0, *CoM[i], color = 'grey')

animation = anim.FuncAnimation(fig, func=update_func)
animation.save("w_alt.gif", dpi=300, fps=10)