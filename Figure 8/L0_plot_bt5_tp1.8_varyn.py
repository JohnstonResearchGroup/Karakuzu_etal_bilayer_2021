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


data = np.loadtxt("plot_l0_tp1pt8_n1pt15_varytpp.txt", usecols = range(0,2))
size = data.shape[0]
n0 = np.zeros((size,2),dtype = 'float')
n0= data[0:size,0:2]
omega0 = n0[:,0]



data = np.loadtxt("plot_l0_tp1pt8_n1pt10_varytpp.txt", usecols = range(0,2))
size = data.shape[0]
n1 = np.zeros((size,2),dtype = 'float')
n1= data[0:size,0:2]
omega1 = n1[:,0]


data = np.loadtxt("plot_l0_tp1pt8_n1pt05_varytpp.txt", usecols = range(0,2))
size = data.shape[0]
n2 = np.zeros((size,2),dtype = 'float')
n2= data[0:size,0:2]
omega2 = n2[:,0]




# %%
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']


fig1,ax1 = plt.subplots(figsize=(8,6.2))
ax1.plot(omega2,n2[:,1],color=colors[0],label=r"$n=1.05$",marker='o',linewidth=2)
ax1.plot(omega1,n1[:,1],color=colors[1],label=r"$n=1.10$",marker='o',linewidth=2)
ax1.plot(omega0,n0[:,1],color=colors[2],label=r"$n=1.15$",marker='o',linewidth=2)




ax1.set_ylabel(r'$\lambda_{s^\pm}$',fontsize=20)
ax1.set_xlabel(r'$t_{\perp}^{\prime}/t$',fontsize=20)
ax1.yaxis.tick_left() 
ax1.yaxis.set_ticks_position('both')

ax1.xaxis.tick_bottom() 
ax1.xaxis.set_ticks_position('both')

ax1.tick_params(labelsize=18)
ax1.locator_params(axis='x', nbins=8)
ax1.locator_params(axis='y', nbins=4)
ax1.legend(frameon=True,fontsize=14)
ax1.set_xlim([0, 1.0])
ax1.set_ylim([0.3,0.5])

plt.show()

