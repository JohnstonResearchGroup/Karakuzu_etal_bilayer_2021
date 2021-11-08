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



data = np.loadtxt("plot_l0_tpp0.0.txt", usecols = range(0,2))
size = data.shape[0]
n0 = np.zeros((size,2),dtype = 'float')
n0= data[0:size,0:2]
omega0 = n0[:,0]

popt1,pconv1 = curve_fit(func,  1./omega0[7:-1],  1.-n0[7:-1,1])
xdata1 = np.linspace(0.01, 0.1, 100)
ydata1 = func(xdata1, *popt1)
print(popt1)



data = np.loadtxt("plot_l0_tpp0.075txt", usecols = range(0,2))
size = data.shape[0]
n1 = np.zeros((size,2),dtype = 'float')
n1= data[0:size,0:2]
omega1 = n1[:,0]




# %%
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']


fig1,ax1 = plt.subplots(figsize=(8,6))
ax1.plot(1./omega0,1.-n0[:,1],color=colors[0],label=r"$t_{\perp}^{\prime}=0.0$",marker='o', linewidth=2)
ax1.plot(xdata1,ydata1,color=colors[0],linewidth=2)
ax1.plot(1./omega1,1.-n1[:,1],color=colors[1],label=r"$t_{\perp}^{\prime}=0.75t$",marker='o',linewidth=2)





ax1.set_ylabel(r'$1-\lambda_{s^\pm}$',fontsize=24)
ax1.set_xlabel(r'$T/t$',fontsize=24)
ax1.yaxis.tick_left() 
ax1.yaxis.set_ticks_position('both')

ax1.xaxis.tick_bottom() 
ax1.xaxis.set_ticks_position('both')

ax1.tick_params(labelsize=18)

ax1.locator_params(axis='y', nbins=7)
ax1.legend(frameon=True,fontsize=18)
ax1.set_xlim([0, 0.25])
ax1.set_ylim([0.0,0.7])

plt.show()

