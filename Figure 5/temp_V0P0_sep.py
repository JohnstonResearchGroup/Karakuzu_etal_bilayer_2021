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


data = np.loadtxt("plot_sep_kz_n1pt15_tp2pt8.txt", usecols = range(0,7))
size = data.shape[0]
n0 = np.zeros((size,7),dtype = 'float')
n0= data[0:size,0:7]
omega0 = 1./n0[:,0]

data = np.loadtxt("plot_sep_kz_n1pt15_tp2pt3.txt", usecols = range(0,5))
size = data.shape[0]
n3 = np.zeros((size,5),dtype = 'float')
n3= data[0:size,0:5]
omega3 = 1./n3[:,0]



data = np.loadtxt("plot_sep_kz_n1pt10_tp2pt3.txt", usecols = range(0,5))
size = data.shape[0]
n1 = np.zeros((size,5),dtype = 'float')
n1= data[0:size,0:5]
omega1 = 1./n1[:,0]



data = np.loadtxt("plot_sep_kz_n1pt05_tp2pt3.txt", usecols = range(0,5))
size = data.shape[0]
n2 = np.zeros((size,5),dtype = 'float')
n2= data[0:size,0:5]
omega2 = 1./n2[:,0]




# %%
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']

fig, ((ax1,ax2))= plt.subplots(2,1,figsize=(8,12),sharex=True, sharey=False)

ax1.plot(omega2,n2[:,1]/1000,color=colors[0],label=r"$n=1.05,t_{\perp}=2.3,t_{\perp}^{\prime}=0.0$",marker='p',linestyle='dashed',linewidth=2)
ax1.plot(omega1,n1[:,1]/1000,color=colors[1],label=r"$n=1.10,t_{\perp}=2.3,t_{\perp}^{\prime}=0.0$",marker='p',linestyle='dashed',linewidth=2)
ax1.plot(omega0,n3[:,1]/1000,color=colors[2],label=r"$n=1.15,t_{\perp}=2.3,t_{\perp}^{\prime}=0.0$",marker='p',linestyle='dashed',linewidth=2)
ax1.plot(omega0,n0[:,1]/1000,color=colors[3],label=r"$n=1.15,t_{\perp}=2.8,t_{\perp}^{\prime}=0.0$",marker='p',linestyle='dashed',linewidth=2)

ax2.plot(omega2,n2[:,2]*1000,color=colors[0],label=r"$n=1.05,t_{\perp}=2.3,t_{\perp}^{\prime}=0.0$",marker='^',linestyle='dashed',linewidth=2)
ax2.plot(omega1,n1[:,2]*1000,color=colors[1],label=r"$n=1.10,t_{\perp}=2.3,t_{\perp}^{\prime}=0.0$",marker='^',linestyle='dashed',linewidth=2)
ax2.plot(omega0,n3[:,2]*1000,color=colors[2],label=r"$n=1.15,t_{\perp}=2.3,t_{\perp}^{\prime}=0.0$",marker='^',linestyle='dashed',linewidth=2)
ax2.plot(omega0,n0[:,2]*1000,color=colors[3],label=r"$n=1.15,t_{\perp}=2.8,t_{\perp}^{\prime}=0.0$",marker='^',linestyle='dashed',linewidth=2)




ax1.set_ylabel(r'$V_{0}(T)[x 10^{-3}]$',fontsize=20)
ax1.yaxis.tick_left() 
ax1.yaxis.set_ticks_position('both')

ax1.tick_params(labelsize=18)
ax1.xaxis.tick_bottom() 
ax1.xaxis.set_ticks_position('both')


plt.locator_params(axis='x', nbins=4)

ax1.legend(frameon=True,fontsize=14)
ax1.set_xlim([0, 0.2])
ax1.set_ylim([0.0,4.0])


ax2.set_ylabel(r'$P_{0}(T)[x 10^{3}]$',fontsize=20)
ax2.set_xlabel(r'$T$',fontsize=24)
ax2.yaxis.tick_left() 
ax2.yaxis.set_ticks_position('both')

ax2.tick_params(labelsize=18)
ax2.xaxis.tick_bottom() 
ax2.xaxis.set_ticks_position('both')


plt.locator_params(axis='x', nbins=4)

ax2.legend(frameon=True,fontsize=14)
ax2.set_xlim([0, 0.2])
ax2.set_ylim([0.0,2.5])


ax1.text(0.01, 3.5, r"$(a)$", fontsize=22)
ax2.text(0.01, 2.2, r"$(b)$", fontsize=22)



plt.show()


