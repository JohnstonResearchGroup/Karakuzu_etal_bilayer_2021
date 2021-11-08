#by Seher Karakuzu

import sys
import os
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy import linalg
from scipy.optimize import minimize
from numpy.linalg import inv

from scipy.interpolate import *


data = np.loadtxt("plot_l0_tp1pt8.txt", usecols = range(0,2))
size = data.shape[0]
n0 = np.zeros((size,2),dtype = 'float')
n0= data[0:size,0:2]
omega0 = n0[:,0]



data = np.loadtxt("plot_l0_tp2.txt", usecols = range(0,2))
size = data.shape[0]
n1 = np.zeros((size,2),dtype = 'float')
n1= data[0:size,0:2]
omega1 = n1[:,0]


data = np.loadtxt("plot_l0_tp2pt2.txt", usecols = range(0,2))
size = data.shape[0]
n2 = np.zeros((size,2),dtype = 'float')
n2= data[0:size,0:2]
omega2 = n2[:,0]



data = np.loadtxt("plot_l0_tp2pt4.txt", usecols = range(0,2))
size = data.shape[0]
n3 = np.zeros((size,2),dtype = 'float')
n3= data[0:size,0:2]
omega3 = n3[:,0]


data = np.loadtxt("plot_l0_tp2pt6.txt", usecols = range(0,2))
size = data.shape[0]
n4 = np.zeros((size,2),dtype = 'float')
n4= data[0:size,0:2]
omega4 = n4[:,0]

data = np.loadtxt("plot_l0_tp2pt3.txt", usecols = range(0,2))
size = data.shape[0]
n5 = np.zeros((size,2),dtype = 'float')
n5= data[0:size,0:2]
omega5 = n5[:,0]




# %%
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']


fig1,ax1 = plt.subplots(figsize=(8,6))
ax1.plot(omega0,n0[:,1],color=colors[0],label=r"$t_{\perp}=1.8t$",marker='o')
ax1.plot(omega1,n1[:,1],color=colors[1],label=r"$t_{\perp}=2.0t$",marker='o')
ax1.plot(omega2,n2[:,1],color=colors[2],label=r"$t_{\perp}=2.2t$",marker='o')
ax1.plot(omega5,n5[:,1],color=colors[3],label=r"$t_{\perp}=2.3t$",marker='o')
ax1.plot(omega3,n3[:,1],color=colors[4],label=r"$t_{\perp}=2.4t$",marker='o')
ax1.plot(omega4,n4[:,1],color=colors[5],label=r"$t_{\perp}=2.6t$",marker='o')





ax1.set_ylabel(r'$\lambda_{s^\pm}$',fontsize=22)
ax1.set_xlabel(r'$t_{\perp}^{\prime}/t$',fontsize=19)
ax1.yaxis.tick_left() 
ax1.yaxis.set_ticks_position('both')

ax1.xaxis.tick_bottom() 
ax1.xaxis.set_ticks_position('both')
ax1.tick_params(labelsize=16)

ax1.locator_params(axis='x', nbins=5)

ax1.set_xlim([0, 0.4])
ax1.set_ylim([0.46,0.55])

ax1.legend(frameon=True, fontsize=14)
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95),
          ncol=3, fancybox=True, shadow=True, fontsize=14)


plt.show()

