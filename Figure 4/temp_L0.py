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


data = np.loadtxt("plot_l0_n1pt15_tp2pt8.txt", usecols = range(0,2))
size = data.shape[0]
n0 = np.zeros((size,2),dtype = 'float')
n0= data[0:size,0:2]
omega0 = 1./n0[:,0]


data = np.loadtxt("plot_l0_n1pt10_tp2pt3.txt", usecols = range(0,2))
size = data.shape[0]
n1 = np.zeros((size,2),dtype = 'float')
n1= data[0:size,0:2]
omega1 = 1./n1[:,0]


popt,pconv = curve_fit(func,  omega1[1:-1],  1.-n1[1:-1,1])
xdata1 = np.linspace(0.01, 0.1, 100)
ydata1 = func(xdata1, *popt)
print(popt)


data = np.loadtxt("plot_l0_n1pt05_tp2pt3.txt", usecols = range(0,2))
size = data.shape[0]
n2 = np.zeros((size,2),dtype = 'float')
n2= data[0:size,0:2]
omega2 = 1./n2[:,0]


popt,pconv = curve_fit(func,  omega2[1:-1],  1.-n2[1:-1,1])
xdata2 = np.linspace(0.01, 0.1, 100)
ydata2 = func(xdata2, *popt)
print(popt)



data = np.loadtxt("plot_l0_n1pt15_tp2pt3.txt", usecols = range(0,2))
size = data.shape[0]
n3 = np.zeros((size,2),dtype = 'float')
n3= data[0:size,0:2]
omega3 = 1./n3[:,0]


popt,pconv = curve_fit(func,  omega3[1:-1],  1.-n3[1:-1,1])
xdata3 = np.linspace(0.01, 0.1, 100)
ydata3 = func(xdata3, *popt)
print(popt)

# %%
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']


fig1,ax1 = plt.subplots(figsize=(8,6))
ax1.plot(omega2,1-n2[:,1],color=colors[0],label=r"$n=1.05, t_{\perp}=2.3, t_{\perp}^{\prime}=0.0$",marker='o', linewidth=2)
ax1.plot(xdata2,ydata2,color=colors[0],linestyle='dashed',linewidth=2)
ax1.plot(omega1,1-n1[:,1],color=colors[1],label=r"$n=1.10, t_{\perp}=2.3, t_{\perp}^{\prime}=0.0$",marker='^', linewidth=2)
ax1.plot(xdata1,ydata1,color=colors[1],linestyle='dashed',linewidth=2)
ax1.plot(omega3,1-n3[:,1],color=colors[2],label=r"$n=1.15, t_{\perp}=2.3, t_{\perp}^{\prime}=0.0$",marker='s', linewidth=2)
ax1.plot(xdata3,ydata3,color=colors[2],linestyle='dashed',linewidth=2)
ax1.plot(omega0,1-n0[:,1],color=colors[3],label=r"$n=1.15, t_{\perp}=2.8, t_{\perp}^{\prime}=0.0$",marker='p', linewidth=2)




ax1.set_ylabel(r'$ 1 - \lambda_0$',fontsize=24)
ax1.set_xlabel(r'$T$',fontsize=24)
ax1.yaxis.tick_left() 
ax1.yaxis.set_ticks_position('both')

ax1.tick_params(labelsize=18)
ax1.xaxis.tick_bottom() 
ax1.xaxis.set_ticks_position('both')


plt.locator_params(axis='x', nbins=4)

ax1.legend(frameon=True, fontsize=14)
ax1.set_xlim([0, 0.2])
ax1.set_ylim([0.0,1.0])

plt.show()


