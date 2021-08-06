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

data = np.loadtxt("plot_l0_tpp0.0.txt", usecols = range(0,2))
size = data.shape[0]
n0 = np.zeros((size,2),dtype = 'float')
n0= data[0:size,0:2]
omega0 = n0[:,0]


#def func(x,a,b,c):
def func(x,b,c):
    #return a+b*np.log(x/c)
    return b*np.log(x/c)

popt,pconv = curve_fit(func,  1./omega0[8:-1],  1.-n0[8:-1,1])
xdata = np.linspace(0.01, 0.06, 100)
ydata = func(xdata, *popt)
print('tpp0.0: ',popt)
#plt.plot(xdata,ydata,1.-n0[:,1])
#plt.plot(xdata,ydata,1.-n0[:,1])

data = np.loadtxt("plot_l0_tpp0.75.txt", usecols = range(0,2))
size = data.shape[0]
n1 = np.zeros((size,2),dtype = 'float')
n1= data[0:size,0:2]
omega1 = n1[:,0]

popt1,pconv1 = curve_fit(func,  1./omega1[5:-1],  1.-n1[5:-1,1])
xdata1 = np.linspace(0.01, 0.07, 100)
ydata1 = func(xdata1, *popt1)
print('tpp0.75: ',popt1)


data = np.loadtxt("plot_l0_tpp0.8.txt", usecols = range(0,2))
size = data.shape[0]
n2 = np.zeros((size,2),dtype = 'float')
n2= data[0:size,0:2]
omega2 = n2[:,0]

data = np.loadtxt("plot_l0_tpp0.85.txt", usecols = range(0,2))
size = data.shape[0]
n3 = np.zeros((size,2),dtype = 'float')
n3= data[0:size,0:2]
omega3 = n3[:,0]

data = np.loadtxt("plot_l0_tpp0.9.txt", usecols = range(0,2))
size = data.shape[0]
n4 = np.zeros((size,2),dtype = 'float')
n4= data[0:size,0:2]
omega4 = n4[:,0]


data = np.loadtxt("plot_l0_tpp0.0_6x6.txt", usecols = range(0,2))
size = data.shape[0]
n5 = np.zeros((size,2),dtype = 'float')
n5= data[0:size,0:2]
omega5 = n5[:,0]



data = np.loadtxt("plot_l0_tpp0.7_6x6.txt", usecols = range(0,2))
size = data.shape[0]
n6 = np.zeros((size,2),dtype = 'float')
n6= data[0:size,0:2]
omega6 = n6[:,0]

data = np.loadtxt("plot_l0_tpp0.6_6x6.txt", usecols = range(0,2))
size = data.shape[0]
n7 = np.zeros((size,2),dtype = 'float')
n7= data[0:size,0:2]
omega7 = n7[:,0]


data = np.loadtxt("plot_l0_tpp0.3.txt", usecols = range(0,2))
size = data.shape[0]
n8 = np.zeros((size,2),dtype = 'float')
n8= data[0:size,0:2]
omega8 = n8[:,0]

popt2,pconv2 = curve_fit(func,  1./omega8,  1.-n8[:,1])
xdata2 = np.linspace(0.01, 0.075, 100)
ydata2 = func(xdata2, *popt2)
print('tpp0.3: ', popt2)


data = np.loadtxt("plot_l0_tpp0.6.txt", usecols = range(0,2))
size = data.shape[0]
n9 = np.zeros((size,2),dtype = 'float')
n9= data[0:size,0:2]
omega9 = n9[:,0]

popt3,pconv3 = curve_fit(func,  1./omega9[6:-1],  1.-n9[6:-1,1])
xdata3 = np.linspace(0.01, 0.045, 100)
ydata3 = func(xdata3, *popt3)
print('tpp0.6: ',popt3)

data = np.loadtxt("plot_l0.txt", usecols = range(0,2))
size = data.shape[0]
n10 = np.zeros((size,2),dtype = 'float')
n10= data[0:size,0:2]
omega10 = n10[:,0]

