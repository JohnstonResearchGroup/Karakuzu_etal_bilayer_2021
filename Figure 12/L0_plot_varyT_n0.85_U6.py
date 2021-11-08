# by Seher Karakuzu

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

data = np.loadtxt("plot_l0_tpp0.0_tp2pt4.txt", usecols = range(0,2))
size = data.shape[0]
n0 = np.zeros((size,2),dtype = 'float')
n0= data[0:size,0:2]
omega0 = n0[:,0]


#def func(x,a,b,c):
def func(x,b,c):
    #return a+b*np.log(x/c)
    return b*np.log(x/c)

popt,pconv = curve_fit(func,  1./omega0,  1.-n0[:,1])
xdata = np.linspace(0.01, 0.25, 100)
ydata = func(xdata, *popt)
print(popt)
#plt.plot(xdata,ydata,1.-n0[:,1])
#plt.plot(xdata,ydata,1.-n0[:,1])

data = np.loadtxt("plot_l0_tpp0.2_tp2pt4.txt", usecols = range(0,2))
size = data.shape[0]
n1 = np.zeros((size,2),dtype = 'float')
n1= data[0:size,0:2]
omega1 = n1[:,0]

popt1,pconv1 = curve_fit(func,  1./omega1,  1.-n1[:,1])
xdata1 = np.linspace(0.01, 0.25, 100)
ydata1 = func(xdata1, *popt1)
print(popt1)



data = np.loadtxt("plot_l0_tpp0.0_tp2pt0.txt", usecols = range(0,2))
size = data.shape[0]
n2 = np.zeros((size,2),dtype = 'float')
n2= data[0:size,0:2]
omega2 = n2[:,0]

popt2,pconv2 = curve_fit(func,  1./omega2,  1.-n2[:,1])
xdata2 = np.linspace(0.02, 0.25, 100)
ydata2 = func(xdata2, *popt2)
print(popt2)


data = np.loadtxt("plot_l0_tpp0.0_tp2pt3.txt", usecols = range(0,4))
size = data.shape[0]
n3 = np.zeros((size,4),dtype = 'float')
n3= data[0:size,0:4]
omega3 = n3[:,0]

popt3,pconv3 = curve_fit(func,  1./omega3[:],  1.-n3[:,1])
xdata3 = np.linspace(0.01, 0.1, 100)
ydata3 = func(xdata3, *popt3)
print(popt3)


# %%
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']


fig1,ax1 = plt.subplots(figsize=(8,6))
ax1.plot(1./omega0,1.-n0[:,1],color=colors[2],label=r"$t_{\perp}=2.4t,~t_{\perp}^{\prime}=0.0$",marker='o')
ax1.plot(xdata,ydata,color=colors[2])
ax1.plot(1./omega1,1.-n1[:,1],color='blue',label=r"$t_{\perp}=2.4t,~t_{\perp}^{\prime}=0.2t$",marker='o')
ax1.plot(xdata1,ydata1,color='blue')
ax1.plot(1./omega2,1.-n2[:,1],color=colors[1],label=r"$t_{\perp}=2.0t,~t_{\perp}^{\prime}=0.0$",marker='o')
ax1.plot(xdata2,ydata2,color=colors[1])
ax1.plot(1./omega3,1.-n3[:,1],color=colors[3],label=r"$t_{\perp}=2.3t,~t_{\perp}^{\prime}=0.0$",marker='o')
ax1.plot(xdata3,ydata3,color=colors[3])





ax1.set_ylabel(r'$1-\lambda_{s^\pm}$',fontsize=20)
ax1.set_xlabel(r'$T/t$',fontsize=20)
ax1.yaxis.tick_left() 
ax1.yaxis.set_ticks_position('both')

ax1.xaxis.tick_bottom() 
ax1.xaxis.set_ticks_position('both')
ax1.tick_params(labelsize=16)


ax1.legend(frameon=True, fontsize=14)
ax1.set_xlim([0, 0.25])
ax1.set_ylim([0.0,0.7])

plt.show()

