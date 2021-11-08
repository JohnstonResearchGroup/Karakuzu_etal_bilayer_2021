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
from scipy.optimize import curve_fit


def func(x,b,c):
    #return a+b*np.log(x/c)
    return b*np.log(x/c)


n0 = np.loadtxt("SummedPhi_kz0.txt", usecols = range(0,1))
omega0 = np.loadtxt("omega.txt", usecols = range(0,1))

n1 = np.loadtxt("SummedPhi_kzpi.txt", usecols = range(0,1))



# %%
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']


fig1,ax1 = plt.subplots(figsize=(8.0,6))
ax1.plot(omega0,-n0,color=colors[0],label=r"$k_z=0$",marker='o', linewidth=2)
ax1.plot(omega0,-n1,color=colors[1],label=r"$k_z=\pi$",marker='o', linewidth=2)





ax1.set_ylabel(r'$\phi_{s^\pm}$',fontsize=22)
ax1.set_xlabel(r'$\omega/t$',fontsize=22)


ax1.yaxis.tick_left() 
ax1.yaxis.set_ticks_position('both')

ax1.tick_params(labelsize=18)
ax1.xaxis.tick_bottom() 
ax1.xaxis.set_ticks_position('both')


plt.locator_params(axis='x', nbins=8)

ax1.legend(frameon=True, fontsize=16)
ax1.set_xlim([-40, 40])
ax1.set_ylim([-0.06,0.06])

ax1.text(-38, 0.050, r"$(b)$", fontsize=22)

plt.tight_layout()

plt.show()