popt4,pconv4 = curve_fit(func,  1./omega10[2:-1],  1.-n10[2:-1,1])
xdata4 = np.linspace(0.01, 0.1, 100)
ydata4 = func(xdata4, *popt4)
print('2x2 n0.95 tp 2.3 tpp0: ',popt4)


data = np.loadtxt("plot_Tc_vs_tperpp.txt", usecols = range(0,2))
size = data.shape[0]
nn = np.zeros((size,2),dtype = 'float')
nn= data[0:size,0:2]
omegan = nn[:,0]




# %%
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']

#plt.style.use(['ggplot','myPlotStyle'])
#plt.style.use(['ggplot'])

fig1,ax1 = plt.subplots(figsize=(8,6))

ax1.plot(omega0,n0[:,1],color=colors[0],marker='p',linestyle='dashed',linewidth=2)



# %%
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']

#plt.style.use(['ggplot','myPlotStyle'])
#plt.style.use(['ggplot'])

fig1,ax1 = plt.subplots(figsize=(8,6))
right, bottom, width, height = [0.23, 0.60, 0.2, 0.2]
axn = fig1.add_axes([right, bottom, width, height])

ax1.plot(1./omega0,1.-n0[:,1],color=colors[0],label=r"$t_{\perp}^{\prime}=0.0$",marker='o',linewidth=2)
ax1.plot(xdata,ydata,color=colors[0],linewidth=2)
ax1.plot(1./omega8,1.-n8[:,1],color=colors[1],label=r"$t_{\perp}^{\prime}=0.3$",marker='o',linewidth=2)
ax1.plot(xdata2,ydata2,color=colors[1],linewidth=2)
ax1.plot(1./omega9,1.-n9[:,1],color=colors[2],label=r"$t_{\perp}^{\prime}=0.6$",marker='o',linewidth=2)
ax1.plot(xdata3,ydata3,color=colors[2],linewidth=2)
ax1.plot(1./omega1,1.-n1[:,1],color=colors[3],label=r"$t_{\perp}^{\prime}=0.75$",marker='o',linewidth=2)
ax1.plot(xdata1,ydata1,color=colors[3],linewidth=2)
ax1.plot(1./omega2,1.-n2[:,1],color=colors[4],label=r"$t_{\perp}^{\prime}=0.8$",marker='o',linewidth=2)
ax1.plot(1./omega3,1.-n3[:,1],color=colors[5],label=r"$t_{\perp}^{\prime}=0.85$",marker='o',linewidth=2)
ax1.plot(1./omega4,1.-n4[:,1],color=colors[6],label=r"$t_{\perp}^{\prime}=0.9$",marker='o',linewidth=2)

ax1.plot(1./omega10,1.-n10[:,1],color="blue",label=r"$t_{\perp}=2.3$, $t_{\perp}^{\prime}=0.0$",marker='o',linewidth=2)
ax1.plot(xdata4,ydata4,color="blue",linewidth=2)

axn.plot(omegan,nn[:,1],color='black',marker='p',linestyle='dashed',linewidth=2)


axn.set_ylabel(r'$T_c$',fontsize=14)
axn.set_xlabel(r'$t_{\perp}^{\prime}$',fontsize=14)
axn.yaxis.tick_left()

axn.yaxis.tick_left() 
axn.yaxis.set_ticks_position('both')

axn.tick_params(labelsize=14)
axn.xaxis.tick_bottom() 
axn.xaxis.set_ticks_position('both')

axn.set_xlim([0, 0.8])
axn.set_ylim([0.0,0.05])



ax1.set_ylabel(r'$1-\lambda_0$',fontsize=22)
ax1.set_xlabel(r'$T$',fontsize=22)
ax1.yaxis.tick_left() 
ax1.yaxis.set_ticks_position('both')

ax1.xaxis.tick_bottom() 
ax1.xaxis.set_ticks_position('both')
ax1.tick_params(labelsize=18)


ax1.locator_params(axis='x', nbins=5)


ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
          ncol=3, fancybox=True, shadow=True)


ax1.set_xlim([0, 0.125])
ax1.set_ylim([0.0,0.6])

plt.show()

