# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 21:54:33 2022

@author: Shashank
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

I1 = 1.0
I3 = 2.0

o1 = 1.0
o2 = 0.5
o3 = 1.0

o_pre = np.sqrt(o1**2 + o2**2)

L_lab = np.array([0, 0, np.sqrt((I1*o1)**2 + (I1*o2)**2 + (I3*o3)**2)])
w_freq = (o3*(I3 - I1))/I1

time = np.arange(0, 20, 0.2)
omega = np.array([np.array([o_pre*np.cos(w_freq*x),o_pre*np.sin(w_freq*x),o3]) for x in time])
L = np.array([np.array([I1*o_pre*np.cos(w_freq*x),I1*o_pre*np.sin(w_freq*x),I3*o3]) for x in time])
origin = np.array([[0, 0, 0],[0, 0, 0]])

print(np.linalg.norm(L[0]))
print(np.linalg.norm(L_lab))

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
    plt.quiver(0, 0, 0, omega[i,0], omega[i,1], omega[i,2], pivot='tail', color='g')
    plt.quiver(0, 0, 0, L[i,0], L[i,1], L[i,2], pivot='tail', color='r')
    #plt.quiver(0, 0, 0, L_lab[0], L_lab[1], L_lab[2], pivot='tail', color='g')
    
animation = anim.FuncAnimation(fig, func=update_func)
animation.save("w.gif", dpi=300, fps=30)