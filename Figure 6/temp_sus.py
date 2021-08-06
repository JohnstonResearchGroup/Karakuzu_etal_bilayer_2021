
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


data = np.loadtxt("sus_varyT_n1pt05_tp2pt3.txt", usecols = range(0,2))
size = data.shape[0]
n0 = np.zeros((size,2),dtype = 'float')
n0= data[0:size,0:2]
omega0 = 1./n0[:,0]


data = np.loadtxt("sus_varyT_n1pt10_tp2pt3.txt", usecols = range(0,2))
size = data.shape[0]
n1 = np.zeros((size,2),dtype = 'float')
n1= data[0:size,0:2]
omega1 = 1./n1[:,0]

data = np.loadtxt("sus_varyT_n1pt15_tp2pt3.txt", usecols = range(0,2))
size = data.shape[0]
n2 = np.zeros((size,2),dtype = 'float')
n2= data[0:size,0:2]
omega2 = 1./n2[:,0]

data = np.loadtxt("sus_varyT_n1pt15_tp2pt8.txt", usecols = range(0,2))
size = data.shape[0]
n3 = np.zeros((size,2),dtype = 'float')
n3= data[0:size,0:2]
omega3 = 1./n3[:,0]



# %%
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']


fig1,ax1 = plt.subplots(figsize=(8,6))
ax1.plot(omega0,n0[:,1],color=colors[0],label=r"$n=1.05,t_{\perp}=2.3$",marker='o', linewidth=2)
ax1.plot(omega1,n1[:,1],color=colors[1],label=r"$n=1.10,t_{\perp}=2.3$",marker='^', linewidth=2)
ax1.plot(omega2,n2[:,1],color=colors[2],label=r"$n=1.15,t_{\perp}=2.3$",marker='s', linewidth=2)
ax1.plot(omega3,n3[:,1],color=colors[3],label=r"$n=1.15,t_{\perp}=2.8$",marker='p', linewidth=2)




ax1.set_ylabel(r'$\chi_s(\mathbf{Q}=0)$',fontsize=21)
ax1.set_xlabel(r'$T$',fontsize=21)
ax1.yaxis.tick_left() 
ax1.yaxis.set_ticks_position('both')

ax1.tick_params(labelsize=18)
ax1.xaxis.tick_bottom() 
ax1.xaxis.set_ticks_position('both')


plt.locator_params(axis='x', nbins=4)

ax1.legend(frameon=True,fontsize=14)
ax1.set_xlim([0, 1.4])
ax1.set_ylim([0.05,0.3])

plt.show()


